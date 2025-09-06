from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Book
from .models import Library  
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("list_books")  # redirect after registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # log in the new user
        return redirect(self.success_url)

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
