from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'proyectowebapp/home.html')



def tienda(request):
    return render(request, 'proyectowebapp/tienda.html')

def blog(request):
    return render(request, 'proyectowebapp/blog.html')

def contacto(request):
    return render(request, 'proyectowebapp/contacto.html')