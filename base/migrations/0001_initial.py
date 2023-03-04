# Generated by Django 4.1.7 on 2023-03-04 21:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SustainabilityScore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=10, unique=True)),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True)),
                ('vendor', models.IntegerField(choices=[(1, 'Kayak'), (2, 'Skyscanner')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sustainability_score', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='base.sustainabilityscore')),
            ],
        ),
    ]