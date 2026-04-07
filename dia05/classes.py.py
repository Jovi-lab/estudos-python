#Classe: forma(molde). #Objeto: Algo criado a partir dessa forma.
#Self: referencia ao objeto
#__init__: Método Construtor
#Attribute: __dict__ ; 
#Method: __getstate__

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.cidade}"
    
class Cadastro:
    def __init__(self):
        self.pessoas = []

    def adicionar(self, pessoa):
        self.pessoas.append(pessoa)
        print(f"{pessoa.nome} cadastrado com sucesso! ")

    def listar(self):
        if len(self.pessoas) == 0:
            print("Nenhuma pessoa encontrada.")
            return
        print(f"--- {len(self.pessoas)} pessoa(s) cadastrada(s) ---")
        for i, pessoa in enumerate(self.pessoas):
            print(f"{i+1}. {pessoa}")

    def buscar(self, nome):
        nome = nome.strip().lower()
        encontrados = [p for p in self.pessoas if nome in p.nome.lower()]
        if not encontrados:
            print("Nenhum resultado encontrado.")
        for p in encontrados:
            print(p)

    def media_idade(self):
        if not self.pessoas:
            return 0
        return sum(p.idade for p in self.pessoas) / len(self.pessoas)
    
    def remover(self, nome_remover):
        nome_remover = nome_remover.strip().lower()
        tamanho_antes = len(self.pessoas)
        self.pessoas = [p for p in self.pessoas if p.nome.lower() != nome_remover]

        if len(self.pessoas) < tamanho_antes:
            print(f"Registro de {nome_remover} removido com sucesso!")
        else:
            print ("Nome não encontrado")
    
def menu():
        cadastro = Cadastro()

        while True:
             print("\n=== Sistema de Cadastro ===")
             print("1 - Cadastrar pessoa")
             print("2 - Listar todos")
             print("3 - Buscar por nome")
             print("4 - Media de idade")
             print("5 - Remover nome")
             print("6 - Sair")
             opcao = input("opção: ")

             if opcao == "1":
                 nome = input("nome: ")
                 idade = int(input("idade: "))
                 cidade = input("cidade: ")
                 p = Pessoa(nome, idade, cidade)
                 cadastro.adicionar(p)
             elif opcao == "2":
                 cadastro.listar()
             elif opcao == "3":    
                 busca = input("Nome para buscar: ")
                 cadastro.buscar(busca)
             elif opcao == "4":        
                 print(f"Media de idade: {cadastro.media_idade():.1f}")
             elif opcao == "5":        
                 excluir = input("Nome para exclusão: ")
                 cadastro.remover(excluir)
             elif opcao == "6":
                 print("Até Logo!")
                 break
             else:
                 print("Opção inválida!")

menu()
        
    



        