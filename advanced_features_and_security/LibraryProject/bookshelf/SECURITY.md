# Security Hardening

## Settings
- DEBUG must be False in production.
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE set True in production.
- SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF and X_FRAME_OPTIONS set.

## CSRF
All POST forms include `{% csrf_token %}`. Verify templates in `bookshelf/templates/`.

## SQL injection
All DB access uses Django ORM or parameterized raw SQL. See `bookshelf/views.py` and `bookshelf/forms.py`.

## CSP
Simple CSP added in `LibraryProject/security_middleware.py`.

## How to test locally
- Use DEBUG True for local dev, but test with DEBUG False in a staging environment that has HTTPS.
