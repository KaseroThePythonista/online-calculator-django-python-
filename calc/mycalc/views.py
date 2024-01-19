from django.shortcuts import render

# Create your views here.

def calculator(request):

    context = {}


    return render(request, 'mycalc/calculator.html', context)

