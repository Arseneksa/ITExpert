# Generated by Django 4.0.3 on 2024-03-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineDB', '0003_alter_wildlife_data_encounter_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patrol_cover_datasmart',
            old_name='forest_cover_rate',
            new_name='patrol_cover_rate',
        ),
        migrations.RenameField(
            model_name='patrol_cover_datasmart',
            old_name='forest_cover_rate_max',
            new_name='patrol_cover_rate_max',
        ),
        migrations.RenameField(
            model_name='patrol_cover_datasmart',
            old_name='forest_cover_rate_min',
            new_name='patrol_cover_rate_min',
        ),
    ]
