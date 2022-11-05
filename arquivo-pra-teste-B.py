from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

from buggy import *
from utilidadesA import *

from recursos import *
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

distraido = []
for i in range(quantidade):
	distraido.append(False)

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

unX = tile.width
unY = tile.height
debugger_limite = [[unY, unY * 6], [unY, unY * 7], [unY * 4, unY * 6], [unY, unY * 6], [unY, unY * 6], [unX * 2, unX * 7], [unX * 9, unX * 18], [unX * 9, unX * 18]]

##A: Sprite e variáveis da Buggy
buggy = Sprite("Assets/Buggy/buggy-vertical.png", 10)
buggy.set_sequence(0,4)
virada_para = "BAIXO"
andou = False
buggy.set_total_duration(500)
posiciona_grid(buggy, tile, 1,1)


##B: ESCONDERIJO
qtd_esconderijos = 1
alvo = 0 
encontro = False
esconderijo_tempo = 10
esconderijo_debugger = [5]

visibilidade = []
for i in range(qtd_esconderijos):
	visibilidade.append(True)

esconderijo = [Sprite("Assets/Mecanismos/hide.png", 22)]
esconderijo[0].set_total_duration(2500)
posiciona_grid(esconderijo[0], tile, 1,7)


##B: DESCONFIOMETRO
desconfiometro = {
    "pre_desc": False,
    "pausa_timer": 10,
    "desc": False,
    "limite_desc": 10,
}


##A: PONTEIROS
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


##B: TELA AZUL
timer_tela_azul = []
tela_azul = []
for i in range(quantidade):
	timer_tela_azul.append(10)
	tela_azul.append(False)


#A: Pro nosso controle de fps
cronometro_fps = 0
frames = 0
taxa_de_quadros = 0

while True:

        cronometro_fps += tela.delta_time()
        frames += 1
        
#Lidando com fps
        if cronometro_fps >= 1:  
            
            taxa_de_quadros = frames
            frames = cronometro_fps = 0

        chao.draw()
        
        
##B: MOVIMENTO DEBUGGER + CONE
        for i in range(quantidade):
            if (desconfiometro["pre_desc"] == False and tela_azul[i] == False and distraido[i] == False):
                debuggers[i], cones[i], debugger_vel[i] = movimento_debugger(debuggers[i], cones[i], debugger_direcao[i], debugger_vel[i], debugger_limite[i], desconfiometro, tela.delta_time())

            if (distraido[i] == True and encontro == False):
                debuggers[i], cones[i], debugger_vel[i], encontro = desvio_armadilha(debuggers[i], cones[i], esconderijo[alvo], debugger_direcao[i], debugger_vel[i], desconfiometro, tela.delta_time())
                
            if (distraido[i] == True and encontro == True):
                distraido[i], esconderijo_tempo, encontro = analise_esconderijo(debuggers[i], cones[i], esconderijo[alvo], debugger_direcao[i], debugger_vel[i], esconderijo_tempo)
                tela.draw_text("Esconderijo {:.0f} segundos".format(esconderijo_tempo), 70, 70, 30, (0,0,0))
                esconderijo_tempo -= tela.delta_time()
                
##B: DESCONFIOMETRO 
            if (tela_azul[i] == False and (False not in visibilidade) and desconfiometro["pre_desc"] == False and desconfiometro["desc"] == False):
            
            #ativa a contagem regressiva e troca pra sprite de desconfiometro
                if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])): 
                    desconfiometro["pre_desc"] = True
                    debuggers = debugger_alerta(quantidade, debuggers, debugger_vel, debugger_direcao)
                    
            if (desconfiometro["desc"] == True): #desconfiometro ativado
                    debugger_desconfiometro(desconfiometro, buggy, debuggers[i], cones[i], visibilidade, tela)
			
        if (desconfiometro["pre_desc"] == True and desconfiometro["pausa_timer"] > 0): #faz a contagem regressiva da pausa 
            tela.draw_text("Pausa {:.0f} segundos".format(desconfiometro["pausa_timer"]), 70, 70, 30, (0,0,0))
            desconfiometro["pausa_timer"] -= tela.delta_time()

        if (desconfiometro["pre_desc"] == True and desconfiometro["pausa_timer"] < 0): #ativa a contagem regressiva do desconfiometro
            desconfiometro["pre_desc"] = False
            desconfiometro["desc"] = True

                
	##BUGGY
        buggy, andou, virada_para = comportamento_buggy(buggy, tela.height/3 * tela.delta_time(), paredes, ponteiro_entrada, ponteiro_saída, esconderijo, tile, virada_para, disparo, teclado)


        ##B: ESCONDERIJO
        for i in range(qtd_esconderijos):
            if (buggy.collided(esconderijo[i])):
                visibilidade[i] = False
            else:
                visibilidade[i] = True

            if (buggy.collided(esconderijo[i]) and teclado.key_pressed("C")):
                alvo = i
                distraido[esconderijo_debugger[i]] = True                


        ##B: DISPARO e TELA AZUL
        if disparo["ativo"]: 
            movimento_disparo(disparo, tela)
            colide_disparo(disparo, debuggers, tela_azul, tela)
            
        if disparo["ativo"]: 
            disparo["imagem"].draw() #Só desenha se ele não colidiu
        else:
            disparo["tempo_esperado"] += tela.delta_time()
            
        for i in range(quantidade):
            if (tela_azul[i] == True and desconfiometro["desc"] == False): #B: só pode dar tela azul se desconfiometro=False
                tela.draw_text("Tela azul {:.0f} segundos".format(timer_tela_azul[i]), 70, 70, 30, (0,0,0))
                timer_tela_azul[i] -= tela.delta_time()
                debuggers[i] = debugger_tela_azul(debuggers[i], debugger_vel[i], debugger_direcao[i])
                
            if (timer_tela_azul[i] <= 0):
                tela_azul[i] = False
                timer_tela_azul[i] = 10
                debuggers[i] = debugger_normal(debuggers[i], debugger_vel[i], debugger_direcao[i], desconfiometro)






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

        #A: Faz a Buggy só exibir animação de caminhada quando ela está genuinamente caminhando
        if andou:
            buggy.update()
        buggy.draw()
        tela.draw_text(str(taxa_de_quadros), 0, 0, 40, (255,255,255))

        
        tela.update()
        
        


##B: todos os objetos que podem fazer o debugger mudar de direção
#colidiveis = []
#for parede in paredes:
#    for p in parede:
#        colidiveis.append(p) 
        
#for mecanismo in mecanismos:
#	for m in mecanismo:
#        colidiveis.append(m) 

