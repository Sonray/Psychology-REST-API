from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model)
    Profile_pic = models.ImageField(upload_to = 'images/')
    User_bio = models.TextField()
    User_email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Post(models.Model)
    comment = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    profile_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
