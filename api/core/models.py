from django.db import models
from django.conf import settings


class Event(models.Model):
    host = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    venue = models.TextField(default=' ')
    date = models.DateField()

    def __str__(self):
        return self.name + "-" + str(self.host)


class Relative(models.Model):
    name = models.CharField(max_length=127)
    message = models.CharField(max_length=255)
    address = models.CharField(max_length=127)
    with_family = models.BooleanField(default=False)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + str(self.event)


class MiniEvent(models.Model):
    name = models.CharField(max_length=255)
    venue = models.TextField(default=' ')
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + str(self.event)


class Bride(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Groom(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    relative = models.OneToOneField(to=Relative, on_delete=models.CASCADE)
    link_slug = models.CharField(max_length=10)

    def __str__(self):
        return self.relative.name
