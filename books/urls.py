from django.urls import path, include
from . import views


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetails.as_view(), name='book-details'),

    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetails.as_view(), name='author-details'),

    path('genres/', views.GenreList.as_view()),
    path('genres/<int:pk>', views.GenreDetails.as_view(), name='genre-details'),
]
