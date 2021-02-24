from subscriptions.views import subscriptions
from django.shortcuts import redirect, render, reverse
from .models import Blog
from django.contrib import messages
from profiles.models import UserProfile


def blog(request):
    """
    A view to return the blog page
    """
    # get the blog entries
    blog = Blog.objects.all()
    template = 'blog/blog.html'

    if request.user.is_anonymous:
        messages.error("Please sign up before tyou can do that!")
        return redirect(reverse('account_signup'))
    else:
        context = {
            'blog': blog
        }

    return render(request, template, context)
