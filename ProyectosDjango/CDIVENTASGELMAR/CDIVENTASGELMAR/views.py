from django.shortcuts import render

def inicio(request):
    
    titulo="inicio"
    nombre="tatiana"

    context = {
        'nombres':nombre,
        'titulo': titulo
    }

    return render (request,'inicio.html',context)

