from django.db import models
from model_utils.models import TimeStampedModel
from django.shortcuts import reverse

from mptt.models import MPTTModel, TreeForeignKey

from filebrowser.fields import FileBrowseField

from core.models import Sortable, City, Profilable, Publishable
from tags.models import Taggable


class BranchType(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'branch types'


class BranchCategory(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'branch categories'


class Branch(TimeStampedModel, Sortable):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    city = models.ForeignKey(City, null=True, blank=True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    type = models.ForeignKey(BranchType, null=True, blank=True)
    categories = models.ManyToManyField(BranchCategory, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.city)

    class Meta:
        verbose_name_plural = 'branches'


class CompanyCategory(TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'company categories'



class Contact(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    company = models.CharField(max_length=255, null=True, blank=True)
    company_category = models.ForeignKey(CompanyCategory, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    city_txt = models.CharField(max_length=255, null=True, blank=True)
    replied = models.BooleanField(default=False)
    reply_message = models.TextField(null=True, blank=True)

    # TODO: add contact type


class Page(Taggable, Publishable, Profilable, TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    full_slug = models.CharField(max_length=255, editable=False)
    content = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # save the object
        super(Page, self).save(*args, **kwargs)

        # calculate full slug based on ancestors and own slug
        self.full_slug = '/'.join(self.get_ancestors(include_self=True).values_list('slug', flat=True))

        # save new full slug
        super(Page, self).save(*args, **kwargs)

        # update children
        for child in self.get_children():
            child.save()

    @property
    def my_url(self):
        return self.get_absolute_url()


    def get_absolute_url(self):
        print('call get_absolute_url for {0}'.format(self.full_slug))
        return '/{0}'.format(self.full_slug)





class ProductProperty(TimeStampedModel):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.unit)

    class Meta:
        verbose_name_plural = 'product properties'


class ProductCategory(Profilable, Publishable, Taggable, TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    full_slug = models.CharField(max_length=255, editable=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    properties = models.ManyToManyField(ProductProperty, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name

    @property
    def my_url(self):
        return self.get_absolute_url()


    def get_absolute_url(self):
        print('call get_absolute_url for {0}'.format(self.full_slug))
        return reverse('website:product_category', kwargs={'slug': self.full_slug})

    def save(self, *args, **kwargs):
        # save the object
        super(ProductCategory, self).save(*args, **kwargs)

        # calculate full slug based on ancestors and own slug
        self.full_slug = '/'.join(self.get_ancestors(include_self=True).values_list('slug', flat=True))

        # save new full slug
        super(ProductCategory, self).save(*args, **kwargs)

        # update children
        for child in self.get_children():
            child.save()


class Product(Profilable, Publishable, Taggable, TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sku = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory)
    properties = models.ManyToManyField(
        ProductProperty,
        through='ProductPropertyValue',
        through_fields=('product', 'property')
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductPropertyValue(models.Model):
    product = models.ForeignKey(Product)
    property = models.ForeignKey(ProductProperty)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{0} {1}'.format(self.value, self.property.unit)

    class Meta:
        verbose_name_plural = 'product properties values'