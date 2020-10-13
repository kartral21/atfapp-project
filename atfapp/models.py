from django.db import models

# Create models here.
class User(models.Model):

    name = models.CharField(max_length=120)
    role = models.CharField(max_length=250)
    domain = models.CharField(max_length=250)
    status = models.CharField(default='new',max_length=120,editable=False)

    def __str__(self):
        return self.name