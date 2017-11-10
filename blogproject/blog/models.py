from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import markdown
from django.utils.html import strip_tags

class Category(models.Model):
    '''分类表'''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    '''标签表'''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    '''文章表'''
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateField()   #DateTimeField()
    modified_time = models.DateField()  #DateTimeField()
    excerpt = models.CharField(max_length=100,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']

class Message(models.Model):
    '''留言表'''
    name = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_theme = models.CharField(max_length=100)
    user_text = models.TextField()
    message_time = models.DateTimeField()

    def __str__(self):
        return self.user_email