from django.shortcuts import render

def index(request):
    return render(request, 'Chapter7/chap7_content.html')
