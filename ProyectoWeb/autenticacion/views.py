from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    def get(self, request): #es el que muestra el formulario
        form=UserCreationForm()
        return render(request, 'registro/registro.html', {'form':form})
        

    def post(self, request): #para crear el usuario
        form=UserCreationForm(request.POST)

        if form.is_valid():
            usuario=form.save()#con esta instruccion se almacena el usuario en la base de datos
            login(request, usuario) #se crea el login
            return redirect('Home') #redirecciona a login
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg]) #con esto logramos que si no se crea bien el usuario, le tira el error que esta ocurriendo.
            return render(request, 'registro/registro.html', {'form':form})



def cerrar_sesion(request): #para cerrar sesion
    logout(request)
    return redirect('Home')


def loguear(request): #para loguearse cuando ya tengo un usuario
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario o contraseña no válido")
        else:
            messages.error(request, "El usuario y/o contraseña ingresado no son válidos")

    form=AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})