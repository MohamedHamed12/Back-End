from email.mime import image
from django.db import models
from django.contrib.auth import get_user_model 
User=get_user_model()
class PhoneModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    Mobile = models.CharField(max_length=20, blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.Mobile)




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_image', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.user.username)