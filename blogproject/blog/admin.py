from django.contrib import admin
from .models import Post,Tag,Category


# Register your models here.
#用户名：luoliang
#密码：qq123456
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)

