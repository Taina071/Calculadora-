from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculo

# Página inicial
def index(request):
    return render(request, 'index.html')

# Função para calcular área
def calcular_area(request):
    if request.method == 'POST':
        try:
            raio = float(request.POST.get('raio'))  # Obtém o raio do formulário
            area = 3.1416 * (raio ** 2)  # Calcula a área (A = π * r²)
            
            # Salva o cálculo no banco de dados
            calculo = Calculo(resultado=area)
            calculo.save()

            
            return render(request, 'calcular-area.html', {'raio': raio, 'area': area})
        except (ValueError, TypeError):
            # Retorna uma mensagem de erro se o input for inválido
            return render(request, 'calcular-area.html', {'erro': "Insira um número válido!"})
    return render(request, 'calcular-area.html')

# Página sobre o autor
def autor(request):
    contexto = {
        'nome': "Taina Oliveira Lima",
        'formacoes': ["tecnico em redes de computadores"],
        
    }
    return render(request, 'autor.html', contexto)