from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    purchase = models.IntegerField(default=0)
    createdAt = models.DateTimeField(
            default=timezone.now)
    deletedAt = models.DateTimeField(
            blank=True, null=True)

    def delete(self):
        self.deletedAt = timezone.now()
        self.save()

    def __str__(self):
        return self.name
