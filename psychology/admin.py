from django.contrib import admin
from .models import Profile_User, Post, Comment

# Register your models here.

admin.site.Register(Profile_User)
admin.site.Register(Post)
admin.site.Register(Comment)