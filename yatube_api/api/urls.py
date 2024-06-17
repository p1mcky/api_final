from django.urls import include, path

from rest_framework import routers

from api import views


router = routers.DefaultRouter()

router.register('posts', views.PostViewSet, basename='posts')
router.register('groups', views.GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, basename="comments"
)
router.register('follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
