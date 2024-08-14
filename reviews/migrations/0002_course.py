# Generated by Django 5.0.7 on 2024-08-14 04:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='reviews.university')),
            ],
        ),
    ]
