from django.shortcuts import render
from django.views import View
from .models import Post
class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'post': posts})

class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        posts = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/detail.html', {'post': posts})