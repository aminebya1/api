from django.db import models
from .users import User


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'roles'


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_roles'
