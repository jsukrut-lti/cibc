# Generated by Django 3.2 on 2022-06-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0015_assessmentquestionnairemaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurancePreProcessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('application_number', models.CharField(help_text='Application Number', max_length=100, verbose_name='Application Number')),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('active', 'ACTIVE'), ('deactivate', 'DEACTIVATE')], default='draft', max_length=10)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='dumpData',
        ),
    ]
