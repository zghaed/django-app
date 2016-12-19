from django.shortcuts import render
# from django.http import HttpResponse
from django.http import Http404

from firstapp.models import Item

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'index.html', {
        'items': items,
    })
    # return HttpResponse('<p>This is the index page</p>')

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except item.DoesNotExist:
        raise Http404('Item does not exist')

    return render(request, 'item_detail.html', {
        'item': item,
    })
    # return HttpResponse('<p>id is {0}</p>'.format(id))
