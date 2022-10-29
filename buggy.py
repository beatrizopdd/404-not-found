from PPlay.sprite import *
from disparo import *
from utilidadesA import *
from PPlay.window import *

#A: Implementando toda a lógica de forma separada agora por facilidade
#Depois a gente pode incorporar algumas dessas funções nos elementos do gameloop pra evitar redundâncias
#Ex: Evitar de percorrer a matriz de paredes duas vezes pra mover a buggy e depois pra desenhar

def comportamento_buggy(buggy, vel, mat_paredes, tile, virada_para, disparo, teclado):

    x_antigo = buggy.x
    y_antigo = buggy.y
    direção_x = 0
    direção_y = 0
    andou = False

    ##A: Lidando com input do jogador

    #A: Registrando pra onde o jogador pretende ir
    #A: Inputs horizontais primeiro pra terem prioridade
    if teclado.key_pressed("RIGHT"):

        if not virada_para == "DIREITA":

            buggy = Sprite("Assets/Buggy/buggy-horizontal.png", 10)
            buggy.set_total_duration(500)
            buggy.set_curr_frame(0)
            buggy.set_sequence(0,4)  

        direção_x = 1
        andou = True
        virada_para = "DIREITA"
    
    elif teclado.key_pressed("LEFT"):

        if not virada_para == "ESQUERDA":

            buggy = Sprite("Assets/Buggy/buggy-horizontal.png", 10)
            buggy.set_total_duration(500)
            buggy.set_curr_frame(5)
            buggy.set_sequence(5,9)

        direção_x = -1
        andou = True
        virada_para = "ESQUERDA"

    elif teclado.key_pressed("UP"):

        if not virada_para == "CIMA":

            buggy = Sprite("Assets/Buggy/buggy-vertical.png", 10)
            buggy.set_total_duration(500)
            buggy.set_curr_frame(5)
            buggy.set_sequence(5,9)

        direção_y = -1
        andou = True
        virada_para = "CIMA"

    elif teclado.key_pressed("DOWN"):

        if not virada_para == "BAIXO":

            buggy = Sprite("Assets/Buggy/buggy-vertical.png", 10)
            buggy.set_total_duration(500)
            buggy.set_curr_frame(0)
            buggy.set_sequence(0,4)

        direção_y = 1
        andou = True
        virada_para = "BAIXO"
    
    #A: Lidando com as interações com mecanismos e disparos
    if teclado.key_pressed("SPACE") and disparo["ativo"] == False:

        criar_disparo(buggy, virada_para, disparo)

    #Realizando as intenções de movimento e verificando se a nova posição do player é válida
    if virada_para == "CIMA" or virada_para == "BAIXO":

        buggy.x = x_antigo
        buggy.y = y_antigo + (vel * direção_y)
    
    elif virada_para == "ESQUERDA" or virada_para == "DIREITA":

        buggy.x = x_antigo + (vel * direção_x)
        buggy.y = y_antigo

    colisão_parede_externa(buggy, tile)

    for vet_paredes in mat_paredes:

        for parede in vet_paredes:

            corrigir_posição(buggy, parede, vel, direção_x, direção_y)
    
    return buggy, andou, virada_para




#A: Por mais caro que pareça, não é
#A: Provavelmente dá pra melhorar a legibilidade. Ainda tô tentando cortar algum dos collided
#A: Lembrar de verificar qual acontece mais, colisão pelo x ou pelo y e colocar encima (baixa prioridade)
def corrigir_posição(buggy, parede, vel, direção_x, direção_y):

    if parede.collided(buggy): #Se a buggy colidiu

        buggy.x += vel * -direção_x #Corrige o movimento no eixo X

        if parede.collided(buggy): #Se o problema não era no X

            buggy.x += vel * direção_x #Descorrige o x
            buggy.y += vel * -direção_y #Corrige o y


            #A: Esse bloco não é mais necessário porque escolhemos desabilitar movimento diagonal pra movimentação ser mais delicada
            '''if parede.collided(buggy): #Se o problema era nos dois

                buggy.x += vel * -direção_x #Corrige os dois
                buggy.y += vel * -direção_y'''

#A: A função pode ser trivial e feia porque a parede externa tá sempre no mesmo lugar
def colisão_parede_externa(objeto, tile):

    lim_esquerdo, lim_superior = cord_grid(tile, 1, 1)
    lim_direito, lim_inferior = cord_grid(tile, 19, 9)


    if objeto.x <= lim_esquerdo:

        objeto.x = lim_esquerdo
    
    if (objeto.x + objeto.width) >= lim_direito:

        objeto.x = lim_direito - objeto.width
    
    if objeto.y <= lim_superior:

        objeto.y = lim_superior
    
    if (objeto.y + objeto.height) >= lim_inferior:

        objeto.y = lim_inferior - objeto.height
