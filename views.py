from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def checkout(request):
    return render(request, "checkout.html")


def Thanks(request):
    return render(request, "ordersuccess.html")


def error(request):
    return render(request, "error.html")
