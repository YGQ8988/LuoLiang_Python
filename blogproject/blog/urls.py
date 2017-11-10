from django.conf.urls import url,include
from . import views
from blog.feeds import AllPostRssfeed

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    #url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^about$',views.about,name='about'),
    url(r'^contact$',views.contact,name='contact'),
    url(r'^articles/$',views.Articles.as_view(),name='articles'),
    url(r'^all/rss/$',AllPostRssfeed(),name='rss'),
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
]

# urlpatterns = [
#     url(r'^$',views.index,name='index'),
#     url(r'^article/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
#     url(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$',views.archives,name='archives'),
#     url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
#     url(r'^articles/$',views.articles,name='articles'),
#     url(r'^about$',views.about,name='about'),
#     url(r'^contact$',views.contact,name='contact'),
#     url(r'^all/rss/$',AllPostRssfeed(),name='rss'),
#     url(r'^search/$', views.search, name='search'),
# ]
