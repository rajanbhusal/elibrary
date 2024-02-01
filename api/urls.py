from django.urls import path
from . import views

urlpatterns = [
    #user APIs
    path('create_user/', views.create_user, name="create_user"),
    path('all_users/', views.all_users, name="all_users"),
    path('get_user/', views.get_user, name="get_user"),
]