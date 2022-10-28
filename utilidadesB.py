# as chances da gente editar o msm arquivo ao msm tempo são menores assim rs
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

tela = Window(1280,660)

#B: adiciona o debugger na direção correspondente
def adiciona_debugger(quantidade, lista_vels, lista_direcoes):
	
	debuggers = []
	for i in range(quantidade):
	
		if (lista_direcoes[i] == "v" and lista_vels[i] > 0): #descendo
			sprite = Sprite("Assets/Inspetor/inspetor-vertical.png", 8)
			sprite.set_sequence(0, 4)
			
		elif (lista_direcoes[i] == "v" and lista_vels[i] < 0): #subindo
			sprite = Sprite("Assets/Inspetor/inspetor-vertical.png", 8)
			sprite.set_sequence(4, 8)
			
		elif (lista_direcoes[i] == "h" and lista_vels[i] > 0): #direita
			sprite = Sprite("Assets/Inspetor/inspetor-horizontal.png", 8)
			sprite.set_sequence(4, 8)
			
		elif (lista_direcoes[i] == "h" and lista_vels[i] < 0): #esquerda
			sprite = Sprite("Assets/Inspetor/inspetor-horizontal.png", 8)
			sprite.set_sequence(0, 4)
			
		sprite.set_total_duration(400)
		debuggers.append(sprite)
		
	return debuggers


#B: adiciona o cone na direção correspondente ao seu debugger
def adiciona_cone(vel, direcao):

	if (direcao == "v" and vel > 0): #descendo
		return GameImage("Assets/Cones de Visão/cone-visao-frente.png")
		
	elif (direcao == "v" and vel < 0): #subindo
		return GameImage("Assets/Cones de Visão/cone-visao-costas.png")
		
	elif (direcao == "h" and vel > 0): #direita
		return GameImage("Assets/Cones de Visão/cone-visao-direita.png")
		
	elif (direcao == "h" and vel < 0): #esquerda
		return GameImage("Assets/Cones de Visão/cone-visao-esquerda.png")
		
		
#B: posiciona o cone próximo ao seu debugger (é mais importante quando a velocidade troca de sinal)
def posiciona_cone(sprite, cone, vel, direcao):

	margem = 0

	if (direcao == "v" and vel > 0): #descendo
		cone.x = sprite.x + (sprite.width - cone.width) / 2
		cone.y = sprite.y + sprite.height + margem
		
	elif (direcao == "v" and vel < 0): #subindo
		cone.x = sprite.x + (sprite.width - cone.width) / 2
		cone.y = sprite.y - cone.height - margem
		
	elif (direcao == "h" and vel > 0): #direita
		cone.x = sprite.x + sprite.width + margem
		cone.y = sprite.y + (sprite.height - cone.height) / 2
		
	elif (direcao == "h" and vel < 0): #esquerda
		cone.x = sprite.x - cone.width - margem
		cone.y = sprite.y + (sprite.height - cone.height) / 2
		
		
#B: não deixa os debuggers colidirem com o cenário e trocam a sprite pra direção correspondente
def limitaV(sprite, vel, obstaculo):

	if (sprite.collided(obstaculo) and vel < 0): # encontrou subindo
		sprite.y -= vel  # posição = y - (-vel) = y + vel
		sprite.set_sequence_time(0, 4, 400, True) # chega olhando pra cima e troca pra baixo
		return -1
		
	elif (sprite.collided(obstaculo) and vel > 0): # encontrou descendo
		sprite.y -= vel # posição = y - vel
		sprite.set_sequence_time(4, 8, 400, True) # chega olhando pra baixo e troca pra cima
		return -1
		
	else:
		return 1
		
def limitaH(sprite, vel, obstaculo):
		
	if (sprite.collided(obstaculo) and vel < 0): # encontrou indo pra esquerda
		sprite.x -= vel
		sprite.set_sequence_time(4, 8, 400, True) # chega olhando pra esquerda e troca pra direita
		return -1
		
	elif (sprite.collided(obstaculo) and vel > 0): # encontrou indo pra direita
		sprite.x -= vel
		sprite.set_sequence_time(0, 4, 400, True) # chega olhando pra direita e troca pra esquerda
		return -1
		
	else:
		return 1

		
#B: troca o sprite do debugger pra versão desconfiômetro
def debugger_alerta(quantidade, lista_debuggers, lista_vels, lista_direcoes):
	
	debuggers = []
	for i in range(quantidade):
	
		if (lista_direcoes[i] == "v" and lista_vels[i] > 0): #descendo
			sprite = Sprite("Assets/Inspetor/inspetor-vertical-alerta.png", 8)
			sprite.set_sequence(0, 4)
			
		elif (lista_direcoes[i] == "v" and lista_vels[i] < 0): #subindo
			sprite = Sprite("Assets/Inspetor/inspetor-vertical-alerta.png", 8)
			sprite.set_sequence(4, 8)
			
		elif (lista_direcoes[i] == "h" and lista_vels[i] > 0): #direita
			sprite = Sprite("Assets/Inspetor/inspetor-horizontal-alerta.png", 8)
			sprite.set_sequence(4, 8)
			
		elif (lista_direcoes[i] == "h" and lista_vels[i] < 0): #esquerda
			sprite = Sprite("Assets/Inspetor/inspetor-horizontal-alerta.png", 8)
			sprite.set_sequence(0, 4)
			
		sprite.set_total_duration(400)
		sprite.x = lista_debuggers[i].x
		sprite.y = lista_debuggers[i].y
		debuggers.append(sprite)
		
	return debuggers
	
	
def cone_alerta(vel, direcao):

	if (direcao == "v" and vel > 0): #descendo
		return GameImage("Assets/Cones de Visão/cone-visao-frente-alerta.png")
		
	elif (direcao == "v" and vel < 0): #subindo
		return GameImage("Assets/Cones de Visão/cone-visao-costas-alerta.png")
		
	elif (direcao == "h" and vel > 0): #direita
		return GameImage("Assets/Cones de Visão/cone-visao-direita-alerta.png")
		
	elif (direcao == "h" and vel < 0): #esquerda
		return GameImage("Assets/Cones de Visão/cone-visao-esquerda-alerta.png")
	
	
#B: troca o sprite do debugger pra versão tela azul
def debugger_tela_azul(sprite, vel, direcao):
	
	if (direcao == "v" and vel > 0): #descendo
		sprite_TA = Sprite("Assets/Inspetor/inspetor-vertical-tazul.png", 8)
		sprite_TA.set_sequence(0, 4, True)
			
	elif (direcao == "v" and vel < 0): #subindo
		sprite_TA = Sprite("Assets/Inspetor/inspetor-vertical-tazul.png", 8)
		sprite_TA.set_sequence(4, 8, True)
			
	elif (direcao == "h" and vel > 0): #direita
		sprite_TA = Sprite("Assets/Inspetor/inspetor-horizontal-tazul.png", 8)
		sprite_TA.set_sequence(4, 8, True)
			
	elif (direcao == "h" and vel < 0): #esquerda
		sprite_TA = Sprite("Assets/Inspetor/inspetor-horizontal-tazul.png", 8)
		sprite_TA.set_sequence(0, 4, True)
			
	sprite_TA.set_total_duration(400)
	sprite_TA.x = sprite.x
	sprite_TA.y = sprite.y
		
	return sprite_TA	
	
	
def debugger_normal(sprite, vel, direcao, contato, alerta):
	
	#caso um debugger consiga pegar a buggy durante o tempo de tela azul então preciso garantir que ele fique na cor adequada
	if (contato == True or alerta == True):
		if (direcao == "v" and vel > 0): #descendo
			sprite_N = Sprite("Assets/Inspetor/inspetor-vertical-alerta.png", 8)
			sprite_N.set_sequence(0, 4, True)
				
		elif (direcao == "v" and vel < 0): #subindo
			sprite_N = Sprite("Assets/Inspetor/inspetor-vertical-alerta.png", 8)
			sprite_N.set_sequence(4, 8, True)
				
		elif (direcao == "h" and vel > 0): #direita
			sprite_N = Sprite("Assets/Inspetor/inspetor-horizontal-alerta.png", 8)
			sprite_N.set_sequence(4, 8, True)
				
		elif (direcao == "h" and vel < 0): #esquerda
			sprite_N = Sprite("Assets/Inspetor/inspetor-horizontal-alerta.png", 8)
			sprite_N.set_sequence(0, 4, True)
		
	else:
		if (direcao == "v" and vel > 0): #descendo
			sprite_N = Sprite("Assets/Inspetor/inspetor-vertical.png", 8)
			sprite_N.set_sequence(0, 4, True)
				
		elif (direcao == "v" and vel < 0): #subindo
			sprite_N = Sprite("Assets/Inspetor/inspetor-vertical.png", 8)
			sprite_N.set_sequence(4, 8, True)
				
		elif (direcao == "h" and vel > 0): #direita
			sprite_N = Sprite("Assets/Inspetor/inspetor-horizontal.png", 8)
			sprite_N.set_sequence(4, 8, True)
				
		elif (direcao == "h" and vel < 0): #esquerda
			sprite_N = Sprite("Assets/Inspetor/inspetor-horizontal.png", 8)
			sprite_N.set_sequence(0, 4, True)
		
			
	sprite_N.set_total_duration(400)
	sprite_N.x = sprite.x
	sprite_N.y = sprite.y
		
	return sprite_N
	
