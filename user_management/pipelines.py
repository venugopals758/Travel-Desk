from social_core.exceptions import AuthForbidden
from django.http import HttpResponse
from user_management.models import User

def check_user(backend, details, response, *args, **kwargs):
    
    email = details.get('email')
    if not User.objects.filter(email=email).exists():
        return HttpResponse("User not allowed to login")
    