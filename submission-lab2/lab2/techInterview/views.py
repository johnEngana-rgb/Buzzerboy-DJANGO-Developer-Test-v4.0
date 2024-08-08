from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'about-us.html')

# Create similar views for other HTML pages
