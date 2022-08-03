from django.conf import settings
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

# from .forms import CommentForm, PostForm
from .models import Record



def index(request):
    record_list = Record.objects.all()
    paginator = Paginator(record_list, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'records/index.html', context)