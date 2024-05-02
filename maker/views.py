# views.py
from django.shortcuts import render, HttpResponse
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse("Yay! you are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
