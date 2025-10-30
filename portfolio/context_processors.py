from .models import ContactMessage

def unread_messages(request):
    if request.user.is_authenticated:
        unread_count = ContactMessage.objects.filter(is_read=False).count()
        recent_unread_messages = ContactMessage.objects.filter(is_read=False).order_by('-created_at')[:5]
        return {
            'unread_count': unread_count,
            'recent_messages': recent_unread_messages
        }
    return {
        'unread_count': 0,
        'recent_messages': []
    }
