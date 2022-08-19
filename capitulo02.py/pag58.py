


print("\texercicios 2.1")
usuarios = []
sobrenomes = []
    #.campo de cadastro.#
usuarios.append("marcos"),sobrenomes.append("vinicios")
usuarios.append("hugo"),sobrenomes.append("virgilio")
usuarios.append("paulo"),sobrenomes.append("oliveira")
    #.campo de de formatação.#
nomes_completos = usuarios + sobrenomes
for nome in nomes_completos:
    print("Bem Vindo De Volta!!!" + " " + nome.title().strip())

