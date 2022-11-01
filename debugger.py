from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

#B: funçoes de troca de sprite

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
	
