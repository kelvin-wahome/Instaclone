from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  pic = models.ImageField(upload_to='images/',blank=True)
  user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
  bio = models.TextField()


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)


class Image(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to = 'images/',blank=True)
  caption = models.TextField(blank = True)
  posted_on = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(User, blank=True,on_delete = models.CASCADE)
  details = models.ForeignKey(Profile, null=True)

class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment_itself= models.TextField()

class Likes(models.Model):
    who_liked=models.ForeignKey(User,on_delete=models.CASCADE, related_name='likes')
    liked_image =models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes')
