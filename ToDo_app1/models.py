from django.db import models

#Creates a table task in our db where the attributes will be column names
# Create your models here.
class Task(models.Model):
    #attributes
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    #When the task is created,it will return the title
    def __str__(self):
        return self.title

