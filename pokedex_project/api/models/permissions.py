from django.db import models
from .roles import Role


class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'permissions'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'role_permissions'
