from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from rest_framework import generics, viewsets, permissions, filters
from models import Post, Profile
from serializers import postserializer, ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm




from .forms import CustomUserCreationForm, ProfileForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    # automatically log in the user after registration
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('profile')
        else:
         messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




@login_required
def profile(request):
    user = request.user
    profile = user.profile


    if request.method == 'POST':
        u_form = None
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
    # If you want to allow changing username/email, create a separate form for User
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile was updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
     p_form = ProfileForm(instance=profile)


    return render(request, 'registration/profile.html', {
    'p_form': p_form,
    })


class PostListView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=postserializer
    permission_classes=IsAuthenticatedOrReadOnly

class PostDetailView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=postserializer
    permission_classes= IsAuthenticatedOrReadOnly

class PostCreateView(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=postserializer
    permission_classes= IsAuthenticatedOrReadOnly

class PostUpdateView(generics.UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=postserializer
    permission_classes= IsAuthenticatedOrReadOnly

class PostDeleteView(generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=postserializer
    permission_classes= IsAuthenticatedOrReadOnly


# Create Comment (used if you want a separate page for creating comments,
# but usually handled inline on post_detail)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.kwargs['pk']})


# Update Comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_edit.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        return self.get_object().author == self.request.user


# Delete Comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        return self.get_object().author == self.request.user

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(   # <-- "Post.objects.filter"
        Q(title__icontains=query) |  # <-- "title__icontains"
        Q(content__icontains=query) |  # <-- "content__icontains"
        Q(tags__name__icontains=query)  # <-- "tags__name__icontains"
    ).distinct()
    return render(request, 'blog/search_results.html', {
        'query': query,
        'results': results,
    })