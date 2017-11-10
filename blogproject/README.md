## 运行环境
```
Python 3+
Django 1.10.6
gunicorn 19.7.1
PyMySQL 0.7.11
Markdown 2.6.9
```
## 服务nginx配置

/etc/nginx/conf.d/blog.conf
```
server {
    charset utf-8;
    listen 80;  #监听端口(需把nginx默认监听端口改掉，不然该程序监听不了)
    server_name luoliang.ga;   #访问链接

    location /static {
        alias /opt/luoliang/blogproject/static;   #通过Django收集完静态文件后的目录(生成在项目根目录下)
    }

    location / {
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/blog.socket;   #blog为nginx配置文件软连
    }
}
```
### 设置nginx配置文件软连
```
sudo ln -s /etc/nginx/conf.d/blog.conf /etc/nginx/sites-enabled/blog
```
## 使用gunicorn启动应用

### 在项目根目录执行此命令
```
gunicorn --bind unix:/tmp/blog.socket blogproject.wsgi:application
```
## 项目文件配置

需在应用目录下__init__.py文件内添加：
```
import pymysql
pymysql.install_as_MySQLdb()
```

在settings文件内配置
```
INSTALLED_APPS(注册应用)
ALLOWED_HOSTS(设置访问域名)
TEMPLATES(添加DIRS HTML文件目录)
DATABASES(配置数据库信)
STATIC_ROOT(添加收集完成后静态文件目录)
```
