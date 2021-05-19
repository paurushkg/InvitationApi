from django.db import models
from django.conf import settings


class Relative(models.Model):
    name = models.CharField(max_length=127)
    message = models.CharField(max_length=255)
    address = models.CharField(max_length=127)
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):

        return self.name


class Bride(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        self.name


class Groom(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        self.name


class Event(models.Model):
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_and_time = models.DateTimeField()
    bride = models.ForeignKey(to=Bride,
                              on_delete=models.CASCADE,
                              null=False,
                              unique=True,
                            )
    groom = models.ForeignKey(to=Groom,
                              on_delete=models.CASCADE,
                              null=False,
                              unique=True,
                            )

    def __str__(self):
        return self.host.name

