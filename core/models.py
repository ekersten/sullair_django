from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from model_utils.models import TimeStampedModel


# Abstract Classes
class Profilable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(Group)

    class Meta:
        abstract = True


class Aprovable(models.Model):
    approved = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Publishable(models.Model):
    published = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Sortable(models.Model):
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True


# Non abstract models
class Country(TimeStampedModel):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=50)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class State(TimeStampedModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'states'


class City(TimeStampedModel):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'