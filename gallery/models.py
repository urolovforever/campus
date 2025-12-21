from django.db import models
from django.utils.text import slugify


class Gallery(models.Model):
    """Gallery model for storing images"""

    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('campus', 'Campus'),
        ('activity', 'Activity'),
        ('achievement', 'Achievement'),
        ('community', 'Community'),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="Slug")
    description = models.TextField(max_length=500, blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='gallery/', verbose_name="Image")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='event',
        verbose_name="Category"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
