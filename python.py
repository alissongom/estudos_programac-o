# tipos primitivos de dados em python
# int
x = 817 # x está atribuido ao valor 817
v = -x # a variável esta retornando o valor negativo
print(x,v)

# float
f = 28.39
a = -f
print(f,a)

# bool
ds = True # 1
we = False # 0
print(ds,we)

# str (tipo não primitivo)
q = 'str com aspas simples são mais usado para deixa o código legivel e serve para coloca "aspas duplas" dentro\n' # \n essa função faz quebra de linha
s = "str com aspas duplas serve para coloca 'aspas simples' dentro"
z = '''\te existe str com aspas triplas que serve para coloca 'aspas simples' e "aspas duplas" dentro

da para fazer multi quebras de linhas e multi    espaços''' # a função \t adiciona um espaço horizontal
print(q, s, z)

# complex (tipo coomplexo)
de = 3j
print(de)

# tem o tipo especial que não tem nenhum valor o NoneType
q = None

# existe uma função que diz qual é o tipo de dado type()
print(type(q))

# atribuição multipla
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)


# operadores dos tipos primitivos de dados
# operadores aritméticos
t = 28
oi = 21
print(t ** oi) # exponencial
print(t * oi) # multiplicação
print(t / oi) # divisão
print(t // oi) # divisao_int
print(t % oi) # resto_divisao
print(t + oi) # adição
print(t - oi) # subtração
# calculo grande precisa usa logica de pemdas
r = (28 + 72) * 838 ** 92 // 82 % 82 / 1 - 98
print(r)

# operador de atribuição composta
a = 5
b = 10
c = 15
a += 2  # equivalente a a = a + 2 ( com adição é possível junta str )
print(a)  # 7
b -= 4  # equivalente a b = b - 4
print(b)  # 6
c *= 2  # equivalente a c = c * 2
print(c)  # 30
a /= 2 # equivalente a a = a / 2
print(a)
b %= 2 # equivalente a b = b % 2
print(b)
c //= 3 # equivalente a c = c // 3# bool
print(c)
b **= 3 # equivalente a b = b ** 3
print(b)

# operadores de comparação
y = 48
yu = 10
uy = 29
print(y > uy) # True
print(y >= yu) # True
print(uy < yu) # False
print(uy <= yu) # False
print(uy == y) # False
print(y != uy) # True

# pode usa operadores aritméticos com operadores de comparação juntos
ret = 19
pill = 38
ter = 21
print((38 * ter) > pill)
print(ret >= (ter // pill))
print(ter < (29 + 21))
print(ter <= (ret % pill))
print(pill == (ter + 18))
print(ter != (10 + ret))

# para fazer comparação com str com outro tipo de dado só é possível com o operador de igualdade == e diferente !=
xz = 3
cz = 'palavra'
print(xz == cz)
print(xz != cz)

# para usa operadores de comparação com str precisa ser do mesmo tipo de dado e a comparação é feita pela comparação lexicografica ( tabela unicode )
er = 'gato'
qs = 'largato'
li = 'cachorro'
print(li > qs) # False
print(qs < er) # False
print(li > er) # False
print(qs > li) # True

# operadores logicos and, or, not
# and
cu = True
cool = 18
print(cool >= 12 and cu)# and só retorna True se os dois valores for verdadeiro

# or
ver = 12
fg = True
print(ver > 18 or fg) # or retorna True se 1 dos valores for verdadeiro

# e tem o operador not que inverte o valor de True para False e False para True
kj = 18
pr = False
print(not(kj > 18 or pr))

# operadores de indentidade ( a utilidade dos operadores de identidade é verificar se dois objetos são exatamente o mesmo objeto, enquanto a utilidade dos operadores de igualdade é verificar se dois objetos têm o mesmo valor, independentemente de sua identidade. )
x = "hello"
y = "hello"
z = x
print(x is y)  # False, porque x e y são objetos diferentes na memória, mesmo contendo o mesmo valor "hello"
print(x is z)  # True, porque x e z são o mesmo objeto na memória
print(x is not y)  # True, porque x e y não são o mesmo objeto na memória

# operações com str | operador de acesso é entre [colchetes] e o índice positivo sempre começa pelo zero e o índice negativo começa pelo -1 ( o espaço também conta como caractere )
# indices positivo
qpw = 'consolação'
print('primeira letra da str: ',qpw[0]) # c
print('ultima letra da str: ',qpw[9]) # o
print('pega a letra L da str: ',qpw[5]) # l
print('pega algumas letras da palavra: ',qpw[0:1:3:4])

# indices negativos
print('pega a primeira letra da str: ',qpw[-10]) # c
print('pega a ultima letra da str: ', qpw[-1]) # 0
print('pega a letra L da str: ',qpw[-5]) # l
print('inverte a str: ',qpw[::-1])

# também é possível fazer uma sub-str que é uma str feita pela str original
print(qpw[3:6]) # palavra sol
print(qpw[-4:]) # palavra ação
print(qpw[3:7]) # palavra sola
print(qpw[:7]) # palavra consola

# operadores de string ( * repete a str N vezes ) ( + Concatena (une) duas strings em uma única str )
jk = 'belo'
jn = 'horizonte'
# repetição
print(4 * jk) # retorna belobelobelobelo
print((jk + ',') * 4) # retorna belo 4 vezes com vírgula
# cocatenacão
print(jk + jn)
print(jk + ' ' + jn) # a vírgula com um espaço dentro serve para dar espaço entre as str
print(jk + ' monte')

# também tem os operadores para verificar se uma str esta esta contida na outra str
# `in` retorna True se a str1 estiver contida na str2
# `not in` retorna True se a str1 NÃO estiver contida na str2
s1 = 'consolação'
s2 = 'sola'
print(s1 in s2) # False
print(s2 in s1) # True
print('sola' in s1) # True
print('sola' not in s2) # False

# Metodos para Str ( Manipulação de Str )
palavra = 'consolação'
print(len(palavra)) # função `len()` retorna quantas caracteres a str tem
s1 = 'belo Horizonte'
s2 = 'Esta é uma frase, com uma vírgula.'
s3 = ' palavra com espaços '
s4 = '231'
print(s1.upper()) # todas as letras maiúsculas ( .isupper retorna True se tiver maiúsculo )
print(s1.lower()) # todas as letras minúsculas ( .islower retornar True se tiver minúsculo )
print(s2.title()) # primeira letra de cada palavra em maísculo ( .istitle retorna True se primeira letra de cada palavra tiver maiúscula )
print(s1.replace('Horizonte', 'Monte')) # substitui 'Horizonte' por 'Monte'
print(s1.startswith('belo')) # verifica se a string começa com 'Belo'
print(s1.endswith('Monte')) # verifica se a string termina com 'Monte'
print(s2.find('frase')) # retorna o índice da primeira ocorrência da palavra frase ( retorna -1 se não for encontrado )
print(s2.split()) # particiona a string, que são separadas por um espaço
print(s2.split(',')) # particiona a string, que são separadas por ','
print(s3.strip()) # remove os espaços extras no início e fim da string
print(s1.capitalize()) # retorna a primeira letra da palavra maiúsculo e o resto minúsculo
print(s2.count('a')) # retorna quantas vezes um elemento aparece na str
print(s4.isnumeric()) # retorna True se a str tiver só números, retorna False se tiver letras ou numeros com ponto ou decimal

# Os métodos das str podem, também, ser utilizados diretamente na declaração do valor.
print('nome'.upper())
a1 = 'console'
ae = a1.upper().replace('CO', 'C') # também é possível utilizar esse método
print(ae)


# Conversão dos tipos de Dados ( converte um tipo de dado em outro, por meio de uma função de conversão )
nascimento = 1986
ano_atual = 2022
idade = ano_atual - nascimento
print('Eu tenho ' + str(idade) + ' anos')

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


# Formatação de Str ( str literais formatadas ) f-str
nascimento = 1986
ano_atual = 2022
print(f'Eu tenho {ano_atual - nascimento} anos') # é possível usa operadores aritméticos no f-str

# também é possível usa metodos e funções no f-str
print(f'exemplo de f-str com um valor de 10 é uma expressão {10 == 15}')
palavra = 'consolação'
print(f'A palavra {palavra.upper()} possuí {len(palavra)} letras')

# formatação com numeros float
orcamento = 7000
vlr_gasto = 430
pct = (vlr_gasto/orcamento)
print(f'Porcentagem já gasta do orçamento: {pct:.2%}') # com o símbolo de porcentagem ( % ) permite declarar que o valor é uma porcentagem, assim não é necessário multiplica por 100


# Tratamento de exceções
try:
    # Código que pode levantar exceções
    x = int(input("Digite um número: "))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    # Tratamento de exceção quando há uma divisão por zero
    print("Não é possível dividir por zero")
except ValueError:
    # Tratamento de exceção quando o usuário não digita um número válido
    print("Por favor, digite um número válido")
except:
    # Tratamento de exceção genérico para qualquer outro tipo de exceção
    print("Ocorreu um erro")
# pode criar vários except


# Estruturas Condicionais ( if elif else ) Instrução Condicional if – elif – else

idade = 22

if idade < 12: # se essa expressão for True

 faixa_etaria = 'Criança' # executa esse código se for False ele pula esse código

elif idade < 18: # se essa expressão for True

 faixa_etaria = 'Adolescente' # executar esse código se for False ele pula esse código

elif idade < 60: # elif pode ser usado várias vezes

 faixa_etaria = 'Adulto'

else: # essa condição é executada se as duas condições if elif retorna False

 faixa_etaria = 'Idoso'

print('Faixa Etária: ', faixa_etaria)

#

#

#

# Estrutura de repetição while ( while é uma Estrutura de repetição que executa um determinado bloco de código enquanto a condição for True)

# exemplo com n = 15

n = 15

soma = 0

contador = 0

while contador <= n:

 soma = soma + contador

 contador = contador + 1

print(f'A soma dos primeiros {n} inteiros é {soma}')

# exemplo com n = 15

n = 15

soma = 0

while n >= 0:

 soma = soma + n

 n = n - 1

print(f'A soma dos primeiros inteiros é {soma}')

#

#

#

# Estrutura de repetição for in ( ela pecorre uma sequência interavel ) ( sequência  interavel são listas, tuplas, conjuntos e strings)

# exemplo a palavra araranguara

a = 'araraguara'

contador = 0

for num in a:

    if num == 'a':

        contador += 1

print(f'a palavra {a} tem {contador} letras "a"')

# a função range() é usado para cria uma sequencia de números ( ele sempre começa com 0 e o valor de fim não é incluído na sequência resultante)

   # range(stop): cria uma sequência de números que vão de 0 até stop-1. range(12) começa com 0 e vai até o 11

   # range(start, stop): cria uma sequência de números que vão de start até stop-1. range(1, 10) começa no 1 e vai até 9

   # range(start, stop, step): cria uma sequência de números que vão de start até stop-1, pulando de step em step. range(0, 11, 2) começa no 0 até o 10 pulando de 1 em 1

# exemplo com n = 15

n = 15

soma = 0

for num in range(n + 1): # n + 1 é o intervalo

 soma = soma + num

print(f'A soma dos primeiros {n} inteiros é {soma}')

#

#

#

# Interrupção da Estruturas de Repetição ( existe o comando break, que encerra a instrução de repetição ao verificar se uma condição específica é verdadeira. if-else)

for num in range(250, 301):

	if num % 21 == 0:		print(f'o divisor de 21 é {num}')

		break

# também é possível fazer com o while

while True: # True faz a repetição nunca parar

    print(contador)

    contador += 1

    if contador >= 10:

        print("Contador chegou a 10, interrompendo a execução.")

        break

#

#

#

# operadores de identidade ( endereço de memória ) ( is is not verifica se as variáveis tem valores unicos dos objetos )

a = [1, 2, 3]

b = [1, 2, 3]

print(a is b)  # False

c = a

print(a is c) # True

print(b is not a)
