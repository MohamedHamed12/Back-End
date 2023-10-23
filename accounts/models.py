from django.db import models

class PhoneModel(models.Model):
    Mobile = models.CharField(max_length=20, blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.Mobile)
