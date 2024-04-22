from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    region_id = models.IntegerField(null=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        db_table = 'locations'

class Move(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(null=True)
    pp = models.SmallIntegerField(null=True)
    accuracy = models.SmallIntegerField(null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(null=True)
    contest_type_id = models.IntegerField(null=True)
    contest_effect_id = models.IntegerField(null=True)
    super_contest_effect_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'moves'

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    class Meta:
        db_table = 'pokemon'

class PokemonEggGroup(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

    class Meta:
        db_table = 'pokemon_egg_groups'

class PokemonFormGeneration(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        db_table = 'pokemon_form_generations'

class PokemonMove(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(null=True)

    class Meta:
        db_table = 'pokemon_moves'

class PokemonStat(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        db_table = 'pokemon_stats'
