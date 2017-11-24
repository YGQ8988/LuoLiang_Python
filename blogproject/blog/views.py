from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from .models import Post,Tag,Category,Message
import markdown
from comments.forms import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView
from django.db.models import Q
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.core.mail import send_mail
from time import strftime
from .m_forms import MessageForm


class IndexView(ListView):
    '''主页'''
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "post_list"
    paginate_by = 5

class ArchivesView(ListView):
    '''归档分类'''
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )

class CategoryView(IndexView):
    '''标签分类'''
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(IndexView):
    '''标签'''
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)

def about(request):
    '''关于我的页面'''
    return render(request,'blog/about.html')

def contact(request):
    '''联系我的页面'''
    form = MessageForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            mlist = Message.objects.all().order_by('-create_time')
            mail_name = '留言人名称：'
            mail_content = '留言内容：'
            mail_email = '留言人邮件地址：'
            mail_text = mail_name + mlist[0].name + '\n' + mail_email + mlist[0].user_email + '\n' + mail_content + \
                        mlist[0].user_text
            send_mail(mlist[0].user_theme, mail_text, '3301885103@qq.com',
                      ['898829225@qq.com'], fail_silently=True)
        return redirect('/contact')
    else:
        return render(request, 'blog/contact.html',context={'form':form})
# def contact(request):
#     '''联系我的页面'''
#     if request.method == "GET":
#         return render(request, 'blog/contact.html')
#     elif request.method == "POST":
#         now = strftime('%Y-%m-%d %H:%M:%S')
#         mail_name = '留言人昵称：'
#         mail_content = '留言内容：'
#         mail_email = '留言人邮箱地址：'
#         texts = {}
#         texts['name'] = request.POST['name']
#         texts['user_email'] = request.POST['email']
#         texts['user_theme'] = request.POST['subject']
#         texts['user_text'] = request.POST['message']
#         Message.objects.create(name=texts['name'],user_email=texts['user_email'],user_theme=texts['user_theme'],user_text=texts['user_text'],message_time=now)
#         mail_text = mail_name + texts['name'] + '\n\n' + mail_email + texts['user_email'] + '\n\n' + mail_content + texts['user_text']

#         send_mail(texts['user_theme'], mail_text, '3301885103@qq.com',
#                       ['898829225@qq.com'], fail_silently=True)
#         return render(request, 'blog/contact.html')

class Articles(IndexView):
    '''博客页面'''
    model = Post
    template_name = 'blog/articles.html'
    context_object_name = 'post_list'
    paginate_by = 5

def search(request):
    '''搜索页面'''
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request,'blog/index.html',{'error_msg':error_msg})
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request,'blog/index.html',{'error_msg':error_msg,'post_list':post_list})

class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        md = markdown.Markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          #'markdown.extensions.toc',
                                          TocExtension(slugify=slugify),
                                      ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

# def category(request,pk):
#     '''分类'''
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate)#.order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

# def articles(request):
#     '''博客页面'''
#     post_list = Post.objects.all()#.order_by('-created_time')
#     return render(request,'blog/articles.html',context={'post_list':post_list})

# def archives(request,year,month):
#     '''归档分类'''
#     post_list = Post.objects.filter(created_time__year=year,created_time__month=month)
#     print(post_list)
#     return render(request,'blog/index.html',context={"post_list":post_list})

# def detail(request,pk):
#     '''文章详情页'''
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views
#     post.body = markdown.markdown(post.body,
#                                      extensions=[
#                                          'markdown.extensions.extra',
#                                          'markdown.extensions.codehilite',
#                                          'markdown.extensions.toc',
#                                      ]
#                                      )
#     form = CommentForm()
#     comment_list = post.comment_set.all()
#     context = {'post':post,
#                'form':form,
#                'comment_list':comment_list}
#
#     return render(request, 'blog/detail.html',context=context)

# def index(request):
#     '''主页'''
#     post_list = Post.objects.all()#.order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})
