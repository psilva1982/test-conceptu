# Generated by Django 3.2.5 on 2021-07-16 20:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acervo', '0002_load_categories_and_users'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('name', 'author', 'user')},
        ),
    ]
