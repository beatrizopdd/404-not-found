# as chances da gente editar o msm arquivo ao msm tempo são menores assim rs
from PPlay.window import*
from PPlay.sprite import*

tela = Window(1280,660)

def limiteV(sprite, vel, obstaculo):

	if (sprite.collided(obstaculo) and vel < 0): # encontrou subindo
		sprite.y -= vel  # posição = y - (-vel) = y + vel
		sprite.set_sequence_time(0, 4, 400, True) #B: chega olhando pra cima e troca pra baixo
		return -1
		
	elif (sprite.collided(obstaculo) and vel > 0): # encontrou descendo
		sprite.y -= vel # posição = y - vel
		sprite.set_sequence_time(4, 8, 400, True) #B: chega olhando pra baixo e troca pra cima
		return -1
		
	else:
		return 1
		
def limiteH(sprite, vel, obstaculo):
		
	if (sprite.collided(obstaculo) and vel < 0): # encontrou indo pra esquerda
		sprite.x -= vel
		sprite.set_sequence_time(4, 8, 400, True) #B: chega olhando pra esquerda e troca pra direita
		return -1
		
	elif (sprite.collided(obstaculo) and vel > 0): # encontrou indo pra direita
		sprite.x -= vel
		sprite.set_sequence_time(0, 4, 400, True) #B: chega olhando pra direita e troca pra esquerda
		return -1
		
	else:
		return 1
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#meu protótipo de limite batendo na borda deu muito trabalho então vou salvar aqui no finalzinho
def pLimiteBorda1(sprite, vel):

	if (sprite.y <= 0):
		sprite.y = 0
		sprite.set_sequence_time(0, 4, 400, True) #B: chega olhando pra cima e troca pra baixo
		return -1
		
	elif (sprite.y >= tela.height - sprite.height):
		sprite.y = tela.height - sprite.height
		sprite.set_sequence_time(4, 8, 400, True) #B: chega olhando pra baixo e troca pra cima
		return -1
		
	else:
		return 1
		
def pLimiteBorda2(sprite, vel):
		
	if (sprite.x <= 0):
		sprite.x = 0
		sprite.set_sequence_time(4, 8, 400, True) #B: chega olhando pra esquerda e troca pra direita
		return -1
		
	elif (sprite.x >= tela.width - sprite.width):
		sprite.x = tela.width - sprite.width
		sprite.set_sequence_time(0, 4, 400, True) #B: chega olhando pra direita e troca pra esquerda
		return -1
		
	else:
		return 1
	
