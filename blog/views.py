from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from next_prev import next_in_order, prev_in_order
from .models import *
from .forms import *


class HomePage(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by tag: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.POST.get('parent', None):
                comment.parent_id = int(request.POST.get('parent'))
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(post.get_absolute_url(), pk=post.pk)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    try:
        next_post = post.get_next_by_created_at()
    except Post.DoesNotExist:
        next_post = None

    try:
        previous_post = post.get_previous_by_created_at()
    except Post.DoesNotExist:
        previous_post = None

    return render(request, 'blog/single.html', {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post
    })