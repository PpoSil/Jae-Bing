import requests

# from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
# DRF의 데코레이터. API 뷰 함수에 인증 클래스와 권한 클래스를 적용하기 위해 사용
from rest_framework.permissions import IsAuthenticated
# 인증된 사용자만이 특정 API 뷰 또는 리소스에 접근할 수 있도록 권한을 부여
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# DRF 인증 클래스. JWT(Json Web Token)인증 방식을 사용하여 사용자를 인증

from .models import Post, PostComment
from .serializers import PostSerializer, PostUserSerializer, PostCommentSerializer, PostCommentUserSerializer


# Create your views here.
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.order_by('pk')
    serializer = PostUserSerializer(posts, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def post_create(request):
    posts = request.data
    post = Post(
        user = request.user,
        title = posts['title'],
        content = posts['content'],
        post_code = 1 # 자유게시판일 경우 code는 1, 문의게시판 코드 2, .....
    )
    post.save()
    serializer = PostUserSerializer(post)

    return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = PostUserSerializer(post, context={'request': request})
    return Response(serializer.data)
    


@api_view(['DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def post_delete_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'DELETE' :
        serializer = PostUserSerializer(post)
        if request.user.is_superuser or post.user == request.user :
            post.delete()
        return Response(True)
    else :
        if post.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else : 
                print("----update error", serializer.errors)
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, post_pk):
    comments = PostComment.objects.order_by('pk').filter(post_id=post_pk)
    serializer = PostCommentUserSerializer(comments, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = request.data
    comment = PostComment(
        post = post,
        user = request.user,
        content = comments['content'],
    )
    comment.save()
    serializer = PostCommentUserSerializer(comment)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(PostComment, pk=comment_pk)
    commentId = comment.id
    if request.method == 'DELETE' :
        serializer = PostCommentSerializer(comment)
        if request.user.is_superuser or post.user == request.user :
            comment.delete()
        return Response({'id':commentId})
    else :
        if comment.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = PostCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else : 
                print("----update error", serializer.errors)
                return Response(False)
            
@api_view(['GET'])
def user_posts(request, username):
    posts = Post.objects.filter(user__username=username)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_comments(request, username):
    comments = PostComment.objects.filter(user__username=username)
    serializer = PostCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    if request.method == 'POST':
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True
    elif request.method == 'GET':
        if post.likes.filter(id=user.id).exists():
            serializer = PostUserSerializer(post, context={'request': request})
            return Response({'liked': True, 'likes_count': post.likes.count(), 'post': serializer.data})
        else:
            serializer = PostUserSerializer(post, context={'request': request})
            return Response({'liked': False, 'likes_count': post.likes.count(), 'post': serializer.data})
    serializer = PostUserSerializer(post, context={'request': request})
    return Response({'liked': liked, 'likes_count': post.likes.count(), 'post': serializer.data})

@api_view(['POST', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_pk):
    comment = get_object_or_404(PostComment, pk=comment_pk)
    user = request.user

    if comment.likes.filter(id=user.id).exists():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True

    serializer = PostCommentUserSerializer(comment, context={'request': request})
    return Response({'liked': liked, 'likes_count': comment.likes.count(), 'comment': serializer.data})