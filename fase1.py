from PPlay import gameimage
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *

from buggy import *
from utilidadesA import *

#A: Tela
tela = Window(1280,660)
teclado = tela.get_keyboard()
tela.set_title("404 Not Found")

#A: Audios
bgm_normal = Sound("Assets/Audio/Bgms/Ayra.ogg")

#A: Game Images | Todas as imagens de fundo e o disparo
chao = GameImage("Assets/Fundos/chao.png")
tile = Sprite("Assets/Fundos/tile.png") #Declarado só pelo uso na função posiciona_grid
parede_externa = GameImage("Assets/Paredes/moldura_com_es.png")

##B: COMEÇA SEÇÃO DE PAREDES

#A: Paredes A3 D1 e D2, nessa ordem
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

##B: TERMINA SEÇÃO DE PAREDES


##A: Sprites | Tudo que tem alguma animação envolvida

#A: Sprite e variáveis da Buggy

buggy = Sprite("Assets/Buggy/buggy-vertical.png", 10)
buggy.set_sequence(0,4)
virada_para = "BAIXO"
andou = False
buggy.set_total_duration(500)
posiciona_grid(buggy, tile, 1,1)

##B: COMEÇA SEÇÃO DE INIMIGOS

#A: Inicializando os debuggers
debugger = []
for i in range(8):
	debugger.append(Sprite("Assets/Inspetor/inspetor-frente.png", 4))

tela_azul = []
for i in debugger:
    tela_azul.append(False)

#A: Ajustando para as sprites iniciais corretas.
debugger[1] = Sprite("Assets/Inspetor/inspetor-costas.png", 4)
debugger[2] = Sprite("Assets/Inspetor/inspetor-esquerda.png", 4)
debugger[4] = Sprite("Assets/Inspetor/inspetor-direita.png", 4)
debugger[6] = Sprite("Assets/Inspetor/inspetor-costas.png", 4)
debugger[7] = Sprite("Assets/Inspetor/inspetor-esquerda.png", 4)

#B: atualizando o set_total_duration
for d in debugger:
    d.set_total_duration(500)

#A: Colando os debuggers nas suas posições iniciais
posiciona_grid(debugger[0], tile, 1,2)
posiciona_grid(debugger[1], tile, 6,6)
posiciona_grid(debugger[2], tile, 7,7)
posiciona_grid(debugger[3], tile, 10,4)
posiciona_grid(debugger[4], tile, 12,6)
posiciona_grid(debugger[5], tile, 14,3)
posiciona_grid(debugger[6], tile, 17,5)
posiciona_grid(debugger[7], tile, 18,2)

#A: Inicializando todos os cones de visão dos debuggers
cone = []
for i in range(8):
    cone.append(GameImage("Assets/Cones de Visão/cone-visao-frente.png"))

#A: Ajustando para as imagens corretas
cone[1] = GameImage("Assets/Cones de Visão/cone-visao-costas.png")
cone[2] = GameImage("Assets/Cones de Visão/cone-visao-esquerda.png")
cone[4] = GameImage("Assets/Cones de Visão/cone-visao-direita.png")
cone[6] = GameImage("Assets/Cones de Visão/cone-visao-costas.png")
cone[7] = GameImage("Assets/Cones de Visão/cone-visao-esquerda.png")

#A: Associando os cones aos seus devidos debuggers e fazendo o alinhamento
for i in (0,3,5):
    alinha_cone(cone[i], debugger[i], 4)

for i in (1,6):
    alinha_cone(cone[i], debugger[i], 2)

for i in (2,7):
    alinha_cone(cone[i], debugger[i], 1)

alinha_cone(cone[4], debugger[4], 3)

##B: TERMINA SEÇÃO DE INIMIGOS

##B: COMEÇA SEÇÃO DE MECANISMOS

esconderijo = [Sprite("Assets/Mecanismos/hide.png", 22)]
esconderijo[0].set_total_duration(2500)
posiciona_grid(esconderijo[0], tile, 1,7)

#A: Comentado pra caso alguma das suas funções explodir a gente poder discutir e arrumar
'''esconderijo = Sprite("Assets/Mecanismos/hide.png", 22)
esconderijo.set_total_duration(2500)
posiciona_grid(esconderijo, tile, 1,7)'''

ponteiro_entrada = [Sprite("Assets/Mecanismos/&w.png", 6)]
ponteiro_entrada[0].set_total_duration(400)
posiciona_grid(ponteiro_entrada[0], tile, 4, 8)

ponteiro_saída = [Sprite("Assets/Mecanismos/W.png", 13)]
ponteiro_saída[0].set_total_duration(1000)
posiciona_grid(ponteiro_saída[0], tile, 9, 1)

ponteiros = [ponteiro_entrada, ponteiro_saída]

#A: Vetor com todos os mecanismos
mecanismos = [esconderijo, ponteiro_entrada, ponteiro_saída]

##B: TERMINA SEÇÃO DE MECANISMOS

#A: Vetores para facilitar os processo de desenho
#A: O cone de visão precisa ser desenhado por último e sem .update(), então fica fora dos vetores
paredes = [parede1X2, parede1X3, parede4X1, parede_unica]

#A: Pro nosso controle de fps
cronometro_fps = 0
frames = 0
taxa_de_quadros = 0

#A: Dicionário com as informações do disparo
disparo = {

    "imagem": GameImage("Assets/Choque/choque-vertical.png"),
    "direção": "CIMA",
    "velocidade": tela.height/2,
    "tempo_esperado": 0,
    "recarga": 3,
    "ativo": False,
}

while True:

    cronometro_fps += tela.delta_time()
    frames += 1
    
    #Lidando com fps
    if cronometro_fps >= 1:  
        
        taxa_de_quadros = frames
        frames = cronometro_fps = 0
        print("X: " + str(buggy.x) + " Y: " + str(buggy.y))
        print(virada_para)

    ##A: LIDANDO COM SONS
    #bgm_normal.play()

    ##A: DESENHANDO OBJETOS NA TELA
    chao.draw()
    parede_externa.draw()

    tela.draw_text(str(taxa_de_quadros), 0, 0, 40, (255,255,255))

    #B: desenha as paredes internas
    for i in paredes:
        for parede in i:
            parede.draw()

    buggy, andou, virada_para = comportamento_buggy(buggy, tela.height/3 * tela.delta_time(), paredes, ponteiro_entrada, ponteiro_saída, esconderijo, tile, virada_para, disparo, teclado)


    if disparo["ativo"]:

        movimento_disparo(disparo, tela)
        colide_disparo(disparo, debugger, tela_azul, tela)

        if disparo["ativo"]: #Só desenha se ele não colidir 

            disparo["imagem"].draw()
    
    else:

        disparo["tempo_esperado"] += tela.delta_time()

    for vet_p in ponteiros:
        for p in vet_p:
            p.update()
            p.draw()

    #A: Faz a Buggy só exibir animação de caminhada quando ela está genuinamente caminhando
    if andou:
        buggy.update()
    buggy.draw()

    for e in esconderijo:
        e.update()
        e.draw()

    for d in debugger:
        d.update()
        d.draw()

    for i in cone:
        i.draw()

    tela.update()
