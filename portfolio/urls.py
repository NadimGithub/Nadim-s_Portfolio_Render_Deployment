from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# URL patterns for the portfolio app
app_name = 'portfolio'  # Define the URL namespace

urlpatterns = [
    # Authentication URLs
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='portfolio/admin/login.html', 
             redirect_authenticated_user=True
         ), 
         name='login'),
    
    # Existing URL patterns follow...
    path('', views.home, name='home'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Personal Info URLs
    path('dashboard/personal-info/', views.personal_info_edit, name='personal_info_edit'),
    
    # Skills URLs
    path('dashboard/skills/', views.skill_list, name='skill_list'),
    path('dashboard/skills/add/', views.skill_add, name='skill_add'),
    path('dashboard/skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('dashboard/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Projects URLs
    path('dashboard/projects/', views.project_list, name='project_list'),
    path('dashboard/projects/add/', views.project_add, name='project_add'),
    path('dashboard/projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('dashboard/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Education URLs
    path('dashboard/education/', views.education_list, name='education_list'),
    path('dashboard/education/add/', views.education_add, name='education_add'),
    path('dashboard/education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('dashboard/education/<int:pk>/delete/', views.education_delete, name='education_delete'),
    
    # Social Links URLs
    path('dashboard/social-links/', views.social_link_list, name='social_link_list'),
    path('dashboard/social-links/add/', views.social_link_add, name='social_link_add'),
    path('dashboard/social-links/<int:pk>/edit/', views.social_link_edit, name='social_link_edit'),
    path('dashboard/social-links/<int:pk>/delete/', views.social_link_delete, name='social_link_delete'),
    
    # Messages URLs
    path('dashboard/messages/', views.message_list, name='message_list'),
    path('dashboard/messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('dashboard/messages/<int:pk>/reply/', views.message_reply, name='message_reply'),
    path('dashboard/messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('dashboard/messages/bulk-action/', views.message_bulk_action, name='message_bulk_action'),
    path('dashboard/messages/<int:message_id>/mark-read/', views.mark_message_read, name='mark_message_read'),
    path('dashboard/test-email/', views.test_email, name='test_email'),
    
    # Contact URL
    path('contact/', views.contact, name='contact'),
]