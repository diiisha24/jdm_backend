# Generated by Django 5.2.1 on 2025-05-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_achievement_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
