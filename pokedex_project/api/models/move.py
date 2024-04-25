from django.db import models


class Move(models.Model):
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
        managed = False  # vu que la base données du prof contient déjà cette table
