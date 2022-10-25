from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

from utilidadesB import *

tela = Window(1280,660)
tela.set_title("404 Not Found")
teclado = tela.get_keyboard()

chao = GameImage("Assets/Fundos/chao.png")


''' RASCUNHOS PAREDE, BUGGY e VETOR '''
pexE = GameImage("Assets/Paredes/pex-e.png")
pexE.set_position(0,0)

pexC = GameImage("Assets/Paredes/pex-c.png")
pexC.set_position((tela.width - pexC.width) / 2,0)

pexD = GameImage("Assets/Paredes/pex-d.png")
pexD.set_position(tela.width - pexD.width,0)

pexB = GameImage("Assets/Paredes/pex-b.png")
pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

paredes = [pexE,pexC,pexD,pexB]

buggy = Sprite("Assets/Buggy/buggy-baixo.png", 5)
buggy.set_position(64,66)
buggy.set_total_duration(500)
velocidade = 100

tiro = GameImage("Assets/tiro.png")
disparo_dado = False

##B: ESCONDERIJO
##B: TERMINA ESCONDERIJO


##B: DEBUGGER
qtd = 3
direcao = ["v","h","v"]

vel = []
for i in range(qtd):
	vel.append(100)

debuggers = adiciona_debugger(qtd, vel, direcao)

''' (NÃO CORINGA) a posição vai ter que ser feita na mão pq cada nível vai ter uma específica pra cada debugger '''
debuggers[0].set_position(128,132)
debuggers[1].set_position(128, tela.height - 132)
debuggers[2].set_position(tela.width - 192, 132)
''' (NÃO CORINGA) '''
'''A: Por isso eu fiz a função posiciona_grid'''

cones = []
for i in range(qtd):
	cone = adiciona_cone(vel[i], direcao[i])
	posiciona_cone(debuggers[i], cone, vel[i], direcao[i])
	cones.append(cone)
##B: TERMINA DEBUGGER


##B: TELA AZUL
timer_tela_azul = 10

tela_azul = []
for i in range(qtd):
	tela_azul.append(False)
##B: TERMINA TELA AZUL


##B: DESCONFIOMETRO
timer_desc = 5 #tempo do debuger ficar parado
contato = False #true = buggy colide com o debugger e ele fica um tempo em "choque"
alerta = False #se ocorrer outra colisão enquanto true então fim de jogo
##B: TERMINA DESCONFIOMETRO







while True:

        chao.draw()

        #rascunho de controle da buggy
        if (teclado.key_pressed("up")):
                buggy.y -= velocidade * tela.delta_time()
        if (teclado.key_pressed("right")):
                buggy.x += velocidade * tela.delta_time()
        if (teclado.key_pressed("down")):
                buggy.y += velocidade * tela.delta_time()
        if (teclado.key_pressed("left")):
                buggy.x -= velocidade * tela.delta_time()
        if (teclado.key_pressed("space")):
                disparo_dado = True
                tiro.x = buggy.x
                tiro.y = buggy.y

        #B: 1 - verifica direção, se a buggy já foi avistada e se esse debugger ta sob efeito da tela_azul
        #B: 2 - movimento debugger-cone
        #B: 3 - ajuste da orientação debugger-cone ao colidir com as paredes (o cone muda de cor se o desconfiometro=True)
        for i in range(qtd):
                if (direcao[i] == "v" and contato == False and tela_azul[i] == False):
                        debuggers[i].y += vel[i] * tela.delta_time()
                        cones[i].y += vel[i] * tela.delta_time()
                        
                        for p in paredes:
                                vel[i] *= limitaV(debuggers[i], vel[i], p)
                                if (alerta == True):
                                        cones[i] = alerta_adiciona_cone(vel[i], direcao[i])
                                else:
                                        cones[i] = adiciona_cone(vel[i], direcao[i])
                                posiciona_cone(debuggers[i], cones[i], vel[i], direcao[i]) 

                if (direcao[i] == "h" and contato == False and tela_azul[i] == False):
                        debuggers[i].x += vel[i] * tela.delta_time()
                        cones[i].x += vel[i] * tela.delta_time()

                        for p in paredes:
                                vel[i] *= limitaH(debuggers[i], vel[i], p)
                                if (alerta == True):
                                        cones[i] = alerta_adiciona_cone(vel[i], direcao[i])
                                else:
                                        cones[i] = adiciona_cone(vel[i], direcao[i])
                                posiciona_cone(debuggers[i], cones[i], vel[i], direcao[i]) 


	#B: 1.1 - se colidir com debugger-cone e o desconfiometro=False --> ativa o tempo de espera e debugger muda de cor
        #B: 1.2 - se colidir com debugger-cone e o desconfiometro=True --> gameover
        #B: 2 - se o tempo de espera estiver ativado ele faz contagem regressiva
        #B: 3 - quando a contagem acabar zera o cronometro, desativa o tempo de espera e ativa o desconfiometro
        for i in range(qtd):
                if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])) and alerta == False:
                        contato = True
                        debuggers = alerta_debugger(qtd, vel, direcao, debuggers)
                        
                if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])) and alerta == True:
                        tela.draw_text("GAME OVER", 70, 70, 30, (0,0,0))
                        
        if (contato == True):
                tela.draw_text("contato feito {:.0f} segundos".format(timer_desc), 70, 70, 30, (0,0,0))
                timer_desc -= tela.delta_time()
                
        if (timer_desc <= 0):
                timer_desc = 5
                contato = False
                alerta = True
                
        #rascunho do tiro
        if (disparo_dado == True):
                tiro.draw()
                tiro.y += velocidade
                
        #B: 1 - se o tiro atingir um dos debuggers --> esconde o tiro, ativa o modo tela azul, troca a sprite
        #B: 3 - quando a contagem acabar zera o cronometro, desativa o modo tela azul e devolve a sprite original
        #B: 2 - se tiver pelo menos 1 de tela azul vai começar uma contagem regressiva
        for i in range(qtd):
                if (tiro.collided(debuggers[i])):
                        disparo_dado = False
                        tela_azul[i] = True
                        debuggers[i] = tela_azul_debugger(debuggers[i], vel[i], direcao[i])

                if (timer_tela_azul <= 0):
                        tela_azul[i] = False
                        debuggers[i] = normal_debugger(debuggers[i], vel[i], direcao[i])
                        
        if (True in tela_azul):
                tela.draw_text("tela azul {:.0f} segundos".format(timer_tela_azul), 70, 140, 30, (0,0,0))
                timer_tela_azul -= tela.delta_time()
        else:
                timer_tela_azul = 10
                


        for p in paredes:
                p.draw()

        for c in cones:
                c.draw()

        for d in debuggers:
                d.draw()
                d.update()

        buggy.draw()
        buggy.update()
        
        tela.update()











    
########## RASCUNHOS ##########

'''
##B: PAREDES DE RASCUNHO PRA TESTE
pexE = GameImage("Assets/Paredes/pex-e.png")
pexE.set_position(0,0)

pexC = GameImage("Assets/Paredes/pex-c.png")
pexC.set_position((tela.width - pexC.width) / 2,0)

pexD = GameImage("Assets/Paredes/pex-d.png")
pexD.set_position(tela.width - pexD.width,0)

pexB = GameImage("Assets/Paredes/pex-b.png")
pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

parede = GameImage("Assets/Paredes/2X9.png")
parede.set_position(2 * 64, 7 * 66)

paredes = [parede,pexE,pexC,pexD,pexB]
##B: TERMINA PAREDES DE RASCUNHO PRA TESTE
'''

'''
##B: DEBUGGER
qtd = 6 #quantidade de debuggers
direcao = ["v","v","v","h","h","h"]

vel = []
for i in range(qtd):
	vel.append(100)

debuggers = adiciona_debugger(qtd, vel, direcao)

#insira as posições dos seus debuggers

cones = []
for i in range(qtd):
	cone = adiciona_cone(vel[i], direcao[i])
	posiciona_cone(debuggers[i], cone, vel[i], direcao[i])
	cones.append(cone)
##B: TERMINA DEBUGGER
'''
