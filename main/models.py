from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
from .clone_object import clone_object

User = get_user_model()


class Post(TimeStampedModel):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))

    def __str__(self):
        return super().__str__() + \
            ' (by %s) "%s": %s' % (self.author, self.title, self.content)


class Comment(TimeStampedModel):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(_('Comment'))

    def __str__(self):
        try:
            bookmarked = self.comment_attribute.is_bookmark
        except Exception as e:
            bookmarked = False
        return super().__str__() + \
            ' (by %s) [%s] %s' % (self.author, 'X' if bookmarked else ' ', self.comment)


class CommentAttribute(TimeStampedModel):
    comment = models.OneToOneField(Comment, related_name='comment_attribute', on_delete=models.CASCADE)
    is_bookmark = models.BooleanField(default=False)


class PostComment(TimeStampedModel):
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)
