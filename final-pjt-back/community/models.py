from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model



def set_FK_Model_user():
    return get_user_model().objects.get(username="삭제된유저")

# new
# def get_deleted_user():
#     User = get_user_model()
#     deleted_user = User.objects.get(username="삭제된유저")
#     return deleted_user

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(set_FK_Model_user))
    # ㄴ 삭제된 유저일 경우 set_FK_Model_user() 함수를 호출하여 설정
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(set_FK_Model_user))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_comments', blank=True)
