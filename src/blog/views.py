from django.shortcuts import redirect, render
from blog.forms import PostForm
from .models import Post


def post_list(request):
    qs = Post.objects.filter(status ='Published')
    context = {
        'object_list': qs
    }
    return render(request, 'blog/post_list.html', context)


def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)