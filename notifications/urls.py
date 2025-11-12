from django.urls import path
from .views import MessageCreateView, MessagesListView

urlpatterns = [
    path('', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessagesListView.as_view(), name='messages_list'),
]