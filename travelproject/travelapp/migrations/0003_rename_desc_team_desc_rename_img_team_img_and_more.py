# Generated by Django 4.1.3 on 2022-12-16 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='desC',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='imG',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='namE',
        ),
    ]
