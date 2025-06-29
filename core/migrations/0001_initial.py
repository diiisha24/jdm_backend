# Generated by Django 5.2.1 on 2025-05-12 16:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hero_video', models.FileField(blank=True, null=True, upload_to='videos/hero/')),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='hero/')),
                ('services_heading', models.CharField(default='Our Services', max_length=200)),
                ('journey_heading', models.CharField(default='Our Journey', max_length=200)),
                ('journey_video', models.FileField(blank=True, null=True, upload_to='videos/journey/')),
                ('clientele_heading', models.CharField(default='Our Clientele', max_length=200)),
                ('associations_heading', models.CharField(default='Associations', max_length=200)),
                ('affiliations_heading', models.CharField(default='Affiliations & Accreditation', max_length=200)),
                ('sea_partners_heading', models.CharField(default='Sea Carrier Partners', max_length=200)),
                ('air_partners_heading', models.CharField(default='Air Carrier Partners', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteleItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='clients/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientele', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='blogs/')),
                ('home', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='AssociationItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='associations/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associations', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='AirPartnerItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='carriers/air/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='air_partners', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='AffiliationItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='affiliations/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affiliations', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('icon', models.CharField(max_length=100)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.JSONField(default=list)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='locations/')),
                ('place', models.CharField(max_length=200)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='SeaPartnerItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='carriers/sea/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sea_partners', to='core.homepagecontent')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='services/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='core.homepagecontent')),
            ],
        ),
    ]
