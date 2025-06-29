# Generated by Django 5.2.1 on 2025-05-19 05:25

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_achievement_prefix_alter_achievement_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='icon',
            field=models.FileField(upload_to='achievements/', validators=[core.models.validate_svg]),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='prefix',
            field=models.CharField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='suffix',
            field=models.CharField(blank=True, default='', null=True),
        ),
    ]
