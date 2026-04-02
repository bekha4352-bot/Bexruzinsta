from .models import Message, Conversation

def unread_messages(request):
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(
            conversation__users=request.user,
            is_read=False
        ).exclude(sender=request.user).count()

        return {
            "unread_count": unread_count
        }
    return {}