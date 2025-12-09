from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addtask/', views.addTask, name='addTask'),
    path('mark/<int:item_id>/', views.mark_as_done, name='mark_as_done'),
    path('delete/<int:item_id>/', views.deleteTask, name='deleteTask'),
    path('edit/<int:item_id>/', views.editTask, name='editTask'),
    path('search/', views.search, name='search')
]
