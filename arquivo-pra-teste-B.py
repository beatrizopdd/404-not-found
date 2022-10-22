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
vel = [64,64]
direcao = ["v","h"]

qtd = 2

for d in debugger:
    d.set_sequence_time(0, 4, 400, True)

## B: FIM DO TESTE DE DEBUGGER

#descartaveis pq a gente tem função pra isso mas elas não são o foco aqui

debuggerV.set_position(70,70)
debuggerH.set_position(tela.width - 70 * 2,tela.height - 70 * 2) 

##B: PAREDES DE RASCUNHO PRA TESTE

pexE = GameImage("Assets/Paredes/pex-e.png")
pexE.set_position(0,0)

pexC = GameImage("Assets/Paredes/pex-c.png")
pexC.set_position((tela.width - pexC.width) / 2,0)

pexD = GameImage("Assets/Paredes/pex-d.png")
pexD.set_position(tela.width - pexD.width,0)

pexB = GameImage("Assets/Paredes/pex-b.png")
pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

parede = GameImage("Assets/Paredes/2X9.png")
parede.set_position(2 * 64, 7 * 66)

paredes = [parede,pexE,pexC,pexD,pexB]

##B: TERMINA PAREDES DE RASCUNHO PRA TESTE

while True:

    chao.draw()

    #B: range(quantidade-de-debuggers) // a meta aqui é que cada atributo possua o msm indice do seu debugger (struct pobre)
    #B: testa se é vertical ou horizontal
    	# linha de movimento
    	# testa se o debugger bateu na parede da lista de paredes // se bater a velocidade é multiplicada por -1
    
    for i in range(qtd):

        if (direcao[i] == "v"):
            debugger[i].y += vel[i] * tela.delta_time()
            
            for p in paredes:
            	vel[i] *= utilidadesB.limiteV(debugger[i], vel[i], p)
            	
        if (direcao[i] == "h"):
            debugger[i].x += vel[i] * tela.delta_time()

            for p in paredes:
            	vel[i] *= utilidadesB.limiteH(debugger[i], vel[i], p)
    	
    	
    for p in paredes:
    	p.draw()
    
    for d in debugger:
    	d.draw()
    	d.update()
    	

    tela.update()
    
    
    
    
    
    
    
    
    
    
    
    
########## RASCUNHOS ##########

##B: PAREDES DE RASCUNHO PRA TESTE

#pexE = GameImage("Assets/Paredes/pex-e.png")
#pexE.set_position(0,0)

#pexC = GameImage("Assets/Paredes/pex-c.png")
#pexC.set_position((tela.width - pexC.width) / 2,0)

#pexD = GameImage("Assets/Paredes/pex-d.png")
#pexD.set_position(tela.width - pexD.width,0)

#pexB = GameImage("Assets/Paredes/pex-b.png")
#pexB.set_position((tela.width - pexC.width) / 2, tela.height - pexB.height)

#parede = GameImage("Assets/Paredes/2X9.png")
#parede.set_position(2 * 64, 7 * 66)

#paredes = [parede,pexE,pexC,pexD,pexB]

##B: TERMINA PAREDES DE RASCUNHO PRA TESTE


