from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from utilidades_audiovisuais import *
from fase1 import *
from fase2 import *

def menu_fases(tela, teclado, mouse, volume_padrao_bgm, audios):

    #Imagems
    menu = GameImage("Assets/Menu/open_file_dois_pontos.png")

    #Botões

    b_fase1 = Sprite("Assets/Menu/fase_1.png")
    b_fase1_press = Sprite("Assets/Menu/fase_1_press.png")

    b_fase2 = Sprite("Assets/Menu/fase_2.png")
    b_fase2_press = Sprite("Assets/Menu/fase_2_press.png")

    b_fase3 = Sprite("Assets/Menu/fase_3.png")
    b_fase3_press = Sprite("Assets/Menu/fase_3_press.png")

    x = Sprite("Assets/Menu/x.png")
    x_press = Sprite("Assets/Menu/x_press.png")

    interrogação = Sprite("Assets/Menu/interrogacao.png")
    interrogação_press = Sprite("Assets/Menu/interrogacao_press.png")

    botões_principais = [b_fase1, b_fase2, b_fase3, interrogação, x]
    botões_secundários = [b_fase1_press, b_fase2_press, b_fase3_press, interrogação_press, x_press]

    #Colocando os botões no lugar
    for b in botões_principais:

        b.y = menu.y + 3 * menu.width/8

    alinha_botões_horizontal(botões_principais, menu, menu.width/6, 3)

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
    prox_fase = 0
    soltou_mouse = True

    input_acidental = True
    while True:

        if teclado.key_pressed("ESC") and not input_acidental:

            return
        
        if not teclado.key_pressed("ESC"):

            input_acidental = False

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

            audios["efeito_erro"].play()
            soltou_mouse = False
        
        elif not mouse.is_button_pressed(1):

            soltou_mouse = True


        #Executando o comando relacionado ao botão quando o jogador solta o mouse
        if clickou_em != -1 and not mouse.is_button_pressed(1):

            if clickou_em == 0: #Se clickou na fase 1

                prox_fase = 1

            if clickou_em == 1: #Se clickou na fase 2

                prox_fase = 2

            if clickou_em == 2: #Se clickou na fase 3

                audios["efeito_invalido"].play()

            if clickou_em == 3: #Se clickou em ?

                audios["efeito_invalido"].play()

            if clickou_em == 4: #Se clickou no X

                return

            clickou_em = -1

        #Cada fase retorna -1 caso o player saia com ESC, o próprio número se ele continuar em caso de game over, ou o número da próxima caso ele ganhe.
        #prox_fase em 0 é um estado passivo

        #Para quando o jogador sai da fase com ESC ele não ter uma surpresa desgradável
        if prox_fase != 0:

            input_acidental = True

        while prox_fase == 1:

            prox_fase = fase1(tela, teclado, volume_padrao_bgm, audios, 1)

        while prox_fase == 2:

            prox_fase = fase2(tela, teclado, volume_padrao_bgm, audios, 2)

        while prox_fase == 3:

            prox_fase = fase1(tela, teclado, volume_padrao_bgm, audios, 3)

        if prox_fase == -1: #Se o player saiu com ESC

            return

        prox_fase = 0

        #Desenhando coisas
        menu.draw()

        for i in range(len(botões_secundários)):

            botões_secundários[i].draw()
            botões_principais[i].draw()


        tela.update()
