#Dicionário: Uma lista que guarda valores em ordem pelo índice [0], [1], [2]...
#Um dicionário guarda valores por NOME. Em vez de acessar pelo número,
#Você acessa pela chave - que pode ser qualquer texto.
#upper() e lower(): maiúscula e minúscula # strip(): remove espaços
# replacee(): substitui um texto por outro # split(): divide em lista
#len(): tamanho do texto #in: verificar se contém #title(): Primeira letra de cada palavra maiúscula
#enumerate(): retorna o índice e o valor ao mesmo tempo

def cadastrar(pessoas):
    nome = input ("Nome: ").strip().title()
    idade = int(input("Idade: "))
    cidade = input("Cidade: ").strip().title()

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    pessoas.append(pessoa)
    print(f"{nome} cadastrado com sucesso! ")

def listar(pessoas):
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada ainda.")
            return
        
        print(f"\n{len(pessoas)} pessoa(s) cadastrada(s): ")
        for i, pessoa in enumerate(pessoas):
            print(f"{i+1}. {pessoa["nome"]} - {pessoa["idade"]} anos - {pessoa["cidade"]}")

def buscar(pessoas):
    busca = input("Digite o nome para buscar: ").strip().lower()

    encontrados = []    
    for pessoa in pessoas:
        if busca in pessoa["nome"].lower():
            encontrados.append(pessoa)
    if len(encontrados) == 0:
        print("Nenhuma pessoa encontrada.")
    else:
        for pessoa in encontrados:
            print("Nome: " + pessoa["nome"] + " | Idade: " + str(pessoa["idade"]) + " | Cidade: " + pessoa["cidade"])

pessoas = []

while True:
    print("\n === Sistema de CAdastro ===")
    print("1 - Cadastrar pessoa")
    print("2 - Listar peessoas")
    print("3 - Buscar por nome")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar(pessoas)
    elif opcao == "2":
        listar(pessoas)
    elif opcao == "3":
        buscar(pessoas)
    elif opcao == "4":
        print("Até Logo")
        break
