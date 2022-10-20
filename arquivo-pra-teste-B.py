from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

#A: Tela
tela = Window(1280,660)
tela.set_title("404 Not Found")

#A: Game Images | Todas as imagens de fundo
chao = GameImage("Assets/Fundos/chao.png")
tile = GameImage("Assets/Fundos/tile.png") #Declarado só pelo uso na função posiciona_grid


while True:

    chao.draw()
    
    

    tela.update()
    
    
    
    
    
    
    
    
    
    
    
    
########## RASCUNHOS ##########

##B: TESTE DE CORTE DE PAREDE

#pexE = GameImage("Assets/Paredes/pex_e.png")
#pexE.set_position(0,0)

#pexC = GameImage("Assets/Paredes/pex_c.png")
#pexC.set_position((tela.width - pexC.width) / 2,0)

#pexD = GameImage("Assets/Paredes/pex_d.png")
#pexD.set_position(tela.width - pexD.width,0)

#pexB = GameImage("Assets/Paredes/pex_b.png")
#pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

#paredes = [pexE,pexC,pexD,pexB]

	#for p in paredes:
    	#p.draw()

##B: TERMINA TESTE DE CORTE DE PAREDE
