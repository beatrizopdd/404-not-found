from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.sound import *
from utilidades_visuais import *


#Tela, teclado e mouse
tela = Window(1260, 660)
teclado = tela.get_keyboard()
mouse = tela.get_mouse()

tela.set_title("404 Not Found")

#GameImages
fundo = GameImage("Assets/Fundos/menu fundo.png")
menu = GameImage("Assets/Menu/menu.png")
play_pressed = GameImage("Assets/Menu/play_press.png")
about_pressed = GameImage("Assets/Menu/about_press.png")

botões = [play_pressed, about_pressed]

centralizar_na_tela(menu, tela)

while True:

    fundo.draw()
    menu.draw()

    for i in botões:
        i.draw()

    tela.update()