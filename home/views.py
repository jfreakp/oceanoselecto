from django.shortcuts import render


from django.shortcuts import redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('marketplace:home')
    context = {"title": "Inicio"}
    return render(request, "home/index.html", context)
