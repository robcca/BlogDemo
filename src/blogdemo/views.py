from django.shortcuts import render

from posts.views import posts_list

def home(request):
    context = {
        # "posts_list":posts_list(request),
        "posts_list": 'posts/',
    }
    return render(request, 'index.html', context)
