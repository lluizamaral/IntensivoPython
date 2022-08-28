
bicicletas = ["trek""cannodale", "redline", "spacialized"]
print("\n")
print(bicicletas)
print("-----//-----")
#       ------//------      #


#     acessando um elemento especifico da lista    #

# ------com o metódo de espeficação do elemento (saí de modo print)
print(bicicletas[0].title())
print(bicicletas[-1].title())  # -----ultimo elemento a diante
print("\n")


#------------//-------------#

motos = []

motos.append("honda")
motos.append("yamaha")
motos.append("suzuki")
print(motos)



motos[0] = "ducati"             #---------LISTA ALTERADA COM UM NOVO valor ADICIONADO Á LISTA
print(motos)


#------------------//------------------#
print("-----------//----------\n")
exemplo = ["CbGANG","High","SantaCruz"]
exemplo.insert(0,"WoodLight")                         #-----ADICIOUNOU UM VALOR NA POSIÇAO 0 SEM 
print(exemplo)                                                   #-|SOBREPOR O VALOR ORIGINAL.  


print("----------//----------")


veificados_de_um_por_um = ["pedro","rojer","lucas","morales","caio"]

ativo = True
while ativo:
    for verificado in veificados_de_um_por_um:
        del veificados_de_um_por_um[0]                   #---------deletando 1 por 1 da lista com o delete,mas sempre começando pelo primeiro valor
        print(veificados_de_um_por_um)
    else:
        ativo = False

print("---------//---------")

lista = ["coisa1","coisa2","coisa3","coisa4"]
lista.sort()
print(lista)


print(lista.pop())
    # ou #                                              #----pode ser usado tanto para excluir o ultimo item da lista mas como tambem pode ser usado um laço FOR
print(lista.pop())                                               #-| para mover todos os itens popados para uma lista.




#------------//------------#
print("--------//------\n")


nomes = []
nomes.append("fernando")
nomes.append("igor")
nomes.append("bruno")
nomes.append("alisson")
nomes.sort()                  #------ALTERA A FORMA DE ORGANIZAÇÃO DA LISTA DE FORMA PERMANENTE    

print(nomes)

#-----------\\------------#
nomes_02 = []
nomes_02.append("fernando")
nomes_02.append("igor")
nomes_02.append("bruno")
nomes_02.append("alisson")



print("\n\tLista Original")

print(nomes_02)

print("\n\tAqui está a lista de forma organizada QUANDO chamada")


print(sorted(nomes_02))                              #------valor organizado QUANDO chamado.

#---------\\---------#
print("------//------")
print("\n\tcomando len para contar a quantidade q há na lista")
print(len(bicicletas))