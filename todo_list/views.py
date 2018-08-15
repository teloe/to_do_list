from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item added!'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'first_name': 'Tom', 'last_name': 'Eloe'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item removed.'))
    return redirect('home')
