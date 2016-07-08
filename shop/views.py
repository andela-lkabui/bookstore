from django.shortcuts import render

from forms import BookForm
from models import Book


# Create your views here.
def search(request):
    """Search view."""
    if request.GET:
        form = BookForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name_field')
            books = Book.objects.filter(name__icontains=name)
            context = {
                'books_list': books
            }
            return render(request, 'shop/results.html', context)

    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'shop/search.html', context)