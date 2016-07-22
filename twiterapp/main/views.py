from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from twixter.models import Twixt

# Create your views here.
class ListViewTwix(View):
    """docstring for """
    def get(self, request):
        template_name = 'base.html'
        user = User.objects.get(username= 'tecmartinmelo')
        twixs = user.blog_posts.all()
        context = {
            'twits': twixs,
        }
        return render(request, template_name, context)