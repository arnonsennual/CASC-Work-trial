# Generated by Django 5.0.7 on 2024-08-14 07:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_reviewform_is_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(null=True)),
                ('star', models.FloatField()),
                ('is_show', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.course')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.university')),
            ],
        ),
    ]
