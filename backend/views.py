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


class ContactView(TemplateView):
    template_name = 'contact.html';

class Index2View(TemplateView):
    template_name = 'index-2.html';

class CategoryView(TemplateView):
    template_name = 'category.html' ; 

class PostdetailsView(TemplateView):
    template_name = 'post-details.html';

class PrivacyView(TemplateView):
    template_name = 'privacy.html';        

