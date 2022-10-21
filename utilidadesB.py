# as chances da gente editar o msm arquivo ao msm tempo são menores assim rs
from PPlay.window import*
from PPlay.sprite import*

tela = Window(1280,660)

def movimento(sprite, vel, direcao):

	if (direcao == "v"):

		sprite.y += vel * tela.delta_time() 
		
	if (direcao == "h"):
	
		sprite.x += vel * tela.delta_time() 

def limite(sprite, vel, direcao):

	if (direcao == "v"):

		if (sprite.y <= 0):
			sprite.y = 0
			sprite.set_sequence(0, 4) #B: chega em cima e troca pra baixo
			return (-1)
			
			
		if (sprite.y >= tela.height - sprite.height):
			sprite.y = tela.height - sprite.height
			sprite.set_sequence(4, 8) #B: chega em baixo e troca pra cima
			return (-1)
		
	if (direcao == "h"):
		
		if (sprite.x <= 0):
			sprite.x = 0
			sprite.set_sequence(4, 8) #B: chega pra esquerda e troca pra direita
			return (-1)
			
		if (sprite.x >= tela.width - sprite.width):
			sprite.x = tela.width - sprite.width
			sprite.set_sequence(0, 4) #B: chega pra direita e troca pra esquerda
			return (-1) 
	
