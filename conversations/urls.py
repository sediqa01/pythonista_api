from django.urls import path
from conversations import views

urlpatterns = [
    path('conversations/', views.ConversationList.as_view()),
]