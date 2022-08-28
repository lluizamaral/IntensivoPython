# ---------- OBJETIVO-------------#
# logar e dar respostas de topicos de interesse e perguntas.

# --------pseudocodigo-----------#
#usuarios
#login
#-formataçao de print de entrada hello-world
#-print do que havera nos topico de perguntas
#-fazer uma funçao para o usuario
#   #|-(if para caso ele escolha o que é mostrado ou n)
#if se usuario quiser ver respostas de outros topicos
    #-|,mostrar aba de perguntas respondidas por usuario x
#encerramento do questonario.


cadastro = []
cadastro = usuarios_cadastrando = []

usuarios_cadastrando.append("caua")
usuarios_cadastrando.append("henrrique")
usuarios_cadastrando.append("pedro")


#blocos de usuarios confirmados

usuarios = cadastro.pop(0)
print("\n\tOlá,digite seu nome de usuario no campo abaixo!!!")
login = input()
if usuarios in login:
    print("\n\n \tBem-Vindo ao Questionario de Programação.")
    respostas = []

        #------perguntas------#

    print("\n1.1.qual o a area sua de interesse ??.")
    r_area_interesse = input()
    r_area_interesse = respostas.append(r_area_interesse)

    print("\n1.2.qual a linguagem que você quer aprender ??.")
    r_area_interesse = input()
    r_area_interesse = respostas.append(r_area_interesse)

    print("\n1.3.qual o seu objetivo nessa linguagem ??.")
    r_area_interesse = input()
    r_area_interesse = respostas.append(r_area_interesse)
    
    print("\n\t.Fim do Questionario." + "\n  (deseja ver como está??[y][n])")
    yes_or_no = input()
    if yes_or_no == "y":
        print("\tbom...aqui está o seu historico:")
        for resposta in respostas:
            print("-" + resposta)
        print("\t.obrigado por participar.fim do programa.")
    elif yes_or_no == "n":
        print(".obrigado por participar.fim do programa")
    elif yes_or_no != "n" or "y":
        print("\n\tesse comando não foi reconhecido!faça novamente")
else: 
    print("\n\t(esse nome de usuario é inexitente.)")


