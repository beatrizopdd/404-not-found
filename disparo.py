from PPlay.gameimage import *
from PPlay.window import *

tela = Window(1280,660)
teclado = tela.get_keyboard()
def criar_disparo(buggy, virada_para, disparo):

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
            break
