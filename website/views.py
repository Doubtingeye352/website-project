from django.shortcuts import render
from joke.jokes import *
import random

def home(requests):
    return render(requests, 'index.html')

def final(requests):
    var = random.choice([icanhazdad(),geek(),icndb()])

    return render(requests, 'final.html',{'jok': var})
