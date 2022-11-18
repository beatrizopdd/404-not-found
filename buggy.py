from PPlay.sprite import *
from disparo import *
from utilidades_grid import *
from PPlay.window import *

#A: Implementando toda a lógica de forma separada agora por facilidade
#Depois a gente pode incorporar algumas dessas funções nos elementos do gameloop pra evitar redundâncias
#Ex: Evitar de percorrer a matriz de paredes duas vezes pra mover a buggy e depois pra desenhar

def comportamento_buggy(buggy, vel, mat_paredes, ponteiro_entrada, ponteiro_saída, vet_esconderijos, tile, virada_para, disparo, teclado):

    x_antigo = buggy.x
    y_antigo = buggy.y

    #As variáveis direção assumem os valores -1,0 e 1 para multiplicar a velocidade
    direção_x = 0
    direção_y = 0
    andou = False

    ##A: Lidando com input do jogador

    #A: Registrando pra onde o jogador pretende ir
    #A: Inputs horizontais primeiro pra terem prioridade
    if teclado.key_pressed("RIGHT"):

        if not virada_para == "DIREITA":

            buggy = Sprite("Assets/Buggy/buggy-horizontal-2.png", 10)
            buggy.set_total_duration(500)
            buggy.set_curr_frame(0)
            buggy.set_sequence(0,4)  

        direção_x = 1
        andou = True
        virada_para = "DIREITA"
    
    elif teclado.key_pressed("LEFT"):

        if not virada_para == "ESQUERDA":

            buggy = Sprite("Assets/Buggy/buggy-horizontal-2.png", 10)
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


    #A: Realizando as intenções de movimento e verificando se a nova posição do player é válida
    #A: Esse passo é necessário por conta das mudanças de sprite
    if virada_para == "CIMA" or virada_para == "BAIXO":

        buggy.x = x_antigo
        buggy.y = y_antigo + (vel * direção_y)
    
    elif virada_para == "ESQUERDA" or virada_para == "DIREITA":

        buggy.x = x_antigo + (vel * direção_x)
        buggy.y = y_antigo    


    colisão_parede_externa(buggy, tile)
    colisão_paredes_internas(buggy, mat_paredes, virada_para, vel)


    #A: Lidando com as interações com mecanismos
    if teclado.key_pressed("SPACE"):

        for i in range(len(ponteiro_entrada)):

            if buggy.collided(ponteiro_entrada[i]):

                buggy.x = ponteiro_saída[i].x + ponteiro_saída[i].width/2 - buggy.width/2
                buggy.y = ponteiro_saída[i].y + ponteiro_saída[i].height/2 - buggy.height/2
                break
            
        for esconderijo in vet_esconderijos:

            if buggy.collided(esconderijo):

                #A: Inserir aqui a lógica de esconderijo de Bia
                break

    if teclado.key_pressed("Z") and (disparo["tempo_esperado"] >= disparo["recarga"]):

        criar_disparo(buggy, virada_para, disparo)
        disparo["tempo_esperado"] = 0


    return buggy, andou, virada_para


#Gera meio que um step assist interessante, mas tem um bug muito esquisito com quinas
def correção_por_retas(buggy, parede):

    #Gerando as retas que compões as fronteiras da parede
    fronteira_esquerda = (parede.rect.topleft, parede.rect.bottomleft)
    fronteira_inferior = (parede.rect.bottomleft, parede.rect.bottomright)
    fronteira_direita = (parede.rect.bottomright, parede.rect.topright)
    fronteira_superior = (parede.rect.topright, parede.rect.topleft)

    if buggy.rect.clipline(fronteira_esquerda): #Se ela colidiu com o lado esquerdo da parede

        buggy.x -= (buggy.x + buggy.width) - parede.x
    
    elif buggy.rect.clipline(fronteira_direita): #Se colidiu com o direito

        buggy.x += (parede.x + parede.width) - buggy.x

    if buggy.rect.clipline(fronteira_superior): #Se colidiu na parte de cima

        buggy.y -= (buggy.y + buggy.height) - parede.y
    
    elif buggy.rect.clipline(fronteira_inferior): #Se colidiu por baixo

        buggy.y += (parede.y + parede.height) - buggy.y

#Tentativa de criar uma colisão genérica através de algum cálculo vetorial. Falha miseravelmente
def correção_vetorial(buggy, parede):

    vet = pygame.math.Vector2()

    vet.x = buggy.rect.centerx - parede.rect.centerx
    vet.y = buggy.rect.centery - parede.rect.centery

    vet = vet.normalize()
       
    while buggy.collided(parede):

        buggy.rect.center += vet
        buggy.set_position(buggy.rect.centerx, buggy.rect.centery)

#Colisão estúpida e instintiva. Falha com sprites não quadradas em quinas
def correção_por_direção(buggy, virada_para, velocidade):

    if virada_para == "ESQUERDA":

        buggy.x += velocidade
    
    if virada_para == "DIREITA":

        buggy.x -= velocidade
    
    if virada_para == "CIMA":

        buggy.y += velocidade
    
    if virada_para == "BAIXO":

        buggy.y -= velocidade


def colisão_paredes_internas(buggy, mat_paredes, virada_para, velocidade):

    for vet_paredes in mat_paredes:

        for parede in vet_paredes:

            if parede.collided(buggy):

                correção_por_direção(buggy, virada_para, velocidade)


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




#A: Função obsoleta pela atual inexistênia de movimento diagonal
def colisão_paredes_internas_obsoleta(buggy, mat_paredes, vel, direção_x, direção_y):

    for vet_paredes in mat_paredes:

        for parede in vet_paredes:

            if parede.collided(buggy):

                buggy.x += vel * -direção_x #Corrige o movimento no eixo X

                if parede.collided(buggy): #Se o problema não era no X ele está no Y

                    buggy.x += vel * direção_x #Descorrige o x
                    buggy.y += vel * -direção_y #Corrige o y