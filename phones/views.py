from django.http import HttpResponse
from django.shortcuts import render

from phones.management.commands.import_phones import Command

b = Command()


def show_catalog(request):
    #template = 'catalog.html'
    #context = {}
    a = b.handle()
    return HttpResponse(a)
    #return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
