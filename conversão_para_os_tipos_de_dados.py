# Conversão dos tipos de Dados ( converte um tipo de dado em outro, por meio de uma função de conversão )
nascimento = 1986
ano_atual = 2022
idade = ano_atual - nascimento
print('Eu tenho ' + str(idade) + ' anos') # converte int para str

# Conversão de inteiro para float
i = 10
f = float(i)
print(f) # saída: 10.0

# Conversão de inteiro para bool
i = 1
b = bool(i)
print(b) # saída: True

# Conversão de inteiro para string
i = 20
s = str(i)
print(s) # saída: '20'

# Conversão de float para inteiro
f = 3.14159
i = int(f)
print(i) # saída: 3

# Conversão de float para bool
f = 0.0
b = bool(f)
print(b) # saída: False

# Conversão de float para string
f = 2.71828
s = str(f)
print(s) # saída: '2.71828'

# Conversão de bool para inteiro
b = True
i = int(b)
print(i) # saída: 1

# Conversão de bool para float
b = False
f = float(b)
print(f) # saída: 0.0

# Conversão de bool para string
b = True
s = str(b)
print(s) # saída: 'True'

# Conversão de string para inteiro
s = '123'
i = int(s)
print(i) # saída: 123

# Conversão de string para float
s = '3.14'
f = float(s)
print(f) # saída: 3.14

# Conversão de string para bool
s = ''
b = bool(s)
print(b) # saída: False

# conversão para o tipo NoneType não existe ( unico jeito é atribuir as variaveis ao valor None )
x = 10
print('Valor:', x, '--', type(x))

# atribuição do valor None à variável x

x = None
print('Valor:', x, '--', type(x))

# a conversão do valor None para outros tipos é possível apenas para os tipos str e bool

print(str(None)) # 'None'
print(bool(None)) # sempre retornara False

#
