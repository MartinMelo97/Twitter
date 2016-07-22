from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import Twixt
from .forms import *

class ListViewTwix(View):
    """docstring for """
    def get(self, arg):
        template_name = 'base.html'
        twixs = blog_posts.all()
        context = {
            'twits': twixs,
        }
        return render(request, template_name, context)

class DetailViewTiwx(View):
    """docstring for """
    def get(self, arg, slug):
        template_name = 'detalleTwix.html'
        post = Twixt.object.get(slug = slug)
        context = {
            'twits': post,
        }
        return render(request, template_name, context)

class NewTwit(View):
    """docstring for NewTwit"""
    def get(self, arg):
        template_name = 'NewTwixter.html'
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)
