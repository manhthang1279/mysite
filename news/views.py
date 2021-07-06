from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from .models import Posts, Comment


# Create your views here.
def home(request):
    first_posts = Posts.objects.order_by('-id').first()
    all_posts = Posts.objects.all().order_by('-id')[1:]
    paginator = Paginator(all_posts, 5)

    page_number = request.GET.get('page')
    all_posts = paginator.get_page(page_number)
    return render(request, 'home.html', {
        'first_posts': first_posts,
        'all_posts': all_posts
    })


def detail(request, pk):
    posts_list = Posts.objects.all().order_by('-id')
    post = Posts.objects.get(id=pk)
    paginator = Paginator(posts_list, 3)

    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            comment=comment,
        )
        messages.success(request, 'Bình luận của bạn đã được gửi và chờ kiểm duyệt.')
    comments = Comment.objects.filter(post=post, status=True).order_by('-id')
    count_comments = len(comments)
    return render(request, 'detail.html', {
        'post': post,
        'posts_list': posts_list,
        'comments': comments,
        'count_comments': count_comments
    })
