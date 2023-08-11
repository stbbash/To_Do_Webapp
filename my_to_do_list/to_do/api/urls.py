from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.getRoutes),
    path('user/create/', views.createTask),
    path('user/', views.users),
    path('user/<str:fk>/', views.userTasks),
    path('user/<str:fk>/<str:pk>/', views.getTask),
    path('user/<str:fk>/<str:pk>/update/', views.updateTask),
    path('user/<str:fk>/<str:pk>/delete/', views.deleteTask),
]


urlpatterns = format_suffix_patterns(urlpatterns)