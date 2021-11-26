from django.shortcuts import render

def Inicio (request):
    return render(request,'index.html')

def papa (request):
    return render(request,'d.html')

