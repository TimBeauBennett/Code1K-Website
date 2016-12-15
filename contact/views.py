from django.shortcuts import render

def index(request):
        return render(request, 'contact/contact_content.html')
