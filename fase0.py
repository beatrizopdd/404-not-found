from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

from buggy import *
from debugger import *
from utilidadesA import *
from utilidadesB import *

tela = Window(1280,660)
tela.set_title("404 Not Found")
teclado = tela.get_keyboard()

#A: Game Images | Todas as imagens de fundo e o disparo
chao = GameImage("Assets/Fundos/chao.png")
tile = Sprite("Assets/Fundos/tile.png") #Declarado só pelo uso na função posiciona_grid

##B: PAREDES
#A: Paredes A3, D1 e D2, nessa ordem
parede1X2 = []
for i in range(3):
    parede1X2.append(GameImage("Assets/Paredes/1X2.png"))
    
#A: Paredes B1, B2 e E2
parede1X3 = []
for i in range(3):
    parede1X3.append(GameImage("Assets/Paredes/1X3.png"))
    
#A: Paredes A2 e C1, nessa ordem
parede4X1 = []
for i in range(2):
    parede4X1.append(GameImage("Assets/Paredes/4X1.png"))

#A: Paredes únicas
paredeE1 = GameImage("Assets/Paredes/1X1.png")
paredeA1 = GameImage("Assets/Paredes/2X1.png")
paredeF1 = GameImage("Assets/Paredes/2X9.png")
paredeC2 = GameImage("Assets/Paredes/3X1.png")
parede_unica = [paredeE1, paredeA1, paredeF1, paredeC2]

#B: Paredes externas esquerda, superior, direita, inferior
pexE = GameImage("Assets/Paredes/pex-e.png")
pexC = GameImage("Assets/Paredes/pex-c.png")
pexD = GameImage("Assets/Paredes/pex-d.png")
pexB = GameImage("Assets/Paredes/pex-b.png")
paredes_externas = [pexE, pexC, pexD, pexB]

#A: Colocando as paredes nas suas posições corretas
posiciona_grid(paredeA1, tile, 3, 2, False)
posiciona_grid(paredeE1, tile, 11,1, False)
posiciona_grid(paredeF1, tile, 9,7, False)
posiciona_grid(paredeC2, tile, 8,6, False)

posiciona_grid(parede1X2[0], tile, 3,5, False)
posiciona_grid(parede1X2[1], tile, 12,4, False)
posiciona_grid(parede1X2[2], tile, 15,4, False)

posiciona_grid(parede1X3[0], tile, 1,8, False)
posiciona_grid(parede1X3[1], tile, 5,8, False)
posiciona_grid(parede1X3[2], tile, 9,3, False)

posiciona_grid(parede4X1[0], tile, 5,2, False)
posiciona_grid(parede4X1[1], tile, 8,1, False)

posiciona_grid(paredes_externas[0], tile, 0, 0, False)
posiciona_grid(paredes_externas[1], tile, 1, 0, False)
posiciona_grid(paredes_externas[2], tile, 19, 0, False)
posiciona_grid(paredes_externas[3], tile, 1, 9, False)

#A: Vetores para facilitar os processo de desenho
paredes = [parede1X2, parede1X3, parede4X1, parede_unica, paredes_externas]


##B: DEBUGGER e CONE
quantidade = 8
debugger_direcao = ["v", "v", "v", "v", "v", "h", "h", "h"]

debugger_vel = []
for i in range(quantidade):
	debugger_vel.append(50)

debuggers = adiciona_debugger(quantidade, debugger_vel, debugger_direcao)

posiciona_grid(debuggers[0], tile, 1, 2)
posiciona_grid(debuggers[1], tile, 6, 6)
posiciona_grid(debuggers[2], tile, 10, 4)
posiciona_grid(debuggers[3], tile, 14, 3)
posiciona_grid(debuggers[4], tile, 17, 5)

posiciona_grid(debuggers[5], tile, 3, 7)
posiciona_grid(debuggers[6], tile, 12, 6)
posiciona_grid(debuggers[7], tile, 17, 2)

cones = []
for i in range(quantidade):
	cone = adiciona_cone(debugger_vel[i], debugger_direcao[i])
	posiciona_cone(cone, debuggers[i], debugger_vel[i], debugger_direcao[i])
	cones.append(cone)


##A: Sprite e variáveis da Buggy
buggy = Sprite("Assets/Buggy/buggy-vertical.png", 10)
buggy.set_sequence(0,4)
virada_para = "BAIXO"
andou = False
buggy.set_total_duration(500)
posiciona_grid(buggy, tile, 1,1)


##B: PONTEIROS
ponteiro_entrada = [Sprite("Assets/Mecanismos/&w.png", 6)]
ponteiro_entrada[0].set_total_duration(400)
posiciona_grid(ponteiro_entrada[0], tile, 4, 8)

ponteiro_saída = [Sprite("Assets/Mecanismos/W.png", 13)]
ponteiro_saída[0].set_total_duration(1000)
posiciona_grid(ponteiro_saída[0], tile, 9, 1)

ponteiros = [ponteiro_entrada, ponteiro_saída]

#A: Vetor com todos os mecanismos
mecanismos = [esconderijo, ponteiro_entrada, ponteiro_saída]


#A: Dicionário com as informações do disparo
disparo = {

    "imagem": GameImage("Assets/Choque/choque-vertical.png"),
    "direção": "CIMA",
    "velocidade": tela.height/2,
    "tempo_esperado": 0,
    "recarga": 3,
    "ativo": False,
}


##B: ESCONDERIJO
qtd_esconderijos = 1
visibilidade = []
for i in range(qtd_esconderijos):
	visibilidade.append(True)

esconderijo = [Sprite("Assets/Mecanismos/hide.png", 22)]
esconderijo[0].set_total_duration(2500)
posiciona_grid(esconderijo[0], tile, 1,7)


##B: DESCONFIOMETRO
contato = False #true = buggy colide com o debugger e ele fica um tempo em "choque"
desconfiometro_pausa = 5 #tempo do debugger ficar em choque
desconfiometro = False
desconfiometro_limite = 10 #tempo que o debugger suporta encontrar a buggy até dar gameover


##B: TELA AZUL
timer_tela_azul = []
for i in range(quantidade):
	timer_tela_azul.append(10)

tela_azul = []
for i in range(quantidade):
	tela_azul.append(False)


##B: todos os objetos que podem fazer o debugger mudar de direção
colidiveis = []
for parede in paredes:
    for p in parede:
        colidiveis.append(p) 
        
for mecanismo in mecanismos:
    for m in mecanismo:
        colidiveis.append(m) 

while True:

        chao.draw()
        
        buggy, andou, virada_para = comportamento_buggy(buggy, tela.height/3 * tela.delta_time(), paredes, ponteiro_entrada, ponteiro_saída, esconderijo, tile, virada_para, disparo, teclado)

        ##B: CONTROLE DO ESCONDERIJO
        for i in range(qtd_esconderijos):
		    if (buggy.collided(esconderijo[i])):
		            visibilidade[i] = False
		    else:
		            visibilidade[i] = True
		
		##B: CONTROLE DO CONTATO e GAMEOVER
		for i in range(quantidade):
			if (desconfiometro == False and tela_azul[i] == False and (False not in visibilidade)): 
				if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])):
					contato = True  
					debuggers = debugger_alerta(quantidade, debuggers, debugger_vel, debugger_direcao)
					
			if (desconfiometro == True and (False not in visibilidade)):
				if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])):
					if (desconfiometro_limite > 0):
						desconfiometro_limite -= tempo()
					else:
						tela.draw_text("GAME OVER", 70, 70, 30, (0,0,0))
				  
		##B: CONTROLE DO DESCONFIOMETRO
		if (contato == True and desconfiometro_pausa > 0):
			tela.draw_text("contato feito {:.0f} segundos".format(desconfiometro_pausa), 70, 70, 30, (0,0,0))
			desconfiometro_pausa -= tempo()
		
		if (desconfiometro_pausa <= 0):
			contato = False
			desconfiometro = True
			
			

		##B: MOVIMENTO DEBUGGER + CONE
        for i in range(quantidade):
                if (debugger_direcao[i] == "v" and contato == False):
                        debuggers[i].y += debugger_vel[i] * tela.delta_time()
                        cones[i].y += debugger_vel[i] * tela.delta_time()
                        
                        for c in colidiveis:
                                debugger_vel[i] *= limitaV(debuggers[i], debugger_vel[i], c)
                                
                                if (alerta == True):
                                        cones[i] = cone_alerta(debugger_vel[i], "v")
                                else:
                                        cones[i] = adiciona_cone(debugger_vel[i], "v")
                                posiciona_cone(cones[i], debuggers[i], debugger_vel[i], "v") 

                if (debugger_direcao[i] == "h" and contato == False):
                        debuggers[i].x += debugger_vel[i] * tela.delta_time()
                        cones[i].x += debugger_vel[i] * tela.delta_time()

                        for c in colidiveis:
                                debugger_vel[i] *= limitaH(debuggers[i], debugger_vel[i], c)
                                
                                if (alerta == True):
                                        cones[i] = cone_alerta(debugger_vel[i], "h")
                                else:
                                        cones[i] = adiciona_cone(debugger_vel[i], "h")
                                posiciona_cone(cones[i], debuggers[i], debugger_vel[i], "h") 



        for mecanismo in mecanismos:
            for m in mecanismo:
                m.draw()
                m.update()

        for parede in paredes:
            for p in parede:
                p.draw()

        for c in cones:
                c.draw()

        for d in debuggers:
                d.draw()
                d.update()

        buggy.draw()
        buggy.update()
        
        
        tela.update()









'''


                                
                                
        ##B: DEBUGGER E CONE
        #B: 1 - verifica direção, se a buggy já foi avistada e se esse debugger ta sob efeito da tela_azul
        #B: 2 - movimento debugger-cone
        #B: 3 - ajuste da orientação debugger-cone ao colidir com as paredes (o cone muda de cor se o desconfiometro=True)
        
        
        ##B: DESCONFIÔMETRO
        #B: 0 - só funciona se a buggy estiver fora do esconderijo
		#B: 1.1 - se colidir com debugger-cone e o desconfiometro+telaAzul=False --> ativa o tempo de espera e debugger muda de cor
        #B: 1.2 - se colidir com debugger-cone e o desconfiometro=True --> gameover
        	#B: não preciso colocar a tela azul aqui pq se o alerta ta ligado não tem tela azul
        #B: 2 - se o tempo de espera estiver ativado ele faz contagem regressiva


        ##B: TELA AZUL
        #B: 1 - se o tiro atingir um dos debuggers --> esconde o tiro, ativa o modo tela azul, troca a sprite
        #B: 3 - quando a contagem acabar: zera o cronometro, desativa o modo tela azul e devolve a sprite original
        #B: 2 - se tiver de tela azul vai começar uma contagem regressiva
        rascunho do tiro
        if (disparo_dado == True):
                tiro.draw()
                tiro.y += velocidade
        fim do rascunho
        
        for i in range(quantidade):
                if (tiro.collided(debuggers[i]) and alerta == False): #B: 0 - NÃO OFICIAL só pode dar tela azul se desconfiometro=False
                        disparo_dado = False
                        tela_azul[i] = True
                        debuggers[i] = debugger_tela_azul(debuggers[i], debugger_vel[i], debugger_direcao[i])

                if (timer_tela_azul[i] <= 0):
                        tela_azul[i] = False
                        debuggers[i] = debugger_normal(debuggers[i], debugger_vel[i], debugger_direcao[i], contato, alerta)

                if (tela_azul[i] == True):
                        tela.draw_text("tela azul {:.0f} segundos".format(timer_tela_azul[i]), 70, 140, 30, (0,0,0))
                        timer_tela_azul[i] -= tela.delta_time()
                else:
                        timer_tela_azul[i] = 10
'''

    
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
