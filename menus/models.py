from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class MenuItem(TimeStampedModel, MPTTModel):
    SELF = '_self'
    BLANK = '_blank'
    TARGET_CHOICES = (
        (SELF, 'Same Window'),
        (BLANK, 'New Window'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_root = models.BooleanField(default=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    # menu = models.ForeignKey(Menu)
    target = models.CharField(max_length=6, choices=TARGET_CHOICES, default=SELF)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.content_object is not None:
            return self.content_object.get_absolute_url()
        elif self.url:
            return self.url
