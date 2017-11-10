gunicorn --bind unix:/tmp/blog.socket blogproject.wsgi:application
