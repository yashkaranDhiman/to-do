from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name+ " -- " + str(self.user)
    