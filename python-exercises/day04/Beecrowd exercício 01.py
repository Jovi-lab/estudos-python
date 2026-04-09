"""
Leia quatro valores inteiros nomeados A, B, C e D. Calcule e imprima a diferença do produto A e B pelo produto de C e D (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprimir DIFERENÇA com todas as letras maiúsculas, conforme o exemplo a seguir, com um espaço em branco antes e depois do sinal igual.
"""

class valores:
    def __init__(self):
        self.A = int(input("Digite o valor de A: "))
        self.B = int(input("Digite o valor de B: "))
        self.C = int(input("Digite o valor de C: "))
        self.D = int(input("Digite o valor de D: "))
        self.resultado = (self.A * self.B) - (self.C * self.D)
        

    def __str__(self):
        return f"DIFERENÇA = {self.resultado}"
    
calc = valores()
print(calc)
    




    