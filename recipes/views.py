from django.shortcuts import render

# Create your views here.

# HTTP REQUEST


def home(request):
    # RETURN HTTP RESPONSE
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Jaqueline Alves',

    })
