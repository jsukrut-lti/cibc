# Generated by Django 3.2 on 2022-05-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20210519_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='objection',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Draft'), ('sap', 'Sent for Approval'), ('ap', 'Approved'), ('re', 'Rejected')], max_length=5, null=True, verbose_name='Status'),
        ),
    ]
