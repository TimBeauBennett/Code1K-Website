from django.shortcuts import render

def index(request):
    return render(request, 'Chapter6/chap6_content.html')
