from django.shortcuts import render

from .models import TradeData

def home(request):
    data = TradeData.objects.all()
    return render(request, 'home.html', {'data': data})