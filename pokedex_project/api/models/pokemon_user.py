from django.db import models
from .users import User
from .pokemon import Pokemon


class PokemonUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='owners')
    date_caught = models.DateTimeField()

    class Meta:
        db_table = 'pokemon_user'
