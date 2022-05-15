from django.urls import path
from .views import get_notes

urlpatterns = [
    path('notes/', get_notes, name='get notes')
]
