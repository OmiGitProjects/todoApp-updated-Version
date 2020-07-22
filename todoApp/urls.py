from django.urls import path
from .import views

urlpatterns = [
    path('', views.viewHomepage, name='homepage'),
    path('edit/<int:slug>/', views.editTask, name='editChanges'),
    path('remove/<int:slug>/', views.removeTask, name='removeTask')
    
]