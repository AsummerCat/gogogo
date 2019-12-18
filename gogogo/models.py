# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    money = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account'

class Test1(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'test_1'
