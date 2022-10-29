from PPlay.gameimage import *
from PPlay.window import *

#A: Função 30x mais legível usando dicionário como struct de pobre
def criar_disparo(buggy, virada_para, disparo):

    disparo["direção"] = virada_para
    disparo["ativo"] = True

    if disparo["direção"] == "CIMA" or disparo["direção"] == "BAIXO":

        disparo["imagem"] = GameImage("Assets/Choque/choque-vertical.png")

    elif disparo["direção"] == "ESQUERDA" or disparo["direção"] == "DIREITA":

        disparo["imagem"] = GameImage("Assets/Choque/choque-horizontal.png")
    

    disparo["imagem"].set_position(buggy.x + buggy.width/2, buggy.y + buggy.height/2)



def movimento_disparo(disparo, tela):

    if disparo["direção"] == "CIMA":

        disparo["imagem"].y -= disparo["velocidade"] * tela.delta_time()
    
    if disparo["direção"] == "BAIXO":
        
        disparo["imagem"].y += disparo["velocidade"] * tela.delta_time()
    
    if disparo["direção"] == "ESQUERDA":

        disparo["imagem"].x -= disparo["velocidade"] * tela.delta_time()
    
    if disparo["direção"] == "DIREITA":

        disparo["imagem"].x += disparo["velocidade"] * tela.delta_time()



def colide_disparo(disparo, vet_debugger, vet_tela_azul, tela):

    #Se passou das bordas da tela
    if (disparo["imagem"].x + disparo["imagem"].width) <= 0 or (disparo["imagem"].y + disparo["imagem"].height) <= 0 or (disparo["imagem"].x) >= tela.width or (disparo["imagem"].y) >= tela.height:

        disparo["ativo"] = False
        return

    for i in range(len(vet_debugger)):

        if disparo["imagem"].collided(vet_debugger[i]):

            vet_tela_azul[i] = True
            disparo["ativo"] = False
            break


## A: CÓDIGOS OBSOLETOS QUE EU NÃO QUERO APAGAR ##

#A: Função usando lista
'''def criar_disparo(buggy, virada_para, disparo):

    disparo[1] = virada_para
    disparo[3] = True

    if disparo[1] == "CIMA" or disparo[1] == "BAIXO":

        disparo[0] = GameImage("Assets/Choque/choque-vertical.png")

    elif disparo[1] == "ESQUERDA" or disparo[1] == "DIREITA":

        disparo[0] = GameImage("Assets/Choque/choque-horizontal.png")
    

    disparo[0].set_position(buggy.x + buggy.width/2, buggy.y + buggy.height/2)



def movimento_disparo(disparo, vel):

    if disparo[1] == "CIMA":

        disparo[0].y -= vel
    
    if disparo[1] == "BAIXO":
        
        disparo[0].y += vel
    
    if disparo[1] == "ESQUERDA":

        disparo[0].x -= vel
    
    if disparo[1] == "DIREITA":

        disparo[0].x += vel



def colide_disparo(disparo, vet_debugger, vet_tela_azul):

    #Se passou das bordas da tela
    if (disparo[0].x + disparo[0].width) <= 0 or (disparo[0].y + disparo[0].height) <= 0 or (disparo[0].x) >= tela.width or (disparo[0].y) >= tela.height:

        disparo[3] = False
        return

    for i in range(len(vet_debugger)):

        if disparo[0].collided(vet_debugger[i]):

            vet_tela_azul[i] = True
            disparo[3] = False
            break'''


