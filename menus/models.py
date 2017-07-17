from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel


# Create your models here.
class MenuItem(TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)



class Menu(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
