from django.shortcuts import render

from phones.models import Phone
from .forms import PhonesFilterForm


def show_catalog(request):
    template = 'catalog.html'
    #paramet = request.GET.get('sort', None)
    phones = Phone.objects.all()

    form = PhonesFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['ordering']:
            phones = phones.order_by(form.cleaned_data['ordering'])

    context = {'phone': phones, 'form': form}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=str(slug))}
    return render(request, template, context)
