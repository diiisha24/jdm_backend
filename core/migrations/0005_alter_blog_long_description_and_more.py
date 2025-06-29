# Generated by Django 5.2.1 on 2025-05-15 04:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_blog_home_blog_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='long_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.JSONField(default=list),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('cv', models.FileField(upload_to='resumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.job')),
            ],
        ),
    ]
