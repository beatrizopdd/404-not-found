from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

from utilidadesB import *

def movimento_debugger(debugger, cone, direcao, vel, limite, cpdl, tempo):
                        
		if (direcao == "v"):
				debugger.y += vel * tempo
				cone.y += vel * tempo
                
				vel *= limitaV(debugger, vel, limite)

				if (cpdl[2] == True or cpdl[0] == True):
					cone = cone_alerta(vel, "v")
				else:
					cone = adiciona_cone(vel, "v")
				posiciona_cone(cone, debugger, vel, "v") 

		if (direcao == "h"):
				debugger.x += vel * tempo
				cone.x += vel * tempo

				vel *= limitaH(debugger, vel, limite)

				if (cpdl[2] == True or cpdl[0] == True):
					cone = cone_alerta(vel, "h")
				else:
					cone = adiciona_cone(vel, "h")
				posiciona_cone(cone, debugger, vel, "h")

		return debugger, cone, vel

                        
def desvio_armadilha(debugger, cone, esconderijo, direcao, vel, cpdl, tempo):

        encontro = False

        if (direcao == "v"):

                if (esconderijo.y < debugger.y and vel > 0): #esconderijo mais pra cima e descendo
                        vel *= -1
                        debugger.set_sequence_time(4, 8, 400, True) #troca pra cima
                if (esconderijo.y > debugger.y and vel < 0): #esconderijo mais pra baixo e subindo
                        vel *= -1
                        debugger.set_sequence_time(0, 4, 400, True) #troca pra baixo

                if (cpdl[2] == True or cpdl[0] == True):
                        cone = cone_alerta(vel, "v")
                else:
                        cone = adiciona_cone(vel, "v")
                posiciona_cone(cone, debugger, vel, "v") 
                
                debugger.y += vel * tempo
                cone.y += vel * tempo

                if (debugger.collided(esconderijo) and vel < 0) or (debugger.collided(esconderijo) and vel > 0):
                        encontro = True


        if (direcao == "h"):

                if (esconderijo.x > debugger.y and vel < 0): #esconderijo mais na direita e indo pra esquerda
                        vel *= -1
                        debugger.set_sequence_time(4, 8, 400, True) #troca pra direita
                if (esconderijo.x < debugger.y and vel > 0): #esconderijo mais na esquerda e indo pra direita
                        vel *= -1
                        debugger.set_sequence_time(0, 4, 400, True) #troca pra esquerda

                if (cpdl[2] == True or cpdl[0] == True):
                        cone = cone_alerta(vel, "h")
                else:
                        cone = adiciona_cone(vel, "h")
                posiciona_cone(cone, debugger, vel, "h")
                
                debugger.x += vel * tempo
                cone.x += vel * tempo

                if (debugger.collided(esconderijo) and vel < 0) or (debugger.collided(esconderijo) and vel > 0):
                        encontro = True

        return debugger, cone, vel, encontro


def analise_esconderijo(debugger, cone, esconderijo, direcao, vel, tempo):

        erro = 0

        if (tempo > 0):
                if (direcao == "v"):
                        if (vel < 0):
                                debugger.y = (esconderijo.y + esconderijo.height) + debugger.height + erro
                        if (debugger.collided(esconderijo) and vel > 0):
                                debugger.y = esconderijo.y - debugger.height - erro
                
                if (direcao == "h"):
                        if (vel < 0):
                                debugger.x = (esconderijo.x + esconderijo.width) + debugger.width + erro
                        if (vel > 0):
                                debugger.x = esconderijo.x - debugger.width - erro
                                
                posiciona_cone(cone, debugger, vel, direcao)
                
                distraido = True
                encontro = True
                
        if (tempo <= 0):
                distraido = False
                encontro = False
                tempo = 10

        return distraido, tempo, encontro
            

def desconfiometro(cpdl, buggy, debugger, cone, visibilidade, tela):

	#contato = cpdl[0] // pausa = cpdl[1] // desconfiometro = cpdl[2] // limite = cpdl[3]
        
        if (cpdl[3] > 0):
                tela.draw_text("Desconfiometro {:.0f} segundos".format(cpdl[3]), 70, 70, 30, (0,0,0))
                if ((buggy.collided(debugger) or buggy.collided(cone)) and (False not in visibilidade)): #condiciona a contagem regressiva do desconfiometro a estar visivel
                        cpdl[3] -= tela.delta_time()

        if (cpdl[3] <= 0):
                tela.draw_text("GAME OVER", 70, 70, 30, (0,0,0))

        return cpdl
