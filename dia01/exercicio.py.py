#Toda variável é um objeto
A = float(input('Qual o primeiro número?'))
Op = input('Qual a operação quee deseja realizar? +, -, * ou / ?')
B = float(input('Qual o segundo número?'))

if Op == '+':
    Op = A + B
elif Op == '-':
    Op = A - B
elif Op == '*':
    Op = A * B
elif Op == '/':
    Op = A / B

else: 
    print('Operação Inválida!')

print(f'Resultado: {Op}')