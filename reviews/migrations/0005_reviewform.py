# Generated by Django 5.0.7 on 2024-08-14 06:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.student')),
                ('study_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.university')),
            ],
        ),
    ]
