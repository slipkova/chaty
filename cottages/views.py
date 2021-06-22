from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from cottages.models import Cottage


def index(request):
    #View function for home page of site.

    # Generate counts of some of the main objects
    num_cottages = Cottage.objects.all().count()
    cottages = Cottage.objects.all()

    context = {
        'num_cottages': num_cottages,
        'cottages': cottages
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'main.html', context=context)


def my_cottages(request):
    cottages = Cottage.objects.all()
    return render(request, 'my_cottages.html', context={})


def registration(request):
    return render(request, 'register.html', context={})


def cottage_detail(request):
    return render(request, 'cottage_detail.html', context={})
