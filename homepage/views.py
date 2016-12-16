from django.shortcuts import render

def index(request):
    return render(request, 'homepage/homepage_content.html')

def contact(request):
    return render(request, 'homepage/contact_content.html')

def books(request):
    return render(request, 'homepage/books_content.html')

def podcast(request):
    return render(request, 'homepage/podcast_content.html')

def resources(request):
    return render(request, 'homepage/resources_content.html')

def Learning_Python(request):
    return render(request, 'homepage/Learning_Python_content.html')
