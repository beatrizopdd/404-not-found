#A: Retorna as coordenadas da tela equivalentes ao x e y dentro do grid de tiles
def cord_grid(tile, x, y):

    x = tile.x * x
    y = tile.y * y

    return x,y

#A: Alterei a função pra gente poder escolher se vai centralizar ou não o objeto no quadrado que ele entra
def posiciona_grid(objeto, tile, x, y, centraliza=True):

    objeto.set_position(tile.width*x, tile.height*y)
    if centraliza:

        errox = tile.width/2 - objeto.width/2
        erroy = tile.height/2 - objeto.height/2

        objeto.x += errox
        objeto.y += erroy


#A: Alinha os cones de visão baseado em pra que lado o debugger está olhando
# 1- Esquerda  2- Cima  3- Direita  4- Baixo, conforme a gente combinou
#A: Obsoleta. Verificar melhor depois
def alinha_cone(cone, debugger, lado):

    X = debugger.x + (debugger.width/2 - cone.width/2)
    Y = debugger.y + (debugger.height/2 - cone.height/2)

    if lado == 1:

        X -= debugger.width*1.2
    
    elif lado == 2:

        Y -= debugger.height

    elif lado == 3:

        X += debugger.width*1.2
    
    elif lado == 4:

        Y += debugger.height
    
    cone.set_position(X,Y)

#A: dist_pontos espera duas tuplas/listas com x e y
def dist_pontos(cords1, cords2):

    dist = ((((cords1[0] - cords2[0])**2) + ((cords1[1] - cords2[1])**2))**0.5)

    return dist
