"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blogapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/',include('django.contrib.auth.urls')),
    url(r'^$', views.home_page_view),
    url(r'^logout/', views.logout_view),
    url(r'^python/', views.python_blog_view),
    url(r'^signup/', views.signup_form_view),
    url(r'^blog/', views.home_page_blog_view),
    url(r'^detai/', views.detailview),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.detailview,name='pdetail'),

]
