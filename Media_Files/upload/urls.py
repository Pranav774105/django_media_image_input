from django.urls import path
from .views import *

urlpatterns = [
    path('av/', Add_view, name='add_url'),
    path('sv/', Show_view, name='show_url'),
    path('uv/<int:pk>/', Update_view, name='update_url'),
    path('dv/<int:pk>/', Delete_view, name='delete_url'),
]