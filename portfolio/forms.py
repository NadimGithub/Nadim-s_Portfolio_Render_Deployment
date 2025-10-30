from django import forms
from .models import PersonalInfo, Skill, Project, Education, SocialLink, ContactMessage

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'title', 'birthday', 'website', 'phone', 'city', 'email', 'degree', 'freelance', 'brief_intro']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'brief_intro': forms.Textarea(attrs={'rows': 4}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage', 'order']
        widgets = {
            'percentage': forms.NumberInput(attrs={
                'min': '0',
                'max': '100',
                'step': '5'
            })
        }

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage < 0 or percentage > 100:
            raise forms.ValidationError('Percentage must be between 0 and 100')
        return percentage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'github_link', 'live_demo_link', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError('End date must be after start date')
        return cleaned_data

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'order']
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if not url.startswith(('http://', 'https://')):
            raise forms.ValidationError('URL must start with http:// or https://')
        return url

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class MessageReplyForm(forms.Form):
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter subject'
        })
    )
    reply = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Type your reply message here...'
        })
    )
    mark_as_replied = forms.BooleanField(required=False, initial=True)

class BulkMessageActionForm(forms.Form):
    ACTIONS = (
        ('mark_read', 'Mark as Read'),
        ('mark_unread', 'Mark as Unread'),
        ('delete', 'Delete Selected')
    )
    
    action = forms.ChoiceField(choices=ACTIONS)
    selected_messages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        messages = kwargs.pop('messages', None)
        super().__init__(*args, **kwargs)
        if messages:
            self.fields['selected_messages'].choices = [
                (message.id, str(message)) for message in messages
            ]
