from django.contrib import admin
from .models import Post
from .models import Comment
from .models import CommentAttribute
from .models import PostComment


class BaseModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(BaseModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(BaseModelAdmin):
    pass


@admin.register(CommentAttribute)
class CommentAttributeAdmin(BaseModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(BaseModelAdmin):
    pass
    filter_horizontal = ['comments', ]
