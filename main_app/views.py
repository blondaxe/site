from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SolutionForm
from .forms import ProblemeForm
from .models import Probleme
from .models import Solution





def home(request):
    return render(request, 'main_app/home.html')


def ajouter_solutions(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger l'utilisateur vers une page de confirmation
            return redirect('../')
    else:
        form = SolutionForm()
    return render(request, 'main_app/ajouter_solutions.html', {'form': form})



def ajouter_problemes(request):
    if request.method == 'POST':
        form = ProblemeForm(request.POST)
        if form.is_valid():
            probleme = Probleme.objects.create(nom=form.cleaned_data['nom'])
            # Faire quelque chose avec le nom
            return redirect('../')

    else:
        form = ProblemeForm()
    return render(request, 'main_app/ajouter_problemes.html', {'form': form})

def voir_problemes(request):
    problemes = Probleme.objects.all().order_by("nom")
    return render(request, 'main_app/voir_problemes.html', {'problemes': problemes})


def detail_probleme(request, pk):
    probleme = Probleme.objects.get(pk=pk)
    solutions = Solution.objects.filter(probleme=probleme)
    context = {
        'probleme': probleme,
        'solutions': solutions
    }
    return render(request, 'main_app/detail_probleme.html', context)