# Generated by Django 5.1.1 on 2024-09-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apileague', '0003_alter_skill_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='e_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='passive_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='q_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='r_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='w_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
