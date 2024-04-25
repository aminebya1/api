from django.contrib.auth.hashers import make_password
from ..models import User


def find_by_email(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def email_exists(email):
    return User.objects.filter(email=email).exists()


def create_user(data):
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password_hash=make_password(data['password'])

    )
    return user
