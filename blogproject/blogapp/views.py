from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogapp.form import signup_form
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    return render(request,'blogapp/base.html')
@login_required
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
            return HttpResponse('/accounts/login')
    form=signup_form()
    return render(request,'blogapp/signup.html',{'form':form})