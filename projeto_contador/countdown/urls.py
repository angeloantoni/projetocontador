from django.urls import path
from .views import countdown_view

urlpatterns = [
    path('', countdown_view, name='countdown'),
    
]
