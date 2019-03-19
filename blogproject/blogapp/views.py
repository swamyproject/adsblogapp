from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from blogapp.form import signup_form
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def home_page_view(request):
    return render(request,'blogapp/pythonblog.html')

def python_blog_view(request):
    return render(request,'blogapp/pythonblog.html')
def logout_view(request):
    return render(request,'blogapp/logout.html')
def signup_form_view(request):
    form=signup_form()
    if request.method=='POST':
        form=signup_form(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse('/python')
    form=signup_form()
    return render(request,'blogapp/signup.html',{'form':form})
from blogapp.models import post
def home_page_blog_view(request):
    posts=post.objects.all()
    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    try:
        posts=paginator.page(page_number)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blogapp/blog.html',{'posts':posts})
def detailview(request,year,month,day,post):
    pdetail=get_object_or_404(post,slug=post,status='published', publish__year=year,publish__month=month,publish__day=day)
    return render(request,blogapp/pdetail.html,{'pdetail':pdetail})
