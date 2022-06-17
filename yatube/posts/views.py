from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts, 
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    description = group.description
    context = {
        'group': group,
        'posts': posts,
        'description': description,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
