from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from sys import *


#Transição simples de fadeout
#A tela fica preta exponenicialmente, mas não vou me dar ao trabalho de deixar linear, não vale a pena.
#Só é perceptível de 4 segundos pra cima. Ninguém vai usar mais que 2
def transição(tela, duração=1, manter_na_tela = []):

    fundo_preto = GameImage("Assets/Fundos/fundo preto.png")
    fundo_preto.image.set_alpha(0)

    alpha = 0
    contador = 0

    while contador <= duração:

        alpha += tela.delta_time()/duração
        contador += tela.delta_time()

        fundo_preto.image.set_alpha(alpha * 255 / duração)
        fundo_preto.draw()

        for objeto in manter_na_tela:
            objeto.draw()
        tela.update()

def centralizar_na_tela(objeto, tela):

    objeto.x = tela.width/2 - objeto.width/2
    objeto.y = tela.height/2 - objeto.height/2

def centralizar(objeto1, objeto2):

    objeto1.x = objeto2.x + objeto2.width/2 - objeto1.width/2
    objeto1.y = objeto2.y + objeto2.height/2 - objeto1.height/2


def alinha_botões_vertical(vet_botões, obj_base, margem, espaçamento=1.5):

    espaço_gasto = margem

    for botão in vet_botões:

        botão.y = obj_base.y + espaço_gasto
        espaço_gasto += botão.height * espaçamento

def alinha_botões_horizontal(vet_botões, obj_base, margem, espaçamento=1.5):

    espaço_gasto = margem

    for botão in vet_botões:

        botão.x = obj_base.x + espaço_gasto
        espaço_gasto += botão.width * espaçamento


def pausa(tela, teclado):

    menu_pausa = Sprite("Assets/Menu/menu_pausa2.png", 2)
    menu_pausa.set_total_duration(1000)

    centralizar_na_tela(menu_pausa, tela)

    input_acidental = True
    input_saida = False

    while True:

        if teclado.key_pressed("ESC"):

            input_saida = True

        if not teclado.key_pressed("ENTER"):

            input_acidental = False
        
        if input_saida:

            return True

        if not input_acidental and teclado.key_pressed("ENTER"):

            return False

        menu_pausa.draw()
        menu_pausa.update()

        tela.update()

def menu_controles(tela, teclado, mouse, audios):

    #Imagems
    menu = Sprite("Assets/Menu/menu_controles2.png", 17)
    menu.set_total_duration(14000)

    centralizar_na_tela(menu, tela)

    menu.x -= menu.width/12
    menu.y -= menu.height/12

    x = Sprite("Assets/Menu/x.png")
    x_press = Sprite("Assets/Menu/x_press.png")

    interrogação = Sprite("Assets/Menu/interrogacao.png")
    interrogação_press = Sprite("Assets/Menu/interrogacao_press.png")

    botões_principais = [interrogação, x]
    botões_secundários = [interrogação_press, x_press]

    #O hardcode é feio, mas não valia fazer uma função só pra alinhas esses dois
    #? e X estavam 15 pixels abaixo do topo do menu na imagem original
    x.x = menu.x + menu.width - x.width - 15
    interrogação.x = x.x - interrogação.width - 3
    x.y = interrogação.y = (menu.y + 15 + 5)

    for i in range(len(botões_secundários)):

        botões_secundários[i].set_position(botões_principais[i].x, botões_principais[i].y)
        botões_secundários[i].hide()


    #Declarações genéricas
    clickou_em = -1
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

            if clickou_em == 0: #Se clickou na ?

                audios["efeito_invalido"].play()

            if clickou_em == 1: #Se clickou no X

                return
        
            clickou_em = -1


        #Desenhando coisas
        menu.update()
        menu.draw()

        for i in range(len(botões_secundários)):

            botões_secundários[i].draw()
            botões_principais[i].draw()


        tela.update()
#Fechar o jogo coloca ele numa tela com o fundo do menu e faz um fadeout com um som
def fechar_jogo(tela):

    #Imagens
    fundo = GameImage("Assets/Fundos/menu fundo.png")

    fundo_preto = GameImage("Assets/Fundos/fundo preto.png")
    fundo_preto.image.set_alpha(0)

    #Sons
    som_desligar = Sound("Assets/Audios/Efeitos/desligando.ogg")
    som_desligar.play()

    #Declarações genéricas
    alpha = 1

    while som_desligar.is_playing():

        alpha += tela.delta_time() * 100

        fundo.draw()
        fundo_preto.image.set_alpha(alpha)
        fundo_preto.draw()

        tela.update()
    
    tela.close()

def parar_soms(audios, tempo=0):

    for k, som in audios.items():

        som.fadeout(tempo)

def animacao_gameover(tela, audios, buggy):
    
    transição(tela, 1, [buggy])

    #A: Como ele vai ser reinicializada depois, eu posso alterar a sequência sem desfazer
    frame = buggy.get_curr_frame()
    buggy.set_sequence(0, 19)

    audios["efeito_gameover"].play()

    timer = 0
    alpha = 255

    while audios["efeito_gameover"].is_playing():


        alpha -= 125 * tela.delta_time()
        timer += tela.delta_time()

        if timer >= 0.1:

            timer = 0
            frame += 5

            if frame >= 20:

                frame -= 20

        tela.set_background_color("BLACK")

        buggy.set_curr_frame(frame)
        buggy.image.set_alpha(alpha)
        buggy.draw()

        tela.update()

def transição_de_vitoria(tela, teclado, n_fase, audios):

    parar_soms(audios, 1000)

    transição(tela, 2)

    som = Sound("Assets/Audios/Efeitos/tadam.ogg")
    fundo = Sprite("Assets/Fundos/menu fundo.png")

    msg = Sprite("Assets/Menu/msg_vitoria.png", 2)
    msg.set_total_duration(1000)

    centralizar_na_tela(msg, tela)

    som.play()
    while True:

        if teclado.key_pressed("ESC"):

            return -1
        
        if teclado.key_pressed("ENTER"):

            return n_fase + 1


        fundo.draw()

        msg.draw()
        msg.update()

        tela.update()


def gameover(tela, teclado, buggy, n_fase, audios):

    parar_soms(audios, 1000)

    animacao_gameover(tela, audios, buggy)

    #Alterar os assets depois
    bgm = Sound("Assets/Audios/Bgms/gameover.ogg")
    fundo = Sprite("Assets/Fundos/fundo preto.png")
    msg = Sprite("Assets/Menu/msg_gameover.png", 2)
    msg.set_total_duration(1000)

    centralizar_na_tela(msg, tela)

    bgm.play()
    while True:

        if teclado.key_pressed("ESC"):

            bgm.fadeout(1500)
            return -1

        if teclado.key_pressed("ENTER"):

            bgm.fadeout(500)
            return n_fase

        fundo.draw()

        msg.draw()
        msg.update()

        tela.update()
