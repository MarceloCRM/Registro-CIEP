from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Registros
from .forms import RegistrosForm, SearchForm

def list_registro(request):
    registro = Registros.objects.all()
    template_name = 'list_registros.html'
    context = {
        'registros': registro
    }
    return render(request, template_name, context)

@login_required
def new_registro(request):
    if request.method == "POST":
        form = RegistrosForm(request.POST)
        print(form.is_valid)
        if form.is_valid():
            form.save()
            return redirect('registro:list_registro')
    else:
        return render(request, template_name="new_registro.html", context={"form": RegistrosForm()})


@login_required
def update_registro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    if request.method == "POST":
        form = RegistrosForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect("registro:list_registro")
    else:
        return render(request, template_name="update_registro.html", context={"form": RegistrosForm(instance=registro), "pk": pk})
    
@login_required
def delete_registro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    registro.delete()
    return redirect('registro:list_registro')

def pesquisa(request):
    form = SearchForm()
    results = Registros.objects.all()
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query: 
                results = Registros.objects.filter(nome__icontains=query)
            else:
                results = Registros.objects.all()
        else:
            results = Registros.objects.all()
    
    return render(request, 'list_registros.html', {'form': form, 'results': results})