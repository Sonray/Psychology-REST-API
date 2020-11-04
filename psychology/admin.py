from django.contrib import admin
from .models import Profile_User, Post, Comment

# Register your models here.

admin.site.register(Profile_User)
admin.site.register(Post)
admin.site.register(Comment)