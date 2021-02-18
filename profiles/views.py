from django.shortcuts import render


def profile(request):
    """
    Dispay the users's profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
