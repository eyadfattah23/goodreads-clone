# Generated by Django 5.1.4 on 2024-12-28 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_slug_alter_author_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['slug'], name='books_book_slug_ca552e_idx'),
        ),
    ]
