from django.shortcuts import render

def index(request):
    return render(request, template_name='index.html', context={"apenas um teste": "teste"})