from django.shortcuts import render
from django.template.context_processors import request

def post_list(request):
    return render(request, 'blog/post_list.html', {})
