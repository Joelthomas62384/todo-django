from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=50 , default="")
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50,default="")
    deleted = models.BooleanField(default = False)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.task[:20] 


