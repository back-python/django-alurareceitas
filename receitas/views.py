from django.shortcuts import render

# Create your views here.
def index(request):
    receitas = {
        1: 'Bolo de Chocolate',
        2: 'Bolo de limão',
        3: 'Suco detox',
        4: 'Pudim'
    }

    dados = {
        'nome_das_receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')