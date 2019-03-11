from django.db import models

class Profile(models.Model):
  pic = models.ImageField(upload_to='images/',blank=True)
  user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
  bio = models.TextField()

class Image(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to = 'images/',blank=True)
  caption = models.TextField(blank = True)
  posted_on = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(User, blank=True,on_delete = models.CASCADE)
  details = models.ForeignKey(Profile, null=True)
