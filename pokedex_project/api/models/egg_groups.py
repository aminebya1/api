from django.db import models


class EggGroup(models.Model):
    identifier = models.CharField(max_length=79)

    class Meta:
        db_table = 'egg_groups'
