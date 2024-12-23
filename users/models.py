#!/usr/bin/python3
"""User related models."""
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from books.models import Book
import os
# Create your models here.


def user_image_upload_to(instance, filename):
    """Generate file path for user profile pictures."""
    ext = filename.split('.')[-1]  # Get the file extension
    return os.path.join(f"profile_pictures/{instance.username}/profile.{ext}")


class CustomUserManager(BaseUserManager):
    """Custom user manager to handle email as username."""

    def create_user(self, email, password=None, **extra_fields):
        """#+
        Create and save a new user with the given email and password.#+
#+
        Args:#+
            email (str): The email address for the new user. This is required.#+
            password (str, optional): The password for the new user. If not provided, the user will have no password.#+
            **extra_fields: Additional fields to be set on the new user model.#+
#+
        Raises:#+
            ValueError: If the email is not provided.#+
#+
        Returns:#+
            CustomUser: The newly created user instance.#+
        """  # +
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """#+
        Create and save a new superuser with the given email and password.#+
#+
        Args:#+
            email (str): The email address for the new superuser. This is required.#+
            password (str, optional): The password for the new superuser. If not provided, the superuser will have no password.#+
            **extra_fields: Additional fields to be set on the new superuser model.#+
#+
        Raises:#+
            ValueError: If is_staff or is_superuser is set to False.#+
#+
        Returns:#+
            CustomUser: The newly created superuser instance.#+
        """  # +
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """User profile model"""
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(
        upload_to=user_image_upload_to, default='default_user_image.png')

    def __str__(self):
        return "{} | id:{}".format(self.username, self.id)

    def save(self, *args, **kwargs):
        # Save once to generate an ID for the instance
        if not self.id:
            super().save(*args, **kwargs)

        # Update the file path using the ID and save again if the file path needs an ID
        if self.image and f'profile_pictures/{self.username}' not in self.image.name:
            self.image.name = user_image_upload_to(self, self.image.name)
            super().save(*args, **kwargs)


class Favorite(models.Model):
    """Model to represent a user's favorite books."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        # Prevent duplicate books in the same shelf
        unique_together = ('user', 'book')
        indexes = [
            models.Index(fields=['user', 'book']),
        ]

    def __str__(self):
        return f"{self.book.title} is a favorite of {self.user.username}"


class BookReview(models.Model):
    """Model to represent a user's book review."""

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate books in the same shelf
        unique_together = ('user', 'book')
        indexes = [
            models.Index(fields=['user', 'book']),
        ]

    def __str__(self):
        return f"{self.user.username} reviewed {self.book.title} at {self.created_at}"
