from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.

def get_all(request):
    first = Zhanr.objects.all()
    second = Kino.objects.all()
    return render(request, 'home.html', context={'first': first, 'second': second})
        
        
def kino_list(request):
    kinos = Kino.objects.all().order_by('-id')
    return render(request, 'kino_list.html', context={'kinos': kinos})


def create_kino(request):
    if request.method == 'POST':
        Kino.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            image=request.FILES.get('image')
        )
        return redirect('kino_list')
    return render(request, 'kino_form.html')


def update_kino(request, pk):
    kino = get_object_or_404(Kino, id=pk)
    if request.method == 'POST':
        kino.name = request.POST.get('name')
        kino.price = request.POST.get('price')
        if request.FILES.get('image'):
            kino.image = request.FILES.get('image')
        kino.save()
        return redirect('kino_list')
    return render(request, 'kino_form.html', context={'kino': kino})


def delete_kino(request, pk):
    kino = get_object_or_404(Kino, id=pk)
    if request.method == 'POST':
        kino.delete()
        return redirect('kino_list')
    return render(request, 'kino_delete.html', context={'kino': kino})


def fidbek(request):
    if request.method == 'POST':
        Fidbek.objects.create(otziv=request.POST.get('otziv'))
        return redirect('fidbek')
    otzivs = Fidbek.objects.all().order_by('-id')
    return render(request, 'fidbek.html', context={'otzivs': otzivs})
