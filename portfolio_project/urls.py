from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use custom logout view
    path('logout/', portfolio_views.custom_logout, name='logout'),
    # Include portfolio URLs with an empty prefix for the home page
    path('', include('portfolio.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
