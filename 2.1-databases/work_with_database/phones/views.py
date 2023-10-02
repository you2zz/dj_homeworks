from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phones = request.GET.get('sort')
    phones_objects = Phone.objects.all()
    sort_dict = {
        'min_price': phones_objects.order_by('price'),
        'max_price': phones_objects.order_by('price').reverse(),
        'name': phones_objects.order_by('name')
    }
    phones_view = sort_dict[sort_phones]
    context = {'phones': phones_view}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
