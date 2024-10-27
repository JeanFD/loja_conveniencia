from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Produto
# Create your views here.

def index(request):
        produtos = Produto.objects.all()
        print(produtos)
        return (render(request, 'index.html', {'produtos': produtos}))
    
def produto(request, pk):
    prod = {
        'produto': Produto.objects.get(id=pk)
    }
    return render(request, 'produto.html', prod)