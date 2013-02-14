from django.contrib import admin
from myapp.models import BlogPost, BlogComment

admin.site.register(BlogPost)
admin.site.register(BlogComment)