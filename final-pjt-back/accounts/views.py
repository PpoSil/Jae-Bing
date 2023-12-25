from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def is_admin(request):
    user = get_user_model().objects.get(username=request.data["username"])
    
    if user.is_superuser:
        return Response(True, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(False)


@api_view(['POST'])
def manage_members(request):
    manager = get_user_model().objects.get(username=request.data['username'])
    
    if manager.is_superuser:
        members = get_user_model().objects.all()
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)
    
    return Response(False)


@api_view(['POST'])
def delete_members(request, member_id):
    manager = get_user_model().objects.get(username=request.data['username'])
    
    if manager.is_superuser:
        member = get_user_model().objects.get(pk=member_id)
        member.delete()
        return Response({'who': member_id})
    
    return Response(False)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response(request.user.id)


@api_view(['GET'])
def get_profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    data = serializer.data
    data['followers_count'] = user.followers.count()  # 팔로워 수 계산하여 추가
    return Response(data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    current_user = request.user
    
    if current_user == user:
        return Response({'error': '자기 자신을 팔로우할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    current_user.following.add(user)
    
    # 팔로워 수 업데이트
    user.followers_count += 1
    user.save()
    
    return Response({'success': '팔로우되었습니다.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def unfollow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    current_user = request.user
    
    if current_user == user:
        return Response({'error': '자기 자신을 언팔로우할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    current_user.following.remove(user)
    
    # 팔로워 수 업데이트
    user.followers_count -= 1
    user.save()
    
    return Response({'success': '언팔로우되었습니다.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_followers(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followers = user.followers.all()
    follower_ids = [follower.id for follower in followers]  # 팔로워의 ID 목록 추출
    return Response(follower_ids)

