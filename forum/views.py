from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Thread, Post
from .forms import PostForm
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

# Create your views here.
class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    content_object_name = 'threads'
    
class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all().order_by('created_at')
        context['form'] = PostForm()
        return context
    
class ThreadCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Thread
    fields = ['title', 'description']
    template_name = 'forum/thread_create.html'
    
    def test_func(self):
        return self.request.user.is_moderator or self.request.user.is_staff
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid()
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        user = self.request.user
        last_post = Post.objects.filter(thread=self.kwargs['pk']).last()
        if last_post:
            if last_post.content == form.cleaned_data.get('content'):
                form.add_error('content', 'Ви вже надіслали таке саме повідомлення')
                return super().form_invalid(form)
            if timezone.now() - last_post.created_at < timedelta(seconds=30):
                form.add_error('content', 'Ви пишете занадто часто. Очікуйте 30 секунд')
                return super().form_invalid(form)
                
                
        form.instance.author = user
        form.instance.thread = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.object.thread.get_absolute_url()