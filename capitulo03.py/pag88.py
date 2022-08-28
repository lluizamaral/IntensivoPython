#-----OBJETIVO------#
# faca voce mesmo,uma lista de convidados situaçao real

#PSEUDOCODIGO
#-criar uma lista com 3 convidados
#-mostrar msg de que 1 deles n poderá ir
#-adicionar novos convidados
    #|-usar metodo:
    #-insert  no começo
    #-insert  no meio da lista
    #-append  para um novo convidado no final da lista

# +1 convidado n podera aparecer: metod pop
#print de mensagem apos do comparecimeto e a lista vazia

convidados = ['Mac Miller','igor santos','eduardo ramos']
print(convidados)
convidados.sort()
print(convidados)

print("\tOlá" + " " + convidados[0] + " " + "voce foi convidado para cantar uma musica!")
print("\tOlá" + " " + convidados[1] + " " + "voce foi convidado para cantar uma musica!")
print("\tOlá" + " " + convidados[2] + " " + "voce foi convidado para cantar uma musica!")
removido = convidados.pop(-1)
print("\n(o convidado" + " " + removido + " " + "nao poderá comparecer)")
convidados.append("felipe fernandes")
print("\n\tOlá" + " " + convidados[0].title() + " " + "voce foi convidado para cantar uma musica!")
print("\tOlá" + " " + convidados[1].title() + " " + "voce foi convidado para cantar uma musica!")
print("\tOlá" + " " + convidados[2].title() + " " + "voce foi convidado para cantar uma musica!")
