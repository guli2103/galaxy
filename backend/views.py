from django.shortcuts import render
from .models import *
from django.views.generic import *

def home(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    mposts = MainPost.objects.all()
    context = {
        'posts': posts,
        'tposts': tposts,
        'mposts': mposts,
    }
    return render(request, 'index.html',context)

class AboutView(TemplateView):
    template_name = "about.html"

