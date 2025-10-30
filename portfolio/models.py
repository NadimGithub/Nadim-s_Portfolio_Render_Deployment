from django.db import models
from django.utils import timezone

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    degree = models.CharField(max_length=100)
    freelance = models.CharField(max_length=50)
    brief_intro = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Personal Information"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.degree

    class Meta:
        ordering = ['-end_date']
        verbose_name_plural = "Education"

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.platform

    class Meta:
        ordering = ['order']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
