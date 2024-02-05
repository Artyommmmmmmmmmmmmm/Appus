from django.urls import path, include
from django.views.generic import TemplateView
from .views import FilePage, word_count, clean
urlpatterns = [
    path('file/', FilePage.as_view(), name='file'),
    path('find/', word_count, name='files'),
    path('del/', clean, name='del'),
]   