# Generated by Django 5.0.7 on 2024-08-14 05:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_course_course_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('study_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='reviews.university')),
            ],
        ),
    ]
