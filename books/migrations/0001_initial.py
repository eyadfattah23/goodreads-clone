# Generated by Django 5.1.4 on 2024-12-19 19:57

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(default='default_author.png', upload_to='authors_pics/')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='books_autho_name_5aec2d_idx')],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='books_genre_name_27aecb_idx')],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('buy_link', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('pages', models.PositiveIntegerField()),
                ('publication_date', models.DateField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(default='default_book.png', upload_to='covers/')),
                ('avg_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('5.00'))])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.author')),
                ('genres', models.ManyToManyField(to='books.genre')),
            ],
            options={
                'ordering': ['-added_date'],
                'indexes': [models.Index(fields=['title'], name='books_book_title_d3218d_idx'), models.Index(fields=['author'], name='books_book_author__709385_idx')],
            },
        ),
    ]