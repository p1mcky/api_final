from django.contrib import admin

from .models import Post, Comment, Follow, Group


admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date', 'group')
    search_fields = ('text', 'author__username', 'group__title')
    list_filter = ('pub_date', 'author', 'group')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post', 'created')
    search_fields = ('text', 'author__username', 'post__text')
    list_filter = ('created', 'author', 'post')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title', 'slug', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Group, GroupAdmin)
