from .models import Role, Permission

# Création de rôles
admin_role = Role.objects.create(name='admin')
member_role = Role.objects.create(name='membre')

# Création de permissions
create_pokemon = Permission.objects.create(name='create_pokemon')
read_pokemon = Permission.objects.create(name='read_pokemon')
update_pokemon = Permission.objects.create(name='update_pokemon')
delete_pokemon = Permission.objects.create(name='delete_pokemon')

# CRU pour les utilisateurs (l'admin a toutes les permissions)
create_user = Permission.objects.create(name='create_user')
read_user = Permission.objects.create(name='read_user')
update_user = Permission.objects.create(name='update_user')
delete_user = Permission.objects.create(name='delete_user')
# Register your models here.
