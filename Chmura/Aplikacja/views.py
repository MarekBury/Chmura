from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import ZamowienieForm, StworzUseraForm
from django.contrib.auth.decorators import login_required

def rejestracja(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = StworzUseraForm()

        if request.method == "POST":
            form = StworzUseraForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto' + user +' zostało stworzone')

                return redirect('logowanie')

        context={'form':form}
        return render(request, 'Aplikacja/rejestracja.html',context)

@csrf_protect
def logowanie(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password =password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło jest niepoprawne!')
                return render(request, 'Aplikacja/logowanie.html')

    context={}
    return render(request, 'Aplikacja/logowanie.html',context)

def wylogowanie(request):
    logout(request)
    return redirect('logowanie')

@login_required(login_url='logowanie')
def home(request):
    zamowienia = Zamowienie.objects.all()
    klient = Users.objects.all()

    ilosc_klientow = klient.count()

    ilosc_zamowien = zamowienia.count()
    dostarczono = zamowienia.filter(status='Dostarczono').count()
    wyslano = zamowienia.filter(status='W doręczeniu').count()

    context = {'zamowienia':zamowienia, 'klient': klient,'ilosc_zamowien':ilosc_zamowien, 'dostarczono':dostarczono,'wyslano':wyslano}

    return render(request, 'Aplikacja/dashboard.html', context)

@login_required(login_url='logowanie')
def produkty(request):
    produkty = Produkt.objects.all()

    return render(request, 'Aplikacja/produkty.html',{'produkty': produkty})

@login_required(login_url='logowanie')
def produkt(request,pk):
    produkt = Produkt.objects.get(id=pk)

    context = {'produkt':produkt}
    return render(request, 'Aplikacja/produkt.html', context)

@login_required(login_url='logowanie')
def klient(request,pk_test):
    klient= Users.objects.get(id=pk_test)

    zamowienia = klient.zamowienie_set.all()
    zamowienia_ilosc= zamowienia.count()
    context = {'klient':klient,'zamowienia':zamowienia, 'zamowienia_ilosc':zamowienia_ilosc}

    return render(request, 'Aplikacja/klient.html',context)

@login_required(login_url='logowanie')
def createOrder(request):
    form = ZamowienieForm
    if request.method == 'POST':
        form = ZamowienieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'Aplikacja/order_form.html', context)

@login_required(login_url='logowanie')
def aktualizujZamowienie(request,pk):
  
    zamowienie = Zamowienie.objects.get(id=pk)
    form = ZamowienieForm(instance =zamowienie)
    if request.method == 'POST':
        form = ZamowienieForm(request.POST, instance=zamowienie)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'Aplikacja/order_form.html', context)

@login_required(login_url='logowanie')
def usunZamowienie(request,pk):
    zamowienie = Zamowienie.objects.get(id=pk)
    if request.method == "POST":
        zamowienie.delete()
        return redirect('/')

    context = {'item': zamowienie}
    return render(request, 'Aplikacja/usun.html', context)