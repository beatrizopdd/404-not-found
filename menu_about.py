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

#Reciclado do menu de fases
def menu_about(tela, teclado, mouse, volume_padrao_bgm, audios):

    #Imagems
    menu = Sprite("Assets/Menu/creditos.png", 6)
    menu.set_total_duration(1)
    
    centralizar_na_tela(menu, tela)

    menu.x += menu.width/15
    menu.y -= menu.height/15

    #Botões

    seta_di = Sprite("Assets/Menu/seta_di.png")
    seta_di_press = Sprite("Assets/Menu/seta_di_press.png")

    seta_es = Sprite("Assets/Menu/seta_es.png")
    seta_es_press = Sprite("Assets/Menu/seta_es_press.png")

    x = Sprite("Assets/Menu/x.png")
    x_press = Sprite("Assets/Menu/x_press.png")

    interrogação = Sprite("Assets/Menu/interrogacao.png")
    interrogação_press = Sprite("Assets/Menu/interrogacao_press.png")

    botões_principais = [seta_es, seta_di, interrogação, x]
    botões_secundários = [seta_es_press, seta_di_press, interrogação_press, x_press]

    #Colocando os botões no lugar
    for b in botões_principais:

        b.y = menu.y + 3 * menu.width/8

    #E vamos de hardcode
    seta_es.x = menu.x + 15
    seta_es.y = menu.y + menu.height - seta_es.height - 25

    seta_di.x = menu.x + menu.width - seta_di.width - 15
    seta_di.y = menu.y + menu.height - seta_di.height - 25

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
    pagina = 0

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

            if clickou_em == 0: #Se clickou na seta esquerda

                pagina -= 1

            if clickou_em == 1: #Se clickou na seta direita

                pagina += 1

            if clickou_em == 2: #Se clickou na ?

                audios["efeito_invalido"].play()

            if clickou_em == 3: #Se clickou no x

                return

            clickou_em = -1

        #Desenhando coisas

        pagina = abs(pagina % 6)

        menu.set_curr_frame(pagina)
        menu.draw()

        for i in range(len(botões_secundários)):

            botões_secundários[i].draw()
            botões_principais[i].draw()


        tela.update()
