# Generated by Django 3.2 on 2022-05-30 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0009_alter_provinceresidence_residency'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceNonEligibleContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='Non Eligible Content')),
                ('effective_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Effective Start Date')),
                ('effective_end_date', models.DateField(default='2099-12-31', verbose_name='Effective End Date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]