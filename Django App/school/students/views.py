from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request, 'index.html')
    
