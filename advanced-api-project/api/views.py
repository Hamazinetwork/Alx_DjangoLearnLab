from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from models import Book, Author
from serializers import AuthorSerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework


class AuthorListView(generics.ListAPIView):
    queryset=Author.objects.all()
    Author_serializer=AuthorSerializer
    permission_classes=[permissions.AllowAny]

class AuthorDetailView(generics.RetrieveAPIView):
    queryset=Author.objects.all()
    Author_serializer=AuthorSerializer
    permission_classes=[permissions.AllowAny]

class AuthorCreateView(generics.CreateAPIView):
    queryset=Author.objects.all()
    Author_serializer=AuthorSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class AuthorUpdateView(generics.UpdateAPIView):
    queryset=Author.objects.all()
    Author_serializer=AuthorSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class AuthorDeleteView(generics.DestroyAPIView):
    queryset=Author.objects.all()
    Author_serializer=AuthorSerializer
    permission_classes=[permissions.IsAuthenticated]


#Book CRUD
class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    Author_serializer=BookSerializer
    permission_classes=[permissions.AllowAny]
    filter_backends=[DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    Order_field=['title', 'publication_year']
    Search_field=['title', 'author__name']
    filterset_fields = ['title', 'author', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    Author_serializer=BookSerializer
    permission_classes=[permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    Author_serializer=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    Author_serializer=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    Author_serializer=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

    #DOCUMENTATION
# BookListView: Anyone can see all books (GET /books/)
# BookDetailView: Anyone can see a single book by ID (GET /books/<id>/)
# BookCreateView: Only authenticated users can create (POST /books/create/)
# BookUpdateView: Only authenticated users can update (PUT /books/<id>/update/)
# BookDeleteView: Only authenticated users can delete (DELETE /books/<id>/delete/)
