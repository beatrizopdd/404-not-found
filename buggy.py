from utilidadesA import *

#A: Implementando toda a lógica de forma separada agora por facilidade
#Depois a gente pode incorporar algumas dessas funções nos elementos do gameloop pra evitar redundâncias
#Ex: Evitar de percorrer a matriz de paredes duas vezes pra mover a buggy e depois pra desenhar

#A: Eu apaguei a solução com correção de movimento porque eu achei que ia conseguir resolver hoje
def movimento_buggy(buggy, vel, teclado, mat_paredes, tela):

    '''dir_usadas = []
    vel *= tela.delta_time()
    
    x_futuro = buggy.x
    y_futuro = buggy.y

    if teclado.key_pressed("LEFT"):

        x_futuro -= vel
        dir_usadas.append("LEFT")

    elif teclado.key_pressed("RIGHT"):

        x_futuro += vel
        dir_usadas.append("RIGHT")
    
    if teclado.key_pressed("UP"):

        y_futuro -= vel
        dir_usadas.append("UP")
    
    elif teclado.key_pressed("DOWN"):

        y_futuro += vel
        dir_usadas.append("DOWN")'''

#A: Essa lógica funciona e dá pra polir a buggy agarrando nas paredes, mas vai dar erro em frame rates mais baixas.
    buggy.move_key_x(vel * tela.delta_time())
    buggy.move_key_y(vel * tela.delta_time())

    for vet_paredes in mat_paredes:

        for parede in vet_paredes:

            if parede.collided(buggy):

                buggy.move_key_x(vel * tela.delta_time() * -1)
                buggy.move_key_y(vel * tela.delta_time() * -1)


#A: Só é usada em um trecho, mas eu fiz separada pra facilitar o reposicionamento no código da fase depois
#A: Fica desagradavelmente extensa porque testar só com as quinas gera alguns erros graves de ejeção
#def corrigir_pos(x,y, parede, vel, dir_usadas):

#def corrige_pos(buggy, parede, vel, dir_usadas):

    
