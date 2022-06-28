# Generated by Django 3.2 on 2022-06-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0003_exitsurveymaster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exitsurveymaster',
            name='exit_msg',
        ),
        migrations.AddField(
            model_name='exitsurveymaster',
            name='exit_msg_line0',
            field=models.CharField(blank=True, help_text='Exit Message0', max_length=500, verbose_name='Exit Msg0'),
        ),
        migrations.AddField(
            model_name='exitsurveymaster',
            name='exit_msg_line1',
            field=models.CharField(blank=True, help_text='Exit Message1', max_length=500, verbose_name='Exit Msg1'),
        ),
        migrations.AddField(
            model_name='exitsurveymaster',
            name='exit_msg_line2',
            field=models.CharField(blank=True, help_text='Exit Message2', max_length=500, verbose_name='Exit Msg2'),
        ),
    ]