from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'post', PostListViewSet, basename='post_list')
router.register(r'posts', PostDetailViewSet, basename='post_detail')
router.register(r'follow', FollowViewSet, basename='follows')
router.register(r'story', StoryViewSet, basename='stories')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
