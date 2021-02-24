from subscriptions.views import subscriptions
from django.shortcuts import redirect, render, reverse
from .models import Blog
from django.contrib import messages
from django.views import generic


class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
