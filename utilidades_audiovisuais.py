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
def transição(tela, duração=1):

    fundo_preto = GameImage("Assets/Fundos/fundo preto.png")
    fundo_preto.image.set_alpha(0)

    alpha = 0
    contador = 0

    while contador <= duração:

        alpha += tela.delta_time()/duração
        contador += tela.delta_time()

        fundo_preto.image.set_alpha(alpha * 255 / duração)
        fundo_preto.draw()

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

def transição_de_vitória(tela, audios):

    parar_soms(audios, 1000)
    transição(tela, 2)

    efeito = Sound("Assets/Audios/Efeitos/tadam.ogg")
    fundo = Sprite("Assets/Fundos/menu fundo.png")
    msg = Sprite("Assets/Menu/menu_vitoria.png", 2)
    msg.set_total_duration(1000)

    centralizar_na_tela(msg, tela)

    efeito.play()
    while True:

        if tela.get_keyboard().key_pressed("ESC"):

            fechar_jogo(tela)

        fundo.draw()

        msg.draw()
        msg.update()

        tela.update()

def game_over(tela, audios):

    parar_soms(audios, 1000)
    transição(tela, 2)

    efeito = Sound("Assets/Audios/Efeitos/tadam.ogg")
    fundo = Sprite("Assets/Fundos/menu fundo.png")
    x = 0

    efeito.play()
    while True:

        if tela.get_keyboard().key_pressed("ESC"):

            fechar_jogo(tela)

        x += tela.delta_time() * tela.width/10

        if x >= tela.width:

            x = -400

        fundo.draw()
        tela.draw_text("Corrigida :(", x, tela.height/2-20, 40, (255,255,255))

        tela.update()