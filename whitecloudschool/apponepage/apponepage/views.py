from django.shortcuts import render, redirect
from .forms import ContactFormForm


def index(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactFormForm()
    return render(request, 'index.html')

