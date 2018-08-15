from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'first_name': 'Tom', 'last_name': 'Eloe'}
    return render(request, 'about.html', context)
