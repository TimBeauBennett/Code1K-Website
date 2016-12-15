from django.shortcuts import render

def index(request):
    return render(request, 'Chapter8/chap8_content.html')
