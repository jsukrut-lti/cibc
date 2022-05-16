# Generated by Django 3.2 on 2022-05-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0008_insurancediscussion_sssavingsemergencyfund'),
    ]

    operations = [
        migrations.CreateModel(
            name='dumpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('active', 'ACTIVE'), ('deactivate', 'DEACTIVATE')], default='draft', max_length=10)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
