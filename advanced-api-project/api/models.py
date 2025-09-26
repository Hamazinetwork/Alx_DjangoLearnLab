from django.db import models

class Author(models.Model):
    name= models.CharField

    def __str__(self):
        return f"{self.name} "
class Book(models.Model):
    title=models.CharField
    publication_year=models.IntegerField
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"



# Author -> Book = One-to-Many relationship
# Each Author can have multiple Books.
# In Book, the `author` ForeignKey establishes this relationship.
