from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate #isso serve para o proprio django ir no bd pegar as info e confirmar#
from django.contrib.auth import login as login_django #so faz liberação das autenticação, não consulta o bd#

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login_django(request, user)
            return HttpResponse('Autenticado!')
        else:
            return HttpResponse('E-mail ou senha invalidos!')
