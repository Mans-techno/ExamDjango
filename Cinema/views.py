from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def get_all(request):
    first = Zhanr.objects.all()
    second = Kino.objects.all()
    return render(request, 'home.html', context={'first': first, 'second': second})
        
        
def create_kino(request):
    if request.method == 'POST':
        Kino.objects.create(
            name = request.POST.get('name'),
            time = request.POST.get('time'),
            price = request.POST.get('price'),
            image = request.FILES.get('image')
        )
        return redirect('show')
    return render(request, 'home.html')


def update_kino(request, pk):
    kino = Kino.objects.get(id=pk)
    if request.method == 'POST':
        kino.name = request.POST.get('name')
        
        kino.time = request.POST.get('time')
        kino.price = request.POST.get('price')
        kino.image = request.FILES.get('image')
        kino.save()
        return redirect('show')
    return render(request, 'home.html', context={'kino': kino})


def delete_kino(request, pk):
    kino = Kino.objects.get(id=pk)
    kino.delete()
    return redirect('show')


def fidbek(request):
    if request.method == 'POST':
        Fidbek.objects.create(otziv=request.POST.get('otziv'))
        return redirect('fidbek')
    otzivs = Fidbek.objects.all().order_by('-id')
    return render(request, 'fidbek.html', context={'otzivs': otzivs})
