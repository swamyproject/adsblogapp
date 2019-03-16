from django.contrib import admin
from blogapp.models import post
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display =['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','publish')

admin.site.register(post,postadmin)


