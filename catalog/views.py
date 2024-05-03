from django.shortcuts import render

# Create your views here.
def catalog(request):
    print('hi')
    return render(request, 'catalog/catalog.html')
