# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetailView, Register
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    #  Authentication routes
    path("register/", views.register, name="register"), 
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
    path("add_book/", add_book, name="add_book"),   
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),  
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
]
