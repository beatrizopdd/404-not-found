from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

from utilidadesB import *

def debugger_desconfiometro(desconfiometro, buggy, debugger, cone, visibilidade, tela):

        if (desconfiometro["limite"] > 0):
                tela.draw_text("Desconfiometro {:.0f} segundos".format(desconfiometro["limite"]), 70, 70, 30, (0,0,0))
                #condiciona a contagem regressiva do desconfiometro a estar visivel
                if ((buggy.collided(cone)) and (False not in visibilidade)): 
                        desconfiometro["limite"] -= tela.delta_time()
                if (buggy.collided(debugger) and (False not in visibilidade)):
                        desconfiometro["limite"] = 0

        if (desconfiometro["limite"] <= 0):
                tela.draw_text("GAME OVER", 70, 70, 30, (0,0,0))

         
def desvio_armadilha(debugger, cone, esconderijo, direcao, vel, desconfiometro, tela):

        encontro = False

        if (direcao == "v"):

                if (esconderijo.y < debugger.y and vel > 0): #esconderijo mais pra cima e descendo
                        vel *= -1
                        debugger.set_sequence_time(4, 8, 400, True) #troca pra cima
                if (esconderijo.y > debugger.y and vel < 0): #esconderijo mais pra baixo e subindo
                        vel *= -1
                        debugger.set_sequence_time(0, 4, 400, True) #troca pra baixo

                if (desconfiometro["ativo"] == True or desconfiometro["pausa"] == True):
                        cone = cone_alerta(vel, "v")
                else:
                        cone = adiciona_cone(vel, "v")
                posiciona_cone(cone, debugger, vel, "v") 
                
                debugger.y += vel * tela.delta_time()
                cone.y += vel * tela.delta_time()

                if (cone.collided(esconderijo) and vel < 0) or (cone.collided(esconderijo) and vel > 0):
                        encontro = True


        if (direcao == "h"):

                if (esconderijo.x > debugger.y and vel < 0): #esconderijo mais na direita e indo pra esquerda
                        vel *= -1
                        debugger.set_sequence_time(4, 8, 400, True) #troca pra direita
                if (esconderijo.x < debugger.y and vel > 0): #esconderijo mais na esquerda e indo pra direita
                        vel *= -1
                        debugger.set_sequence_time(0, 4, 400, True) #troca pra esquerda

                if (desconfiometro["ativo"] == True or desconfiometro["pausa"] == True):
                        cone = cone_alerta(vel, "h")
                else:
                        cone = adiciona_cone(vel, "h")
                posiciona_cone(cone, debugger, vel, "h")
                
                debugger.x += vel * tela.delta_time()
                cone.x += vel * tela.delta_time()

                if (cone.collided(esconderijo) and vel < 0) or (cone.collided(esconderijo) and vel > 0):
                        encontro = True

        return debugger, cone, vel, encontro


def analise_esconderijo(debugger, cone, esconderijo, direcao, vel, tempo):

        erro = 0

        if (tempo > 0):
                if (direcao == "v"):
                        if (vel < 0):
                                debugger.y = (esconderijo.y + esconderijo.height) + cone.height + erro
                        if (vel > 0):
                                debugger.y = esconderijo.y - cone.height - debugger.height - erro
                
                if (direcao == "h"):
                        if (vel < 0):
                                debugger.x = (esconderijo.x + esconderijo.width) + cone.width + erro
                        if (vel > 0):
                                debugger.x = esconderijo.x - cone.width - debugger.width - erro
                                
                posiciona_cone(cone, debugger, vel, direcao)
                
                distraido = True
                encontro = True
                
        if (tempo <= 0):
                distraido = False
                encontro = False
                tempo = 10

        return distraido, tempo, encontro
            
'''

ESCONDERIJO


'''
#linha 109
distraidos = []
for i in range(quantidade):
	distraidos.append(False)
	
#linha 124
##B: ESCONDERIJO
qtd_esconderijos = 1
sacrificado = 0 
esconderijo_colisao = False
esconderijo_tempo = 10
esconderijo_debugger = [5]

visibilidade = []
for i in range(qtd_esconderijos):
	visibilidade.append(True)

esconderijo = [Sprite("Assets/Mecanismos/hide.png", 22)]
esconderijo[0].set_total_duration(2500)
posiciona_grid(esconderijo[0], tile, 1, 7)

#linha 212
##B: ESCONDERIJO
        for i in range(qtd_esconderijos):
        
            if (buggy.collided(esconderijo[i])):
                visibilidade[i] = False
                break
            else:
                visibilidade[i] = True

            if (buggy.collided(esconderijo[i]) and teclado.key_pressed("C")):
                
                sacrificado = i
                distraidos[esconderijo_debugger[i]] = True  
                break 
          
#linha 241
##B: ESCONDERIJO                
            #movimento sob efeito do esconderijo (sair de onde está e ir em direcao a ele)
            if (distraidos[i] == True and esconderijo_colisao == False):
                debuggers[i], cones[i], debugger_vel[i], esconderijo_colisao = desvio_armadilha(debuggers[i], cones[i], esconderijo[sacrificado], debugger_direcao[i], debugger_vel[i], desconfiometro, tela)
                
            #contagem regressiva do efeito do esconderijo
            if (distraidos[i] == True and esconderijo_colisao == True):
                distraidos[i], esconderijo_tempo, esconderijo_colisao = analise_esconderijo(debuggers[i], cones[i], esconderijo[sacrificado], debugger_direcao[i], debugger_vel[i], esconderijo_tempo)
                
                tela.draw_text("Esconderijo {:.0f} segundos".format(esconderijo_tempo), 70, 120, 30, (0,0,0))
                esconderijo_tempo -= tela.delta_time()      
                
