from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from re import match
class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code that is executed in each request before the view is called
        if match("/users/login", request.path):
            from .views import get_token
            response = get_token(request)
            return JsonResponse(response[0], status=response[1])
        if not request.headers.get("Token"):
            return JsonResponse({"response": "Token Is Missing"}, status=403)
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        return response