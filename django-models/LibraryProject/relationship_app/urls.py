# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView, Register
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    #  Authentication routes
    path("register/", views.Register.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
    path("add_book/", add_book, name="add_book"),   
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),  
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
]
