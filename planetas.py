planetas = [

]

def menu():
    print("\nBem-Vindo ao sistema de Planetas do Talento Tech")
    print("\nO que deseja fazer?")
    print("1 - Adicionar Planeta")
    print("2 - Exibir Planetas")
    print("3 - Buscar Planeta por nome")
    print("4 -Alterar informações de um Planeta")
    print("5 - Excluir Planeta")
    print("6 - Sair")

def adicionar():
    nome = input("Nome do Planeta: ")
    massa = float(input("Massa(em Kg): "))
    raio = float(input("Raio(em Km):" ))
    distancia = float(input("Distancia em relação ao Sol(em Km): "))
    planetas.append({"Nome": nome, "Massa": massa, "Raio": raio, "Distancia": distancia})
    print(f"Planeta {nome} adicionado com sucesso!")

def exibir():
    if not planetas:
        print("Poxa que pena,nenhum Planeta ainda foi cadastrado.")
        return
    
    for planeta in planetas:
        print(f"\nNome: {planeta['nome']}")
        print(f"\Massa: {planeta['massa']}")
        print(f"\nNome {planeta['nome']}")
        print(f"\nNome {planeta['nome']}")