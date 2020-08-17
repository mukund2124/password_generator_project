from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    randompassword = ''
    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()'))

    for i in range(length):
        randompassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': randompassword})
def aboutsite(request):
    return render(request,'generator/about_site.html')