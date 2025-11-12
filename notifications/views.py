from django.views.generic import CreateView, ListView
from .models import Message

class MessageCreateView(CreateView):
    model = Message
    template_name = 'message_create.html'
    fields = ['first_name', 'last_name', 'phone', 'email', 'message']

class MessagesListView(ListView):
    model = Message
    template_name = 'messages_list.html'
    ordering = ['-date']