# Generated by Django 5.1.4 on 2025-01-01 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='book',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookReview',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]