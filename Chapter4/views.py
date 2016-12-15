from django.shortcuts import render

def index(request):
    return render(request, 'Learning_Python/Learning_Python_content.html')
