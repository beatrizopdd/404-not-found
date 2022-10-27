from utilidadesA import *

#A: Implementando toda a lógica de forma separada agora por facilidade
#Depois a gente pode incorporar algumas dessas funções nos elementos do gameloop pra evitar redundâncias
#Ex: Evitar de percorrer a matriz de paredes duas vezes pra mover a buggy e depois pra desenhar

def comportamento_buggy(buggy, vel, teclado, mat_paredes, tile, tela):

    direção_x = 0
    direção_y = 0
    vel *= tela.delta_time()

    #A: Colocar as alterações de sprite depois
    if teclado.key_pressed("LEFT"):

        direção_x = -1

    elif teclado.key_pressed("RIGHT"):

        direção_x = 1
    
    if teclado.key_pressed("UP"):

        direção_y = -1
    
    elif teclado.key_pressed("DOWN"):

        direção_y = 1

    buggy.x += vel * direção_x
    buggy.y += vel * direção_y

    colisão_parede_externa(buggy, tile)

    for vet_paredes in mat_paredes:

        for parede in vet_paredes:

            corrigir_posição(buggy, parede, vel, direção_x, direção_y)

#A: Por mais caro que pareça, não é
#A: Provavelmente dá pra melhorar a legibilidade. Ainda tô tentando cortar algum dos collided
def corrigir_posição(buggy, parede, vel, direção_x, direção_y):

    #A: Lembrar de verificar qual acontece mais, colisão pelo x ou pelo y e colocar encima (baixa prioridade)
    if parede.collided(buggy): #Se a buggy colidiu

        buggy.x += vel * -direção_x #Corrige o movimento no eixo X

        if parede.collided(buggy): #Se o problema não era no X

            buggy.x += vel * direção_x #Descorrige o x
            buggy.y += vel * -direção_y #Corrige o y
        
            if parede.collided(buggy): #Se o problema era nos dois

                buggy.x += vel * -direção_x #Corrige os dois
                buggy.y += vel * -direção_y

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