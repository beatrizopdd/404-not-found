def transição():
    pass

#Coloca o objeto 1 no centro do objeto 2
def centralizar_na_tela(objeto1, tela):

    objeto1.x = tela.width/2 - objeto1.width/2
    objeto1.y = tela.height/2 - objeto1.height/2

def alinha_botões(vet_botões, obj_base, margem, espaçamento=1.5):

    espaço_gasto = margem

    for botão in vet_botões:

        botão.x = obj_base.x + obj_base.width/2 - botão.width/2

        botão.y = obj_base.y + espaço_gasto

        espaço_gasto += botão.height * espaçamento