from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('is-admin/', views.is_admin),
    path('manage_members/', views.manage_members),
    path('delete_members/<int:member_id>/', views.delete_members),
    path('user/', views.get_user),
    path('profile/<username>/', views.get_profile),
    path('profile/<username>/follow/', views.follow),
    path('profile/<username>/unfollow/', views.unfollow),
    path('profile/<username>/followers/', views.get_followers),
]