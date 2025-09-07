from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Book
from .models import Library  
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# Helper functions to check roles
def role_check(role):
    def check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return check

@user_passes_test(role_check('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(role_check('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


class Register(CreateView):
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

# --- Add Book ---
@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author_id")
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect("list_books")  # assumes list_books exists
    return render(request, "relationship_app/add_book.html")


# --- Edit Book ---
@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        author_id = request.POST.get("author_id")
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect("list_books")
    return render(request, "relationship_app/edit_book.html", {"book": book})


# --- Delete Book ---
@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
