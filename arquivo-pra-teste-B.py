from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import utilidadesB

#A: Tela
tela = Window(1280,660)
tela.set_title("404 Not Found")

#A: Game Images | Todas as imagens de fundo
chao = GameImage("Assets/Fundos/chao.png")
tile = GameImage("Assets/Fundos/tile.png") #Declarado só pelo uso na função posiciona_grid


## B: TESTE DE DEBUGGER

debuggerV = Sprite("Assets/Inspetor/inspetor-vertical.png", 8)
debuggerH = Sprite("Assets/Inspetor/inspetor-horizontal.png", 8)

debugger = [debuggerV,debuggerH]
orientacao = ["v","h"]
vel = [100,95]

for d in debugger:
    d.set_sequence_time(0, 4, 400, True)
    
#descartaveis
debuggerV.set_position(0,0)
debuggerH.set_position(tela.width - debuggerH.width,tela.height - 64) #chutei o balde nesse 64 aqui

## B: FIM DO TESTE DE DEBUGGER


while True:

    chao.draw()
    
    #B: parei aqui o boneco não anda beatriz favor resolver
    i = 0
    for d in debugger:
    if (orientacao[i] == "v"):
		d.y += vel[i] * tela.delta_time() 
	if (orientacao[i] == "h"):
		d.x += vel[i] * tela.delta_time()

    	#utilidadesB.movimento(d, vel[i], orientacao[i])
    	#vel[d] *= utilidadesB.limite(debugger[d], vel[d], orientacao[d])
    	i += 1
    
    for d in debugger:
    	d.draw()
    	d.update()

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
