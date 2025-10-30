from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .models import PersonalInfo, Skill, Project, Education, SocialLink, ContactMessage
from .forms import (
    PersonalInfoForm, SkillForm, ProjectForm, EducationForm,
    SocialLinkForm, ContactMessageForm, MessageReplyForm, BulkMessageActionForm
)
from functools import wraps

def admin_view_context(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Get recent messages
        recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
        
        # Call the original view function
        response = view_func(request, *args, **kwargs)
        
        # If it's a render response, add messages to the context
        if hasattr(response, 'context_data'):
            response.context_data['recent_messages'] = recent_messages
        elif isinstance(response, dict):
            response['recent_messages'] = recent_messages
        
        return response
    return wrapper

def home(request):
    personal_info = PersonalInfo.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    social_links = SocialLink.objects.all()
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio:home')
    else:
        form = ContactMessageForm()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'projects': projects,
        'education': education,
        'social_links': social_links,
        'form': form
    }
    return render(request, 'portfolio/index.html', context)

@login_required
def admin_dashboard(request):
    # Get unread messages
    unread_messages = ContactMessage.objects.filter(is_read=False).order_by('-created_at')[:3]
    
    context = {
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
        'unread_messages': unread_messages.count(),
        'recent_projects': Project.objects.all()[:5]
    }
    return render(request, 'portfolio/admin/dashboard.html', context)

# Personal Info Views
@login_required
def personal_info_edit(request):
    personal_info = PersonalInfo.objects.first()
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=personal_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal information updated successfully!')
            return redirect('portfolio:admin_dashboard')
    else:
        form = PersonalInfoForm(instance=personal_info)
    return render(request, 'portfolio/admin/personal_info_edit.html', {'form': form})

# Skills Views
@login_required
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/admin/skill_list.html', {'skills': skills})

@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('portfolio:skill_list')
    else:
        form = SkillForm()
    return render(request, 'portfolio/admin/skill_form.html', {'form': form})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('portfolio:skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portfolio/admin/skill_form.html', {'form': form})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('portfolio:skill_list')

# Projects Views
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/admin/project_list.html', {'projects': projects})

@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('portfolio:project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/admin/project_form.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('portfolio:project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/admin/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('portfolio:project_list')

# Education Views
@login_required
def education_list(request):
    education = Education.objects.all()
    return render(request, 'portfolio/admin/education_list.html', {'education': education})

@login_required
def education_add(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education added successfully!')
            return redirect('portfolio:education_list')
    else:
        form = EducationForm()
    return render(request, 'portfolio/admin/education_form.html', {'form': form})

@login_required
def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully!')
            return redirect('portfolio:education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'portfolio/admin/education_form.html', {'form': form})

@login_required
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    education.delete()
    messages.success(request, 'Education deleted successfully!')
    return redirect('portfolio:education_list')

# Social Links Views
@login_required
def social_link_list(request):
    social_links = SocialLink.objects.all()
    return render(request, 'portfolio/admin/social_link_list.html', {'social_links': social_links})

@login_required
def social_link_add(request):
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link added successfully!')
            return redirect('portfolio:social_link_list')
    else:
        form = SocialLinkForm()
    return render(request, 'portfolio/admin/social_link_form.html', {'form': form})

@login_required
def social_link_edit(request, pk):
    social_link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        form = SocialLinkForm(request.POST, instance=social_link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link updated successfully!')
            return redirect('portfolio:social_link_list')
    else:
        form = SocialLinkForm(instance=social_link)
    return render(request, 'portfolio/admin/social_link_form.html', {'form': form})

@login_required
def social_link_delete(request, pk):
    social_link = get_object_or_404(SocialLink, pk=pk)
    social_link.delete()
    messages.success(request, 'Social link deleted successfully!')
    return redirect('portfolio:social_link_list')

# Messages Views
@login_required
def admin_messages(request):
    messages = ContactMessage.objects.all()
    context = {
        'messages': messages,
        'unread_count': ContactMessage.objects.filter(is_read=False).count()
    }
    return render(request, 'portfolio/admin/messages.html', context)

@login_required
def mark_message_read(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ContactMessage, id=message_id)
        message.is_read = True
        message.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def message_list(request):
    contact_messages = ContactMessage.objects.all()
    context = {
        'contact_messages': contact_messages,
        'unread_count': ContactMessage.objects.filter(is_read=False).count()
    }
    return render(request, 'portfolio/admin/messages.html', context)

@login_required
def message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'portfolio/admin/message_detail.html', {'message': message})

@login_required
def message_reply(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            try:
                # Get form data
                subject = form.cleaned_data['subject']
                reply_text = form.cleaned_data['reply']
                
                # Create email message with proper formatting
                email_message = f"""Dear {message.name},

{reply_text}

Best regards,
Nadim Pathan"""

                # Send email
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[message.email],
                    fail_silently=False,
                )
                
                # Mark message as read
                message.is_read = True
                message.save()
                
                messages.success(request, f'Reply sent successfully to {message.email}!')
                return redirect('portfolio:message_list')
            except Exception as e:
                print(f"Email error: {str(e)}")  # For debugging
                messages.error(request, f'Failed to send reply: {str(e)}')
    else:
        # Pre-fill the subject with Re: original subject
        initial_subject = f'Re: {message.subject}' if message.subject else 'Re: Your Message'
        form = MessageReplyForm(initial={'subject': initial_subject})
    
    return render(request, 'portfolio/admin/message_reply.html', {
        'form': form,
        'message': message
    })

@login_required
def message_bulk_action(request):
    if request.method == 'POST':
        form = BulkMessageActionForm(request.POST, messages=ContactMessage.objects.all())
        if form.is_valid():
            action = form.cleaned_data['action']
            message_ids = form.cleaned_data['selected_messages']
            messages_to_update = ContactMessage.objects.filter(id__in=message_ids)
            
            if action == 'mark_read':
                messages_to_update.update(is_read=True)
                messages.success(request, 'Selected messages marked as read!')
            elif action == 'mark_unread':
                messages_to_update.update(is_read=False)
                messages.success(request, 'Selected messages marked as unread!')
            elif action == 'delete':
                messages_to_update.delete()
                messages.success(request, 'Selected messages deleted!')
                
    return redirect('portfolio:message_list')

@login_required
def message_delete(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    messages.success(request, 'Message deleted successfully!')
    return redirect('portfolio:message_list')

@login_required
def test_email(request):
    try:
        send_mail(
            subject='Test Email',
            message='This is a test email to verify the email configuration.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # Sending to the same email for testing
            fail_silently=False,
        )
        return JsonResponse({'status': 'success', 'message': 'Test email sent successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    return redirect('portfolio:index')

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def custom_logout(request):
    logout(request)
    return redirect('portfolio:home')
