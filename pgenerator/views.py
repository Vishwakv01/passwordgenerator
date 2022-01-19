from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'pgenerator/about.html')


def input(request):
    return render(request, 'pgenerator/index.html')


def pgen(request):
    charset = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('passwordLength'))
    if request.GET.get('uppercase'):
        charset.extend([char.upper() for char in charset])
    if request.GET.get('number'):
        charset.extend([str(i) for i in range(10)])
    if request.GET.get('specialchar'):
        charset.extend(list('!@#$%^&'))
    password = ''
    for i in range(length):
        password += random.choice(charset)
    return render(request, 'pgenerator/pgen.html', {'passwordkey':password})