from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecordForm, TextForm
from .models import Record, Text


def index(request):
    record_list = Record.objects.all()
    paginator = Paginator(record_list, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "records/index.html", context)

def record_detail(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    texts = record.texts.all()
    form = TextForm()
    context = {
        "record": record,
        "texts": texts,
        "form": form,
    }
    return render(request, "records/record_detail.html", context)


def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.author = request.user
        record.save()
        return redirect("logs:index")
    return render(request, "records/record_create.html", {"form": form})


def text_create(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = TextForm(request.POST or None)
    if form.is_valid():
        text = form.save(commit=False)
        text.record = record
        text.save()
        return redirect('logs:record_detail', record_id)
        
    context = {
        'form': form,
    }
    return render(request, 'records/text_create.html', context)


def text_edit(request, text_id):
    text = get_object_or_404(Text, id=text_id)
    # if request.user != post.author:
    #     return redirect('posts:post_detail', post_id)

    form = TextForm(
        request.POST or None,
        instance=text
    )
    if form.is_valid():
        form.save()
        return redirect('logs:record_detail', text.record.id)
    context = {'form': form, 'text': text, 'is_edit': True}
    return render(request, 'records/text_create.html', context)
    



# def post_create(request):
#     form = PostForm(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
#         return redirect('posts:profile', request.user)
#     return render(request, 'posts/create_post.html', {'form': form})

# def record_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.user != post.author:
#         return redirect('posts:post_detail', post_id)

#     form = PostForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=post
#     )
#     if form.is_valid():
#         form.save()
#         return redirect('posts:post_detail', post_id)
#     context = {'form': form, 'post': post, 'is_edit': True}
#     return render(request, 'posts/create_post.html', context)




# def index(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list, settings.POSTS_FOR_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, 'posts/index.html', context)


# def group_posts(request, slug):
#     group = get_object_or_404(Group, slug=slug)
#     post_list = group.posts.all()
#     paginator = Paginator(post_list, settings.POSTS_FOR_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'group': group,
#         'page_obj': page_obj,
#     }
#     return render(request, 'posts/group_list.html', context)


# def profile(request, username):
#     author = get_object_or_404(User, username=username)
#     profile_posts = author.posts.all()
#     paginator = Paginator(profile_posts, settings.POSTS_FOR_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     following = False
#     if request.user.is_authenticated:
#         following = Follow.objects.filter(
#             user=request.user, author=author
#         ).exists()

#     context = {
#         'author': author,
#         'page_obj': page_obj,
#         'following': following,
#     }
#     return render(request, 'posts/profile.html', context)


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     comments = post.comments.all()
#     form = CommentForm()
#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form,
#     }
#     return render(request, 'posts/post_detail.html', context)


# @login_required
# def post_create(request):
#     form = PostForm(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
#         return redirect('posts:profile', request.user)
#     return render(request, 'posts/create_post.html', {'form': form})


# @login_required
# def post_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.user != post.author:
#         return redirect('posts:post_detail', post_id)

#     form = PostForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=post
#     )
#     if form.is_valid():
#         form.save()
#         return redirect('posts:post_detail', post_id)
#     context = {'form': form, 'post': post, 'is_edit': True}
#     return render(request, 'posts/create_post.html', context)


# @login_required
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.author = request.user
#         comment.post = post
#         comment.save()
#     return redirect('posts:post_detail', post_id=post_id)


# @login_required
# def follow_index(request):
#     post_list = Post.objects.filter(author__following__user=request.user)
#     paginator = Paginator(post_list, settings.POSTS_FOR_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, 'posts/follow.html', context)


# @login_required
# def profile_follow(request, username):
#     author = get_object_or_404(User, username=username)
#     if Follow.objects.filter(user=request.user, author=author).exists():
#         return redirect('posts:profile', username=username)

#     if request.user != author:
#         Follow.objects.create(
#             user=request.user,
#             author=author,
#         )
#     return redirect('posts:profile', username=username)


# @login_required
# def profile_unfollow(request, username):
#     author = get_object_or_404(User, username=username)
#     obj = Follow.objects.filter(user=request.user, author=author)
#     obj.delete()
#     return redirect('posts:profile', username=username)
