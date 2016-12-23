from books.models import Book, Chapter_Notes
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'books': Books.objects.all(),
        'posts': Chapter_Notes.objects.all(),
    })

def view_post(request, slug):
