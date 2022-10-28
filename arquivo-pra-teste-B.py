from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

from utilidadesB import *

tela = Window(1280,660)
tela.set_title("404 Not Found")
teclado = tela.get_keyboard()


''' RASCUNHOS CHÃO, PAREDE, BUGGY e VETOR '''
chao = GameImage("Assets/Fundos/chao.png")

pexE = GameImage("Assets/Paredes/pex-e.png")
pexE.set_position(0, 0)

pexC = GameImage("Assets/Paredes/pex-c.png")
pexC.set_position((tela.width - pexC.width) / 2, 0)

pexD = GameImage("Assets/Paredes/pex-d.png")
pexD.set_position(tela.width - pexD.width, 0)

pexB = GameImage("Assets/Paredes/pex-b.png")
pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

buggy = Sprite("Assets/Buggy/buggy-baixo.png", 5)
buggy.set_position(64,66)
buggy.set_total_duration(500)
velocidade = 100

tiro = GameImage("Assets/tiro.png")
disparo_dado = False


##B: ESCONDERIJO
qtd_esconderijos = 1
visibilidade = True

esconderijo = Sprite("Assets/Mecanismos/hide.png", 22)
esconderijo.set_total_duration(2200)

esconderijo.set_position(64 * 5, 66 * 4)
##B: TERMINA ESCONDERIJO


##B: DEBUGGER
quantidade = 3
direcao = ["v","h","v"]

vel = []
for i in range(quantidade):
	vel.append(100)

debuggers = adiciona_debugger(quantidade, vel, direcao)

''' (NÃO CORINGA) '''
debuggers[0].set_position(128,132)
debuggers[1].set_position(64 * 7, tela.height - 66 * 6)
debuggers[2].set_position(tela.width - 192, 132)
''' (NÃO CORINGA) '''

cones = []
for i in range(quantidade):
	cone = adiciona_cone(vel[i], direcao[i])
	posiciona_cone(debuggers[i], cone, vel[i], direcao[i])
	cones.append(cone)
##B: TERMINA DEBUGGER


##B: TELA AZUL
timer_tela_azul = []
for i in range(quantidade):
	timer_tela_azul.append(10)

tela_azul = []
for i in range(quantidade):
	tela_azul.append(False)
##B: TERMINA TELA AZUL


##B: DESCONFIOMETRO
timer_desconfiado = 5 #tempo do debuger ficar parado
contato = False #true = buggy colide com o debugger e ele fica um tempo em "choque"
alerta = False #se ocorrer outra colisão enquanto true então fim de jogo
##B: TERMINA DESCONFIOMETRO

objetos = [pexE,pexC,pexD,pexB,esconderijo] #o esconderijo entra aqui pra facilitar o draw() e o uso do limite mas só no teste

while True:

        chao.draw()

        ##B: ESCONDERIJO
        if (buggy.collided(esconderijo)):
                visibilidade = False
        else:
                visibilidade = True

        '''rascunho de controle da buggy'''
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
        '''fim do rascunho'''

        ##B: DEBUGGER E CONE
        #B: 1 - verifica direção, se a buggy já foi avistada e se esse debugger ta sob efeito da tela_azul
        #B: 2 - movimento debugger-cone
        #B: 3 - ajuste da orientação debugger-cone ao colidir com as paredes (o cone muda de cor se o desconfiometro=True)
        for i in range(quantidade):
                if (direcao[i] == "v" and contato == False and tela_azul[i] == False):
                        debuggers[i].y += vel[i] * tela.delta_time()
                        cones[i].y += vel[i] * tela.delta_time()
                        
                        for o in objetos:
                                vel[i] *= limitaV(debuggers[i], vel[i], o)
                                
                                if (alerta == True):
                                        cones[i] = cone_alerta(vel[i], direcao[i])
                                else:
                                        cones[i] = adiciona_cone(vel[i], direcao[i])
                                posiciona_cone(debuggers[i], cones[i], vel[i], direcao[i]) 

                if (direcao[i] == "h" and contato == False and tela_azul[i] == False):
                        debuggers[i].x += vel[i] * tela.delta_time()
                        cones[i].x += vel[i] * tela.delta_time()

                        for o in objetos:
                                vel[i] *= limitaH(debuggers[i], vel[i], o)
                                
                                if (alerta == True):
                                        cones[i] = cone_alerta(vel[i], direcao[i])
                                else:
                                        cones[i] = adiciona_cone(vel[i], direcao[i])
                                posiciona_cone(debuggers[i], cones[i], vel[i], direcao[i]) 


        ##B: DESCONFIÔMETRO
        #B: 0 - só funciona se a buggy estiver fora do esconderijo
	#B: 1.1 - se colidir com debugger-cone e o desconfiometro+telaAzul=False --> ativa o tempo de espera e debugger muda de cor
        #B: 1.2 - se colidir com debugger-cone e o desconfiometro=True --> gameover
        	#B: não preciso colocar a tela azul aqui pq se o alerta ta ligado não tem tela azul
        #B: 2 - se o tempo de espera estiver ativado ele faz contagem regressiva
        #B: 3 - quando a contagem acabar: zera o cronometro, desativa o tempo de espera e ativa o desconfiometro
        if (visibilidade == True):
                for i in range(quantidade):
                        if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])) and alerta == False and tela_azul[i] == False:
                                contato = True
                                debuggers = debugger_alerta(quantidade, debuggers, vel, direcao)
                                
                        if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])) and alerta == True:
                                tela.draw_text("GAME OVER", 70, 70, 30, (0,0,0))
                                
        if (contato == True):
                tela.draw_text("contato feito {:.0f} segundos".format(timer_desconfiado), 70, 70, 30, (0,0,0))
                timer_desconfiado -= tela.delta_time()
                        
        if (timer_desconfiado <= 0):
                timer_desconfiado = 5
                contato = False
                alerta = True

        ##B: TELA AZUL
        #B: 1 - se o tiro atingir um dos debuggers --> esconde o tiro, ativa o modo tela azul, troca a sprite
        #B: 3 - quando a contagem acabar: zera o cronometro, desativa o modo tela azul e devolve a sprite original
        #B: 2 - se tiver de tela azul vai começar uma contagem regressiva
        '''rascunho do tiro'''
        if (disparo_dado == True):
                tiro.draw()
                tiro.y += velocidade
        '''fim do rascunho'''
        
        for i in range(quantidade):
                if (tiro.collided(debuggers[i]) and alerta == False): #B: 0 - NÃO OFICIAL só pode dar tela azul se desconfiometro=False
                        disparo_dado = False
                        tela_azul[i] = True
                        debuggers[i] = debugger_tela_azul(debuggers[i], vel[i], direcao[i])

                if (timer_tela_azul[i] <= 0):
                        tela_azul[i] = False
                        debuggers[i] = debugger_normal(debuggers[i], vel[i], direcao[i], contato, alerta)

                if (tela_azul[i] == True):
                        tela.draw_text("tela azul {:.0f} segundos".format(timer_tela_azul[i]), 70, 140, 30, (0,0,0))
                        timer_tela_azul[i] -= tela.delta_time()
                else:
                        timer_tela_azul[i] = 10


        for o in objetos:
                o.draw()

        for c in cones:
                c.draw()

        for d in debuggers:
                d.draw()
                d.update()

        buggy.draw()
        buggy.update()
        
        esconderijo.update()
        
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
quantidade = 6 #quantidade de debuggers
direcao = ["v","v","v","h","h","h"]

vel = []
for i in range(quantidade):
	vel.append(100)

debuggers = adiciona_debugger(quantidade, vel, direcao)

#insira as posições dos seus debuggers

cones = []
for i in range(quantidade):
	cone = adiciona_cone(vel[i], direcao[i])
	posiciona_cone(debuggers[i], cone, vel[i], direcao[i])
	cones.append(cone)
##B: TERMINA DEBUGGER
'''

'''
##B: ESCONDERIJO
qtd_esconderijos = 1

esconderijos = []
for i in range(qtd_esconderijos):
        esconderijo = Sprite("Assets/Mecanismos/hide.png", 22)
        esconderijo.set_total_duration(2200)
	esconderijos.append(esconderijo)
	
##B: TERMINA ESCONDERIJO
'''
