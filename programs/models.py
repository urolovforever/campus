from django.db import models
from django.utils.text import slugify


class Program(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, default='🌱', help_text='Emoji or icon class')
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    impact_stat = models.CharField(max_length=100, blank=True, help_text='e.g., "2.3M Trees Planted"')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Display order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
