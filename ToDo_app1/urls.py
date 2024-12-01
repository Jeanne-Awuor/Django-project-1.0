from django.urls import path
from . import views
#Where we map our routes to the functions
urlpatterns =[
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),
]