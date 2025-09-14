from django.core.exceptions import ValidationError
from django import forms
from .models import Book, Author

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['author','title','publication_year']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "publication_year")

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if "<script" in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title

def validate_image_size(image):
    limit_mb = 5
    if image.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Image too large (>{limit_mb}MB).")
