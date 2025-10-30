from django.contrib import admin
from .models import PersonalInfo, Skill, Project, Education, SocialLink, ContactMessage

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'order')
    list_editable = ('percentage', 'order')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'percentage')
    list_filter = ('institution',)
    search_fields = ('degree', 'institution')
    ordering = ('-end_date',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order')
    list_editable = ('order',)
    list_filter = ('platform',)
    ordering = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    actions = ['mark_as_read']
