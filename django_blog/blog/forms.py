from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="Your Comment",
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Write your comment here..."
        }),
        max_length=500,
        help_text="Maximum 500 characters."
    )

    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or content.strip() == "":
            raise forms.ValidationError("Comment cannot be empty.")
        return content


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')


class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data.get("email")
    if commit:
        user.save()
    return user


class ProfileForm(forms.ModelForm):
    class Meta:
        from .models import Profile
        model = Profile
        fields = ("bio", "avatar")
        widgets = {
        'bio': forms.Textarea(attrs={'rows':3}),
        }