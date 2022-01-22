from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
# DIRECTORIO INICIAL HOME
def home(request):
    return render(request,'basic_app/home.html')

# PRUEBA
@login_required
def special(request):
    return HttpResponse("you are logged in, nice!")

# LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# REGISTRO
def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.error,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

# LOGIN
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request,'basic_app/login.html',{})

# SOPORTE AL CLIENTE
def support(request):
    return render(request,'basic_app/soporte.html')

# CARRITO
def carrito(request):
    return render(request,'basic_app/carrito.html')

# ORDENADORES
def ordenadores(request):
    return render(request,'basic_app/ordenadores.html')

def ordenadores_sobremesa(request):
    return render(request,'basic_app/ordenadores_sobremesa.html')

def ordenadores_portatiles(request):
    return render(request,'basic_app/ordenadores_portatiles.html')

# CONSOLAS
def consolas(request):
    return render(request,'basic_app/consolas.html')

def consolas_xbox(request):
    return render(request,'basic_app/consolas_xbox.html')

def consolas_playstation(request):
    return render(request,'basic_app/consolas_playstation.html')

def consolas_nintendo(request):
    return render(request,'basic_app/consolas_nintendo.html')

# PERIFÉRICOS
def perifericos(request):
    return render(request,'basic_app/perifericos.html')

def perifericos_teclados(request):
    return render(request,'basic_app/perifericos_teclados.html')

def perifericos_ratones(request):
    return render(request,'basic_app/perifericos_ratones.html')

def perifericos_cascos(request):
    return render(request,'basic_app/perifericos_cascos.html')

# IMPRESORAS
def impresoras(request):
    return render(request,'basic_app/impresoras.html')

def impresoras_tinta(request):
    return render(request,'basic_app/impresoras_tinta.html')

def impresoras_laser(request):
    return render(request,'basic_app/impresoras_laser.html')

def impresoras_matriciales(request):
    return render(request,'basic_app/impresoras_matriciales.html')

# VIDEOJUEGOS
def videojuegos(request):
    return render(request,'basic_app/videojuegos.html')

def videojuegos_xbox(request):
    return render(request,'basic_app/videojuegos_xbox.html')

def videojuegos_playstation(request):
    return render(request,'basic_app/videojuegos_playstation.html')

def videojuegos_ordenador(request):
    return render(request,'basic_app/videojuegos_ordenador.html')

def videojuegos_nintendo(request):
    return render(request,'basic_app/videojuegos_nintendo.html')
