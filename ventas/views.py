from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ventas(request):
	return render(request, 'ventas/ventas.html')