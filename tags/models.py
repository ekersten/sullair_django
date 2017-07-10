from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Taggable(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True
