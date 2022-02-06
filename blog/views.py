from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView, UpdateView


def blog(request):
    posts = Posts.objects.order_by('-pub_date')

    return render(request, 'blog.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog_detail.html'
    context_object_name = 'post'


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return _inner


@login_required
@superuser_only
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Wrong input'

    form = PostsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog_create.html', data)


class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'blog_edit.html'
    form_class = PostsForm
    context_object_name = 'post'


def post_delete(request, pk):
    post = Posts.objects.get(pk=pk) # Get your current cat

    if request.method == 'POST':         # If method is POST,
        post.delete()                     # delete the cat.
        return redirect('/blog')             # Finally, redirect to the homepage.