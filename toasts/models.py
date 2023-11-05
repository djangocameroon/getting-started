from django.db import models

class Toast(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
