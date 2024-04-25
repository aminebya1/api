from django.db import models

class Pokemon(models.Model):
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    class Meta:
        db_table = 'pokemon'
        managed = False  # vu que la base données du prof contient déjà cette table


