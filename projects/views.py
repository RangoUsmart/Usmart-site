from time import timezone
from django.shortcuts import render, redirect,  get_object_or_404
from django.views.generic.base import View
from .models import Post
from .forms import PostForm
# Вивід всіх проектів
class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog.html", {'post_list': posts})

# Вивід одного проєкту
class PostProject(View):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "article.html", {'post': post})


# def post_new(request):
#     form = PostForm()
#     return render(request, 'post_edit.html', {'form': form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # post.author = request.user
            # post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # print(post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
