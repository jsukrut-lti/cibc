# Generated by Django 3.2 on 2022-06-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0015_auto_20220601_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuranceproduct',
            name='creditProduct_code',
        ),
        migrations.DeleteModel(
            name='InsuranceCreditProduct',
        ),
    ]
