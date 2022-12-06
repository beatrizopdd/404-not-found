from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

from buggy import *
from utilidades_grid import *

from utilidadesB import *

#A: Tela
tela = Window(1280,660)
tela.set_title("404 Not Found")
teclado = tela.get_keyboard()

#A: Audios

volume_padrao_bgm = 40

bgm_normal = Sound("Assets/Audios/Bgms/Up In My Jam.ogg")
bgm_normal.set_volume(volume_padrao_bgm)
bgm_normal.set_repeat(True)

efeito_disparo = Sound("Assets/Audios/Efeitos/choque1.ogg")
efeito_tela_azul = Sound("Assets/Audios/Efeitos/desligando.ogg")
efeito_ponteiro = Sound("Assets/Audios/Efeitos/teleporte2.ogg")

efeito_erro = Sound("Assets/Audios/Efeitos/erro.ogg")

audios = {
    "bgm_normal": bgm_normal,
    "efeito_disparo": efeito_disparo,
    "efeito_tela_azul": efeito_tela_azul,
    "efeito_ponteiro": efeito_ponteiro,
    "efeito_erro": efeito_erro
}

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
paredes_internas = [parede1X2, parede1X3, parede4X1, parede_unica]


##B: DEBUGGER e CONE
quantidade = 8
debugger_direcao = ["v", "v", "v", "v", "v", "h", "h", "h"]

debugger_vel = []
for i in range(quantidade):
	debugger_vel.append(50)

debuggers = adiciona_debugger(quantidade, debugger_vel, debugger_direcao)

unX = tile.width
unY = tile.height
debugger_limite = [[unY, unY * 7], [unY, unY * 7], [unY * 4, unY * 6], [unY, unY * 6], [unY, unY * 6], [unX, unX * 7], [unX * 9, unX * 18], [unX * 9, unX * 18]]

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
	

#109#


##A: Sprite e variáveis da Buggy
buggy = Sprite("Assets/Buggy/buggy.png", 20)
buggy.set_sequence(0,4)
virada_para = "BAIXO"
andou = False
atirou = False

buggy.set_total_duration(850)
posiciona_grid(buggy, tile, 1,1)

#124#

##B: DESCONFIOMETRO
desconfiometro = {
    "pausa": False,
    "pausa_timer": 10,
    "ativo": False,
    "limite": 10,
}


##A: PONTEIROS
ponteiro_entrada = [Sprite("Assets/Mecanismos/&w.png", 6)]
ponteiro_entrada[0].set_total_duration(400)
posiciona_grid(ponteiro_entrada[0], tile, 4, 8)

ponteiro_saída = [Sprite("Assets/Mecanismos/W.png", 13)]
ponteiro_saída[0].set_total_duration(1000)
posiciona_grid(ponteiro_saída[0], tile, 9, 1)

ponteiros = [ponteiro_entrada, ponteiro_saída]


#A: Dicionário com as informações do disparo
disparo = {
    "imagem": GameImage("Assets/Choque/choque-vertical.png"),
    "direção": "CIMA",
    "velocidade": tela.height/2,
    "tempo_esperado": 0,
    "recarga": 6,
    "ativo": False,
}


##B: TELA AZUL
tempo_max_tela_azul = 5
timer_tela_azul = []
tela_azul = []
for i in range(quantidade):
	timer_tela_azul.append(tempo_max_tela_azul)
	tela_azul.append(False)


#A: Pro nosso controle de fps
cronometro_fps = 0
frames = 0
taxa_de_quadros = 0

##A: Elementos da interface do jogo

carinhas = Sprite("Assets/Interface/carinhas.png", 3)
barra_choque = Sprite("Assets/Interface/barra_raio.png", 6)
barra_tela_azul = Sprite("Assets/Interface/barra_ta.png", 6)

elementos_iu = [carinhas, barra_choque, barra_tela_azul]
for elemento in elementos_iu:
    elemento.set_total_duration(1)

barra_choque.y = carinhas.y + carinhas.height
barra_tela_azul.y = barra_choque.y + barra_choque.height

#Contadores para os elementos da interface
iu_choque = 0
iu_tela_azul = tempo_max_tela_azul
frame_barra_choque = 0
frame_barra_ta = 5

#A: Entrada e saída do nível
entrada = Sprite("Assets/Mecanismos/hide.png", 22)
saida = Sprite("Assets/Mecanismos/hide.png", 22)
nuvens = [entrada, saida]

for n in nuvens:
    n.set_total_duration(2500)

posiciona_grid(entrada, tile, 1, 0.5)
posiciona_grid(saida, tile, 18, 8)

#Para o menu de pausa
input_acidental = False


bgm_normal.play()
while True:

    if teclado.key_pressed("ESC") and not input_acidental:

        input_acidental = True
        audios["efeito_erro"].play()
        audios["bgm_normal"].set_volume(volume_padrao_bgm/2)

        pausa(tela, teclado)

        audios["bgm_normal"].set_volume(volume_padrao_bgm)

    if not teclado.key_pressed("ESC"):

        input_acidental = False

#Lidando com fps
    cronometro_fps += tela.delta_time()
    frames += 1
    if cronometro_fps >= 1:
        taxa_de_quadros = frames
        frames = cronometro_fps = 0


##BUGGY
    buggy, andou, atirou, virada_para = comportamento_buggy(buggy, tela.height/3.5 * tela.delta_time(), paredes_internas, ponteiro_entrada, ponteiro_saída, tile, virada_para, disparo, teclado, saida, audios, tela)

##A: DISPARO
    if disparo["ativo"]: 
        movimento_disparo(disparo, tela)
        colide_disparo(disparo, debuggers, tela_azul, audios, tela)
        
        if disparo["ativo"]:  #Só desenha se ele não colidiu
            disparo["imagem"].draw()
        
    else:
        disparo["tempo_esperado"] += tela.delta_time()
        

    #212#
               
    
##B: MOVIMENTO DEBUGGER + CONE
    for i in range(quantidade):
    
        if (tela_azul[i] == False and desconfiometro["pausa"] == False):
            debuggers[i], cones[i], debugger_vel[i] = movimento_debugger(debuggers[i], cones[i], debugger_direcao[i], debugger_vel[i], debugger_limite[i], desconfiometro, tela)


##B: TELA AZUL
        if (tela_azul[i] == True): #ATIVA o modo tela azul
            debuggers[i] = debugger_tela_azul(debuggers[i], debugger_vel[i], debugger_direcao[i])

            #print("Tela azul {:.0f} segundos".format(timer_tela_azul[i]))
            timer_tela_azul[i] -= tela.delta_time()

            if (timer_tela_azul[i] <= 0):
                tela_azul[i] = False
                timer_tela_azul[i] = tempo_max_tela_azul
                debuggers[i] = debugger_normal(debuggers[i], debugger_vel[i], debugger_direcao[i], desconfiometro)


        #241#


##B: DESCONFIOMETRO pt.1
        if (tela_azul[i] == False and desconfiometro["pausa"] == False and desconfiometro["ativo"] == False):
        
            if (buggy.collided(debuggers[i]) or buggy.collided(cones[i])): #ATIVA contagem regressiva e TROCA sprite
                desconfiometro["pausa"] = True
                debuggers = debugger_alerta(quantidade, debuggers, debugger_vel, debugger_direcao)

                for i in range(quantidade):
                    cones[i] = cone_alerta(debugger_vel[i], debugger_direcao[i])
                    posiciona_cone(cones[i], debuggers[i], debugger_vel[i], debugger_direcao[i])

        if (desconfiometro["ativo"] == True and desconfiometro["limite"] > 0): #FAZ a contagem regressiva
            #print("Desconfiometro {:.0f} segundos".format(desconfiometro["limite"]))  

            if (buggy.collided(cones[i])):
                desconfiometro["limite"] -= tela.delta_time()
                
            if (buggy.collided(debuggers[i])):
                desconfiometro["limite"] = 0

        if (desconfiometro["limite"] <= 0):
            #print("GAME OVER")
            pass    


##B: DESCONFIOMETRO pt.2                              
    if (desconfiometro["pausa"] == True): 

        if (desconfiometro["pausa_timer"] > 0): #REALIZA contagem regressiva
            #print("Pausa {:.0f} segundos".format(desconfiometro["pausa_timer"]))
            desconfiometro["pausa_timer"] -= tela.delta_time()

        else: #TERMINA a contagem regressiva
            desconfiometro["pausa"] = False
            desconfiometro["ativo"] = True

##A: Controlando os sons

    #if not bgm_normal.is_playing():
    #    bgm_normal.play()

##A: Lógica dos elementos da interface

    if disparo["ativo"]:

        frame_barra_choque = iu_choque = 0
    
    else:

        iu_choque += tela.delta_time()

        if iu_choque >= disparo["recarga"]/4 * frame_barra_choque and frame_barra_choque < 5:

            frame_barra_choque += 1


    if not (True in tela_azul):

        frame_barra_ta = iu_tela_azul = tempo_max_tela_azul
    
    else:

        iu_tela_azul -= tela.delta_time()

        if iu_tela_azul <= tempo_max_tela_azul/5 * frame_barra_ta and frame_barra_ta > 0:

            frame_barra_ta -= 1

    barra_choque.set_curr_frame(frame_barra_choque)
    barra_tela_azul.set_curr_frame(frame_barra_ta)

    if desconfiometro["ativo"]:

        carinhas.set_curr_frame(2)
    
    elif desconfiometro["pausa"]:

        carinhas.set_curr_frame(1)
    
    else:

        carinhas.set_curr_frame(0)

##B: DESENHOS

    chao.draw()

    for ponteiro in ponteiros:
        for p in ponteiro:
            p.draw()
            p.update()

    for parede in paredes:
        for p in parede:
            p.draw()

    for n in nuvens:
        n.draw()
        n.update()

    for c in cones:
        c.draw()

    if disparo["ativo"]:
        disparo["imagem"].draw()

    for d in debuggers:
        d.draw()
        d.update()


    #A: Faz a Buggy só exibir animação de caminhada quando ela está genuinamente caminhando
    if andou:
        buggy.update()
    buggy.draw()

    for e in elementos_iu:
        e.draw()
    
    #print(taxa_de_quadros)
        
    tela.update()
    
    

