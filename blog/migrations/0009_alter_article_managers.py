# Generated by Django 4.2.15 on 2024-12-13 21:54

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_is_published'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
