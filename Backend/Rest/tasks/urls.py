from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='tasks_list'),
    path('tasks/<str:pk>/', views.task_detail, name='task_detail')
]