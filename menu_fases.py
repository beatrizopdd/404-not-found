from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from utilidades_visuais import *

def menu_fases(tela, teclado, mouse):

    #Sons
    som_startup = Sound("Assets/Audios/Efeitos/startup.ogg")
    som_invalido = Sound("Assets/Audios/Efeitos/botão_invalido.ogg")
    som_erro = Sound("Assets/Audios/Efeitos/erro.ogg")
    som_desligando = Sound("Assets/Audios/Efeitos/desligando.ogg")

    #Imagems
    menu = GameImage("Assets/Menu/menu_puro.png")

    #Botões

    fase1 = Sprite("Assets/Menu/x.png")
    fase1_press = Sprite("Assets/Menu/x_press.png")

    fase2 = Sprite("Assets/Menu/x.png")
    fase2_press = Sprite("Assets/Menu/x_press.png")

    fase3 = Sprite("Assets/Menu/x.png")
    fase3_press = Sprite("Assets/Menu/x_press.png")

    x = Sprite("Assets/Menu/x.png")
    x_press = Sprite("Assets/Menu/x_press.png")

    interrogação = Sprite("Assets/Menu/interrogacao.png")
    interrogação_press = Sprite("Assets/Menu/interrogacao_press.png")

    botões_principais = [fase1, fase2, fase3, interrogação, x]
    botões_secundários = [fase1_press, fase2_press, fase3_press, interrogação_press, x_press]

    #Colocando os botões no lugar
    for b in botões_principais:

        b.y = menu.y + 3 * menu.width/5

    alinha_botões_horizontal(botões_principais, menu, menu.width/6, 4)

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
    soltou_mouse = True


    while True:

        if teclado.key_pressed("ESC"):

            fechar_jogo(tela)

        #Procurando por clicks nos botões e mudando eles visualmente
        if mouse.is_over_object(menu):

            for i in range(len(botões_principais)):

                if mouse.is_over_object(botões_principais[i]) and mouse.is_button_pressed(1):

                    botões_principais[i].hide()
                    botões_secundários[i].unhide()

                    clickou_em = i
                
                elif clickou_em != i:

                    botões_principais[i].unhide()
                    botões_secundários[i].hide()
        

        #Lógica do som inválido quando clicka fora da janela
        if mouse.is_button_pressed(1) and not mouse.is_over_object(menu) and soltou_mouse:

            som_erro.play()
            soltou_mouse = False
        
        elif not mouse.is_button_pressed(1):

            soltou_mouse = True


        #Executando o comando relacionado ao botão quando o jogador solta o mouse
        if clickou_em != -1 and not mouse.is_button_pressed(1):

            if clickou_em == 0: #Se clickou na fase 1

                som_invalido.play()

            if clickou_em == 1: #Se clickou na fase 2

                som_invalido.play()

            if clickou_em == 2: #Se clickou na fase 3

                som_invalido.play()

            if clickou_em == 3: #Se clickou em ?

                som_invalido.play()

            if clickou_em == 4: #Se clickou no X

                return

            clickou_em = -1


        #Desenhando coisas
        menu.draw()

        for i in range(len(botões_secundários)):

            botões_secundários[i].draw()
            botões_principais[i].draw()


        tela.update()