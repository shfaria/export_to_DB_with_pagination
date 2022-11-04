from django.db import models

class Demo(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
