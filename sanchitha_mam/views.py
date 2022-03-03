from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'MAM/home.html')



def about(request):
    return render(request, 'MAM/about.html')


def mam(request):
    return render(request, 'MAM/mam.html')