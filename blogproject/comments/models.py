from django.db import models

class Comment(models.Model):
    '''评论表'''
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    #关联文章
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
