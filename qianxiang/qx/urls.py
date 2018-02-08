from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^about/$',views.about,name='about'),
    url(r'^product/$',views.product,name='product'),
    url(r'^anli/$',views.anli,name='anli'),
    url(r'^acontact/$',views.acontact,name='acontact')
]