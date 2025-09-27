from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('Hello. Evsu!')

def home(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def about_view(request):
    context = {
        'name': 'Jane Doe',
        'student_id': '12345678'
    }
    return render(request, 'about.html', context)
