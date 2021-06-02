from django.db import models
from django.conf import settings


class Relative(models.Model):
    name = models.CharField(max_length=127)
    message = models.CharField(max_length=255)
    address = models.CharField(max_length=127)
    with_family = models.BooleanField(default=False)
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + str(self.host)


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
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bride = models.OneToOneField(to=Bride,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 )
    groom = models.OneToOneField(to=Groom,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 )
    address = models.TextField(default=' ')

    def __str__(self):
        return self.name + "-" + str(self.host)


class MiniEvent(models.Model):
    name = models.CharField(max_length=255)
    date_and_time = models.DateTimeField()
    address = models.TextField(default=' ')
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + str(self.event)

