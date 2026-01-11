from django.shortcuts import render


def index(request):
    context = {"title": "Inicio"}
    return render(request, "home/index.html", context)
