from django.shortcuts import render


# Create your views here.
def search(request):
    """Search view."""
    return render(request, 'shop/search.html')