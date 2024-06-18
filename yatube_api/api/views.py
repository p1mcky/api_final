from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import AuthorOrOnlyRead
from posts.models import Group, Post, Follow
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrOnlyRead,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrOnlyRead,)

    def get_post(self):
        return get_object_or_404(
            Post.objects.all(), pk=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['following__username',]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        following = serializer.validated_data['following']
        follow, created = Follow.objects.get_or_create(
            user=user, following=following
        )
        serializer.instance = follow

    def retrieve(self, request, *args, **kwargs):
        raise NotFound
