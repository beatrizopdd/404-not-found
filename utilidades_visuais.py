from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from sys import *


def transição():
    pass

def centralizar_na_tela(objeto1, tela):

    objeto1.x = tela.width/2 - objeto1.width/2
    objeto1.y = tela.height/2 - objeto1.height/2


def alinha_botões(vet_botões, obj_base, margem, espaçamento=1.5):

    espaço_gasto = margem

    for botão in vet_botões:

        botão.x = obj_base.x + obj_base.width/2 - botão.width/2

        botão.y = obj_base.y + espaço_gasto

        espaço_gasto += botão.height * espaçamento


def pausa(tela, teclado):

    while True:

        
        if teclado.key_pressed("ENTER"):

            return

        tela.set_background_color("BLACK")
        tela.draw_text("Pausado", tela.width/2-140, tela.height/2-20, 40, (255,255,255))
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
    alpha = 0

    while som_desligar.is_playing():

        alpha += tela.delta_time() * 100

        fundo.draw()
        fundo_preto.image.set_alpha(alpha)
        fundo_preto.draw()

        tela.update()
    
    tela.close()

def transição_de_vitória(tela):

    fundo = Sprite("Assets/Fundos/menu fundo.png")
    x = 0

    while True:

        if tela.get_keyboard().key_pressed("ESC"):

            fechar_jogo(tela)

        x += tela.delta_time() * tela.width/10

        if x >= tela.width:

            x = -400

        fundo.draw()
        tela.draw_text("Fase 1 concluída!", x, tela.height/2-20, 40, (255,255,255))

        tela.update()