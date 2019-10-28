from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import messages
import random
# Create your views here.

def sorteado(request):    
    escolhido = None
    
    if request.POST:        
        #TODO
        #Criar recomendações
        
        users = User.objects.all().exclude(username=request.user)
        amigos = []
        usuario_requisicao = request.user.usuario_set.get()
        
        if request.user.usuario_set.first().amigo_secreto is None:

            for user in Usuario.objects.all():
                if user.amigo_secreto:
                    amigos.append(user.amigo_secreto)#pega todos amigos selecionados
            
            print('amigos %s' %amigos)
            print('todos %s' %users)
            for amigo in amigos:
                users = users.exclude(username=amigo)
            print('Lista de quem sobrou: %s' % users)
            try:
                #print(users)
                escolhido = random.choice(users)
                print(type(escolhido))
            except IndexError: 
                messages.error(request, 'Não existe nenhum amigo que possa sortear no momento.')
            finally:
                    user = Usuario.objects.get(user=request.user)
                    user.amigo_secreto = escolhido
                    print(user.amigo_secreto)
                    user.save()
                    print('gravou') 
        else:
            escolhido = usuario_requisicao.amigo_secreto                               
     
    return render(request, 'index.html', {'amigo': escolhido})