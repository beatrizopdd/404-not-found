from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from utilidades_visuais import *
from menu_fases import *


#Tela, teclado e mouse
tela = Window(1280, 660)
teclado = tela.get_keyboard()
mouse = tela.get_mouse()

tela.set_title("404 Not Found")

#Sons
som_startup = Sound("Assets/Audios/Efeitos/startup.ogg")
som_invalido = Sound("Assets/Audios/Efeitos/botão_esquisito.ogg")
som_desligando = Sound("Assets/Audios/Efeitos/desligando.ogg")

#Imagems
fundo = GameImage("Assets/Fundos/menu fundo.png")
menu = GameImage("Assets/Menu/menu_puro.png")

centralizar_na_tela(menu, tela)

#Botões
play = Sprite("Assets/Menu/play.png")
play_press = Sprite("Assets/Menu/play_press.png")

about = Sprite("Assets/Menu/about.png")
about_press = Sprite("Assets/Menu/about_press.png")

x = Sprite("Assets/Menu/x.png")
x_press = Sprite("Assets/Menu/x_press.png")

interrogação = Sprite("Assets/Menu/interrogacao.png")
interrogação_press = Sprite("Assets/Menu/interrogacao_press.png")

botões_principais = [play, about, interrogação, x]
botões_secundários = [play_press, about_press, interrogação_press, x_press]

#Colocando os botões no lugar
for b in botões_principais:
    centralizar(b, menu)

alinha_botões_vertical(botões_principais, menu, menu.height/1.5)

#O hardcode é feio, mas não valia fazer uma função só pra alinhas esses dois
#? e X estavam 15 pixels abaixo do topo do menu na imagem original
x.x = menu.x + menu.width - x.width - 8
interrogação.x = x.x - interrogação.width - 3
x.y = interrogação.y = (menu.y + 15)

for i in range(len(botões_secundários)):

    botões_secundários[i].set_position(botões_principais[i].x, botões_principais[i].y)
    botões_secundários[i].hide()


#Declarações genéricas
clickou_em = -1


som_startup.play()
while True:

    if teclado.key_pressed("ESC"):

        fechar_jogo(tela)

    #Procurando por clicks nos botões e mudando eles visualmente
    for i in range(len(botões_principais)):

        if mouse.is_over_object(botões_principais[i]) and mouse.is_button_pressed(1):

            botões_principais[i].hide()
            botões_secundários[i].unhide()

            clickou_em = i
        
        elif clickou_em != i:

            botões_principais[i].unhide()
            botões_secundários[i].hide()

    #Executando o comando relacionado ao botão quando o jogador solta o mouse
    if clickou_em != -1 and not mouse.is_button_pressed(1):

        if clickou_em == 0: #Se clickou em jogar

            #transição(tela)
            menu_fases(tela, teclado, mouse)


        if clickou_em == 1: #Se clickou em about

            som_invalido.play()

        if clickou_em == 2: #Se clickou na ?

            som_invalido.play()

        if clickou_em == 3: #Se clickou no X

            fechar_jogo(tela)

        clickou_em = -1


    #Desenhando coisas
    fundo.draw()
    menu.draw()

    for i in range(len(botões_secundários)):

        botões_secundários[i].draw()
        botões_principais[i].draw()


    tela.update()