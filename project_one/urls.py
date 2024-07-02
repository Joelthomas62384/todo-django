
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('tasks',views.tasks,name='tasks'),
    path('task_delete/<str:id>',views.task_delete,name='task_delete'),
    path('task_done/<str:id>',views.task_done,name='task_done'),


    path('about',views.about,name='about'),
]
