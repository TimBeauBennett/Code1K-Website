from django.shortcuts import render

def index(request):
    return render(request, 'Chapter5/chap5_content.html')
