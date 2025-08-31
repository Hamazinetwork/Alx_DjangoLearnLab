# Django Admin Setup for Book Model

## Registration
The Book model was registered in `bookshelf/admin.py` using `@admin.register(Book)`.

## Customizations
- **list_display**: Shows `title`, `author`, and `publication_year`.
- **list_filter**: Allows filtering by `author` and `publication_year`.
- **search_fields**: Enables search by `title` and `author`.

## Testing
1. Logged into `http://127.0.0.1:8000/admin/`.
2. Verified Books are listed under the Bookshelf app.
3. Added, searched, and filtered book entries successfully.
