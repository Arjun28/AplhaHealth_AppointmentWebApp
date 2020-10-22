from django.db import models

class Users(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Users'

    

class UsersInfo(models.Model):
    userName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName  = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'UsersInfo'


class UsersAppointments(models.Model):
    userName = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
    time  = models.CharField(max_length=8)
    reason = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'UsersAppointments'