from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class post(models.Model):
    status_choices=(('draft','Draft'),('publish','Publish'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='publish')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=status_choices,default='draft')

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

    def get_obsolute_url(self):
        return reverse('pdetail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])





