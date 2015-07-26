from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'hafa/index.html', {})

def about(request):
    return render(request, 'hafa/about.html', {})

def mission(request):
    return render(request, 'hafa/index.html', {})

def services(request):
    return render(request, 'hafa/index.html', {})

def blog(request):
    return render(request, 'hafa/blog.html', {})

def contact(request):
    return render(request, 'hafa/contact.html', {})

def whatwedo(request):
    return render(request, 'hafa/whatwedo.html', {})

def howwework(request):
    return render(request, 'hafa/howwework.html', {})

def wherewework(request):
    return render(request, 'hafa/wherewework.html', {})

def getinvolved(request):
    return render(request, 'hafa/getinvolved.html', {})
