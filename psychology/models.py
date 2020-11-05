from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_model(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    password = models.CharField(max_length=280)


class Profile_User(models.Model):
    Profile_pic = models.ImageField(upload_to = 'images/')
    User_bio = models.TextField()
    user = models.OneToOneField(User_model, on_delete=models.CASCADE,)


class Post(models.Model):
    user_post = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    profile_id = models.ForeignKey(User_model, on_delete=models.CASCADE,)
    user_profile = models.ForeignKey(Profile_User, on_delete=models.CASCADE,)

class Comment(models.Model):
    comment = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User_model, on_delete=models.CASCADE)