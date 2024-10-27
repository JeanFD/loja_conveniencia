from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Produto
# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        print(produtos)
        return (render(request, 'index.html', {'produtos': produtos}))