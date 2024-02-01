from django.urls import path
from . import views

urlpatterns = [
    #user APIs
    path('create_user/', views.create_user, name="create_user"),
    path('all_users/', views.all_users, name="all_users"),
    path('get_user/', views.get_user, name="get_user"),
    path('add_book/', views.add_book, name="add_book"),
    path('all_books/', views.all_books, name="all_books"),
    path('get_book/', views.get_book, name="get_book"),
    path('update_book/', views.update_book, name="update_book"),
    path('borrow_book/', views.borrow_book, name="borrow_book"),
    path('borrowed_books/', views.borrowed_books, name="return_book"),
]