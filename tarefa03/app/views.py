from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def usuarios(request):
    dados_usuario= [
        {"nome": "Michael Scott", "matricula": "12", "idade": 48, "cidade": "Scranton"},
        {"nome": "Tony Stark", "matricula": "9201", "idade": 50, "cidade": "California"},
        {"nome": "Steve Rogers", "matricula": "1298", "idade": 230, "cidade": "Brooklyn"},
        {"nome": "James Halpert", "matricula": "1267", "idade": 38, "cidade": "Scranton"},
        {"nome": "Dwight Schrute", "matricula": "1234", "idade": 42, "cidade": "Scranton"},
    ]

    context = {
        "usuarios" : dados_usuario,
    }
    
    return render(request, "app/usuarios.html", context)
