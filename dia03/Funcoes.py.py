#append = adicionar #remove = remover #in = verificação(True/False)
#len: conta quantos caracteres tem
def tabuada(numero):
    for t in range(11):
        r = numero * t
        print(f"{numero} x {t} = {r}")


num = int(input("Digite um número: "))
tabuada(num)