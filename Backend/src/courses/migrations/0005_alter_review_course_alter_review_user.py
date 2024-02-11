# Generated by Django 4.2.10 on 2024-02-11 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_course', to='courses.courses'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
