from django.shortcuts import render

def index(request):
    return render(request, 'resources/resources_content.html')
