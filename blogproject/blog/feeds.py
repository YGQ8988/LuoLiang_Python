from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssfeed(Feed):
    title = "洛凉 & Django"
    link = '/'
    description = "洛凉 博客文章"
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s ' % (item.category,item.title)
    def item_description(self, item):
        return item.body