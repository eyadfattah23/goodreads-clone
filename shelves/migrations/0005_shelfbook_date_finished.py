# Generated by Django 5.1.4 on 2024-12-30 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0004_shelfbook_date_added_shelfbook_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelfbook',
            name='date_finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]