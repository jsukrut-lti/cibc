# Generated by Django 3.2 on 2022-05-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0013_remove_insurancecreditproduct_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecreditproduct',
            name='credit_product_name',
            field=models.CharField(help_text='Credit Product Name', max_length=200, verbose_name='Credit Product Name'),
        ),
    ]