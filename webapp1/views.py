from .models import Book
from django.shortcuts import render

def index(request, template='index.html', page_template='new_index.html'):
    context = {
        'entry_list': Book.objects.all(),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)


