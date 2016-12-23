from django.db import models
from django.db.models import permalink

class Book(models.Model):
    title = models.CharField(max_length=140, unique=True)
    author =  models.CharField(max_length=140, unique=True)
    link = models.CharField(max_length=100000000, unique=True)
    preview = models.TextField()

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_chapter_name', None, { 'title': self.title })

class Chapter_Notes(models.Model):
    book_name = models.ForeignKey('books.Book')
    notes = models.TextField()

    def __str__(self):
        return '%s' % self.book_name

    @permalink
    def get_absolute_url(self):
        return ('view_book_name', None, { 'book_name': self.book_name})
