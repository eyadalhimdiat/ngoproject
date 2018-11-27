from django.db import models
from django.utils import timezone


class donationtype(models.Model):
    name = models.TextField(max_length=200)
    monthlyComitment = models.BooleanField

class UserType(models.Model):
    role = models.CharField(max_length=50)


class User(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField(max_length=50)
    phone = models.IntegerField()
    role = models.ForeignKey(UserType, on_delete=models.CASCADE)
    donation = models.ForeignKey(donationtype, on_delete=models.CASCADE)
    userNamed = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name +" "+self.donation+" "+str(self.created_date.date())


