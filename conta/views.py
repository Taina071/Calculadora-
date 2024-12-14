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
            raio = float(request.POST.get('raio'))
            # Calcula a área (A = π * r²)
            area = 3.1416 * (raio ** 2)

            # Salvar o resultado no banco de dados
            Cal = Calculo(
                resultado=area
            )
            Cal.save()

            # Exibe o resultado na página calcular-area.html
            return render(request, 'calcular-area.html', {'raio': raio, 'area': area})
        except ValueError:
            return HttpResponse("Erro: insira um número válido.", status=400)
    return HttpResponse("Método não permitido.", status=405)

# Página sobre o autor
def autor(request):
    return render(request, 'autor.html')