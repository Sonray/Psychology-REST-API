from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile_User(models.Model)
    Profile_pic = models.ImageField(upload_to = 'images/')
    User_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Post(models.Model)
    user_post = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    profile_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    user_profile = models.ForeignKey(Profile_User, on_delete=models.CASCADE,)

class Comment(models.Model)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)