from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import(
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_posts, 
    PostByTagListView
    
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
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag')
]