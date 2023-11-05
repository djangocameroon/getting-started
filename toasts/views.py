from django.shortcuts import render
from django.http import HttpResponse
from .forms import ToastForm


def index(request):
    return HttpResponse("Hello, world. You're at the toasts index.")

def submit_toast_form(request):
    if request.method == 'POST':
        form = ToastForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Hurray!!! Your form was submitted successfully</h1>")
    else:
        form = ToastForm()

        context = {
            'form': form
        }
    
    return render(request, 'toaster_form.html', context)
