from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User
import random
# Create your views here.

def sorteado(request):    
    if request.POST:        
        escolhido = random.choice(User.objects.all())                                            
        
        print(escolhido)   
     
    return render(request, 'index.html')