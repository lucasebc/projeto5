from django.shortcuts import render
from projeto5_website.models import Pergunta

from django.http import HttpResponse, HttpResponseRedirect
from projeto5_website.forms import PerguntaForm


# Create your views here.


def home(request):
  return render(request, "projeto5_website/home.html", 
        {"perguntas": Pergunta.objects.all()})

def pergunta_form(request):
  if request.method == "POST":
    form = PerguntaForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/') #Lembrar de importar
  else:
    form = PerguntaForm()
  return render(request, "projeto5_website/pergunta_form.html", {'form': form})
  