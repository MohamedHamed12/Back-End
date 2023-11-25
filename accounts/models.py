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
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return str(self.first_name+' '+self.last_name)

class PatientProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)