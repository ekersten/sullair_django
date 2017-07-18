from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class MenuItem(MPTTModel, TimeStampedModel):
    SELF = '_self'
    BLANK = '_blank'
    TARGET_CHOICES = (
        (SELF, 'Same Window'),
        (BLANK, 'New Window'),
    )

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    target = models.CharField(max_length=6, choices=TARGET_CHOICES, default=SELF)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
