from django.db import models


class Items(models.Model):
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True, blank=True)
    fling_effect_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'items'
