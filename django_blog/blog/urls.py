from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import(
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView
)


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),              
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  
    path("post/new/", PostCreateView.as_view(), name="post-create"),   
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), 
]