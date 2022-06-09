# Generated by Django 3.2 on 2022-06-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0019_auto_20220601_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCreditProduct1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('modified_by', models.CharField(max_length=200, null=True)),
                ('credit_product_code', models.CharField(help_text='Credit Product Code', max_length=100, unique=True, verbose_name='Credit Product Code')),
                ('credit_product_name', models.CharField(help_text='Credit Product Name', max_length=200, verbose_name='Credit Product Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='InsuranceCreditProduct',
        ),
    ]