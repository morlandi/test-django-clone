import traceback
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Post
from .clone_object import clone_object


def index(request):
    return render(request, 'index.html', {
        'posts': Post.objects.all().order_by('id')
    })


def delete_post(request, id):
    try:
        post = get_object_or_404(Post, id=id)
        message = '%s <b>deleted</b>' % post
        post.delete()
        messages.info(request, mark_safe(message))
    except Exception as e:
        messages.error(request, str(e))
    return HttpResponseRedirect('/')


def clone_post(request, id):
    try:
        post = get_object_or_404(Post, id=id)
        #new_obj = post.clone()
        clone = clone_object(post)
        message = '%s <b>cloned</b> to %s' % (post, clone)
        messages.info(request, mark_safe(message))
    except Exception as e:
        messages.error(request, str(e))
        messages.error(request, traceback.format_exc())
    return HttpResponseRedirect('/')


