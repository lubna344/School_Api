from django.db import models

# Create your models here.

######### Students Model ######

class Students(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['name']

############ Rooms Model #############

class Rooms(models.Model):
    numbers_of_rooms = models.CharField(max_length=300)
    numbers_of_students = models.CharField(max_length=100)

    class Meta:
        ordering = ['numbers_of_rooms']

####### Teachers Model ##########
class Teachers(models.Model):
    names_of_teachers = models.CharField(max_length=100)
    numbers_of_teachers = models.CharField(max_length=300)


    class Meta:
        ordering = ['names_of_teachers']

