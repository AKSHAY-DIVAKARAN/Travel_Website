# Generated by Django 4.1.3 on 2022-12-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_desc_team_desc_rename_img_team_img_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='imG',
            new_name='imge',
        ),
    ]