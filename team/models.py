from django.db import models


class TeamMember(models.Model):
    """Model representing a team member"""
    name = models.CharField(max_length=200, verbose_name="Full Name")
    role = models.CharField(max_length=200, verbose_name="Role/Position")
    email = models.EmailField(verbose_name="Email Address")
    linkedin = models.URLField(max_length=500, blank=True, null=True, verbose_name="LinkedIn Profile")
    twitter = models.URLField(max_length=500, blank=True, null=True, verbose_name="Twitter Profile")
    image = models.ImageField(upload_to='team/', verbose_name="Profile Image")
    order = models.IntegerField(default=0, verbose_name="Display Order")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"
