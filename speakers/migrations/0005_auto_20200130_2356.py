# Generated by Django 2.2.5 on 2020-01-30 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20200130_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='company',
            field=models.CharField(help_text='Name of Organization speaker is from. eg. Google', max_length=200),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='linkedin',
            field=models.CharField(help_text="Please enter only the user name eg.'/in/mawy7' ", max_length=100),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='position',
            field=models.CharField(help_text='Position of the speaker eg. CEO', max_length=200),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='twitter',
            field=models.CharField(help_text="Please enter only the user name eg.'mawy_7' ", max_length=100),
        ),
    ]
