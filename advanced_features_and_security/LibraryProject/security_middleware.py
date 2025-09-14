# LibraryProject/security_middleware.py
class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Example policy — restrict sources; adjust to your resources
        self.policy = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;"

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", self.policy)
        return response
