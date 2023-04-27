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

# operações com str | operador de acesso é entre [colchetes] e o índice positivo sempre começa pelo zero e o índice negativo começa pelo -1 ( o espaço também conta como caractere )

# indices positivo

qpw = 'consolação'

print('primeira letra da str: ',qpw[0]) # c

print('ultima letra da str: ',qpw[9]) # o

print('pega a letra L da str: ',qpw[5]) # l

print('pega algumas letras da palavra: ',qpw[0:5:1]) # começa pelo 0 vai até o 5 (não retorna a letra do numero 5) pulando de 1 em 1

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

# operadores de indentidade ( a utilidade dos operadores de identidade é verificar se dois objetos são exatamente o mesmo objeto, enquanto a utilidade dos operadores de igualdade é verificar se dois objetos têm o mesmo valor, independentemente de sua identidade. )

x = "hello"

y = "hello"

z = x

print(x is y)  # False, porque x e y são objetos diferentes na memória, mesmo contendo o mesmo valor "hello"

print(x is z)  # True, porque x e z são o mesmo objeto na memória

print(x is not y)  # True, porque x e y não são o mesmo objeto na memória

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

# o bloco de código tratamento de exceções pode ter vários except

# Estruturas Condicionais ( estruturas de controle de fluxo em Python ) Instrução Condicional if – elif – else

# essas condicionais serve para executar um determinado bloco de código se a condição for verdadeira

# if - else

# Exemplo em que a condição é verdadeira

idade = 35

if idade >= 18:  # condição da condicional if

 print('Idade suficiente para CNH!')

else: # se a condição do if for False executa o else

 print('Idade não suficiente para CNH!')

# if - elif - else

idade = 22

if idade < 12: # se essa condição for True

 faixa_etaria = 'Criança' # executa esse código se a condição for False ele pula esse código

elif idade < 18: # se essa condição for True

 faixa_etaria = 'Adolescente' # executar esse código se for False ele pula esse código

elif idade < 60: # elif pode ser usado várias vezes

 faixa_etaria = 'Adulto'

else: # essa condição é executada se as duas condições if elif retorna False

 faixa_etaria = 'Idoso'

print('Faixa Etária: ', faixa_etaria)

# Estrutura de repetição while ( while é uma Estrutura de repetição que executa um determinado bloco de código enquanto a condição for True )

# exemplo com n = 15

n = 15

soma = 0

contador = 0

while contador <= n:

 soma += contador

 contador = contador + 1

print(f'A soma dos primeiros {n} inteiros é {soma}')

# exemplo sem a variavel contador

n = 15

soma = 0

while n >= 0: # condição n é maior ou igual a 0

 soma += n

 n -= 1

print(f'A soma dos primeiros inteiros é {soma}')

# Estrutura de repetição for in ( ela pecorre uma sequência interavel ) ( sequência  interavel são listas, tuplas, conjuntos e strings )

# exemplo a palavra araranguara

a = 'araraguara'

contador = 0

for num in a:

    if num == 'a':

        contador += 1

print(f'a palavra {a} tem {contador} letras "a"')

# a função range() é usado para cria uma sequencia de números ( ele sempre começa com 0 e o valor de fim não é incluído na sequência resultante )

   # range(stop): cria uma sequência de números que vão de 0 até stop-1. range(12) começa com 0 e vai até o 11

   # range(start, stop): cria uma sequência de números que vão de start até stop-1. range(1, 10) começa no 1 e vai até 9

   # range(start, stop, step): cria uma sequência de números que vão de start até stop-1, pulando de step em step. range(0, 11, 2) começa no 0 até o 10 pulando de 1 em 1

# exemplo com n = 15

n = 15

soma = 0

for num in range(n + 1): # n + 1 é o intervalo

 soma = soma + num

print(f'A soma dos primeiros {n} inteiros é {soma}')

# Interrupção da Estruturas de Repetição ( existe o comando break, que encerra a instrução de repetição ao verificar se uma condição específica é verdadeira. if-else )

for num in range(250, 301):

    if num % 21 == 0:	      print(f'o divisor de 21 é {num}')

      break

# também é possível fazer com o while

contador = 0

while True: # True faz a repetição nunca parar se não tiver o break no final

    print(contador)

    contador += 1

    if contador >= 10:

        print("Contador chegou a 10, interrompendo a execução.")

        break

# Estrutura de dados em python ( tipos não primitivo de dados ) ( as estruturas de dados em Python permitem armazenar e manipular diferentes tipos de dados de forma mais eficiente e conveniente Ao usar essas estruturas de dados, os programadores podem escrever código mais eficiente e legível, facilitando a manipulação dos dados em seus programas. )

# Listas [list] Tuplas (tuple) Conjuntos {set} Dicionário {dict}

# Criação de Listas e Acesso dos Elementos ( existe list homogênea os elementos são do mesmo tipo ) ( existe list heterogêneo os elementos são diferentes tipos )

s = [2, 'a', 5.44, True] # lista com valores heterogêneo

print(s)

c = ['um', 'dois', None, 4] # lista com valor nulo dentro

print(c)

l = [0, 1] # listas com outras listas dentro (listas aninhadas)

l = [l, 'dois', 'três', [4, 5], 'seis']

print(l)

i = [] # lista vazia

print(i)

# para acessar um elemento da lista usa operador ([]) colocando o índice ( é possível utilizar indice negativo ) ( e fazer slicing que é uma sub-list)

lista = [2, 'a', 5.44, True, None, 'casa']

# acesso por índices

print(lista[0])

print(lista[3])

print(lista[-1])

# acesso por slices

print(lista[1:4])

print(lista[-2:])

print(lista[:])

# encontrar o maior idade entre um grupo de três pessoas

idades = [27, 49, 12, 67, 21, 32, 18, 45, 84, 53, 22, 56, 80, 35, 18]

maior_idade = idades[0] # assume que a primeira idade é maior

for idade in idades: # percorrer a cada elemento da list

 if idade > maior_idade:

     maior_idade = idade

print(f'a maior idade da list é {maior_idade}')

# manipulação de list 

list = [2, 'a', 'b', 'c', 5.44, True]

print(list)

list.append(999) # método append adiciona um novo elemento na list

print(list)

# Altera o valor do quarto e o do último elemento

list[3] = 'a'

list[-1] = list[-1] + 1

print(list)

list.remove('a') # remove a primeira elemento 'a' que tiver na list ( pode dar erro se o elemento não existir )

print(list)

# dá para usa operadores de cocatenação (+), repetição (*) e de filiação (in) com as listas. Também podemos utilizar funções e métodos. igual na str

l1 = [30, 10, 20]

l2 = [2, 'a', 5.44, True]

# Operações de concatenação (+), repetição (*) e filiação (in)

print(l1 + l2)

print(l1 * 3)

print(10 in l1)

# Funções úteis

print(len(l2)) # len: retorna a quantidade de elementos da lista.

print(sum(l1)) # sum: retorna a soma dos elementos de uma lista. ( só funciona com list int )

print(max(l1)) # max: retorna o maior elemento da lista ( só funciona com list int )

print(min(l1)) # retorna o menor valor da list ( so funciona com list int )

# Métodos que alteram os valores internos da lista

l2.reverse() # reverse: inverte a ordem dos elementos

print(l2)

l1.extend([10, 20, 30, 40, 10]) # extend: adiciona elementos de outra sequência

print(l1)

l1.sort() # sort: ordena os valores da lista ( dá erro se coloca int com str ) ( mais funciona com list str )

print(l1)

l2.insert(2, 'novo valor') # insert: adiciona um elemento em um índice especifico

print(l2)

l2.pop() # pop: remove o último elemento da lista

print(l2)

l2.clear() # clear: limpa a lista, removendo todos os elementos

print(l2)

# Métodos que retornam valores e não alteram a lista

print(l1.index(40)) # index: retorna o índice do elemento list

print(l1.count(10)) # count: conta quantas elementos 10 tem na list

# da para usar o metodo max() para encontrar a maior idade de um grupo de pessoas

idades = [27, 49, 12, 67, 21, 32, 18, 45, 84, 53, 22, 56, 80, 35, 18]

print('Maior idade:', max(idades))

# tuplas ( tuplas são iguais a list mais são ordenando e imutaveis não é possível muda os valor e nem adicionar )

# Criação de uma tupla homogênea

tupla = (0, 1, 3, 4)

print(tupla)

# Tupla heterogênea

tupla2 = (2, 'a', 5.44, True, None)

print(tupla2)

# Tupla vazia

tupla3 = ()

print(tupla3)

# acesso por índices

print(tupla[0])

print(tupla[3])

print(tupla[-1])

# acesso por slices

print(tupla2[1:4])

print(tupla2[-2:])

print(tupla2[:])

# métodos para tuplas

t1 = (30, 10, 20)

t2 = (2, 'a', 5.44, True)

# Operações de concatenação (+), repetição (*) e filiação (in)

print(t1 + t2)

print(t1 * 3)

print(10 in t1)

# Funções úteis

print(len(t2)) # len: retorna a quantidade de elementos da tupla

print(min(t1)) # min: retorna o menor elemento da tupla

print(max(t1)) # max: retorna o maior elemento da tupla

print(sum(t1)) # sum: retorna a soma dos elementos da tupla

# Métodos que retornam valores

print(t1.index(20)) # index: retorna o índice da primeira ocorrência do elemento

print(t2.count('a')) # count: conta as ocorrências do elemento

# sets ( o tipo sets é não-ordenadas que representam uma coleção de itens unicos sem repetições e também é mutavel )

# o tipo sets suporta operações matemáticas entre conjuntos como união, interseção e diferença.

# Criação de um conjunto homogêneo

c1 = {3, 0, 1, 4, 3} # o tipo sets retorna os elementos em ordem numérica ou alfabética

print(c1)

# Criação do mesmo conjunto, porém com uma ordenação diferente dos itens

c2 = {2, 1, 4, 3, 0}

print(c2)

# Conjunto heterogêneo

c3 = {2, 'a', 5.44, True, None}

print(c3)

# não existe uma maneira direta de acessa a os elementos do sets

# o tipo set é uma estrutura projetada para não fornecer acesso aos elementos e sim para representar os dados em forma de conjunto e oferecer operações matemáticas tradicionais

    # união - A ∪ B ( O resultado será o conjunto formado por todos os elementos de A e B )

    # interseção - A ∪ B ( O resultado será o conjunto formado apenas pelos elementos que estejam em A e B, simultaneamente )

    # diferença - A - B ( O resultado será o conjunto formado pelos elementos que estejam em A, mas que não estejam em B )

# as operações podem ser realizado através de operadores ou métodos

# Criação dos conjuntos A e B

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}

print('A:', A)

print('B:', B)

# Operação de União: (A ∪ B)

print('A | B =>', A | B)

print('A.union(B) =>', A.union(B))

# Operação de Interseção: (A ∩ B)

print('A & B =>', A & B)

print('A.intersection(B) =>', A.intersection(B))

# Operação de Diferença: (A - B) e (B - A)

print('A - B =>', A - B)

print('A.difference(B) =>', A.difference(B))

print('B - A =>', B - A)

print('B.difference(A) =>', B.difference(A))

# metodos

# Criação dos conjuntos A e B

c1 = {1, 2, 3, 4, 5}

c2 = {4, 5}

c3 = {91, 92, 93}

# Adiciona um elemento ao conjunto

c1.add(6)

print(c1)

# Adiciona os elementos de uma sequência iterável

c1.update([2, 4, 6, 8])

print(c1)

# Descarta um elemento do conjunto

c1.discard(8)

print(c1)

# Diferentemente do set.remove(), o discard não gera um erro se o elemento a ser removido não existir

c1.discard(99)

print(c1)

# Verifica se os conjuntos são disjuntos, ou seja, se não possuem nenhum elemento em comum

print(c1.isdisjoint(c2))

print(c1.isdisjoint(c3))

# Verifica se o conjunto é subconjunto de outro

print(c1.issubset(c2))

print(c2.issubset(c1))

# Verifica se o conjunto contém outro conjunto (superset)

print(c1.issuperset(c2))

print(c2.issuperset(c1))

# exemplo prático com sets ( um programa para gerenciar três turmas de idioma inglês, espanhol e francês )

# precisamos resolver dois problemas ( 1.cria uma relação com todas os alunos da escola sem repetições ) ( 2.Identificar os alunos que estão matriculados em pelo menos duas ou mais turmas para oferecermos um desconto )

# Criação dos conjuntos de alunos das turmas ( o tipo sets é a melhor forma porque não retorna os elementos repetidos )

ING = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}

ESP = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}

FRA = {'Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina'}

# Operação de união dos conjuntos (união dos alunos de todas as turmas)

# intercessão de todas as turmas

# Também poderia ser: ALL = ING.union(ESP).union(FRA)

ALL = ING | ESP | FRA

# Exibição do resultado

print('Relação de todos os alunos da escola:')

print(ALL)

# calcula a intercessão entre os pares de conjuntos e depois realiza a união das intercessões gerando a lista final d

ING = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}

ESP = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}

FRA = {'Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina'}

# 1 – Interseção entre os pares de turmas: (ING & ESP), (ING & FRA) e (ESP & FRA)

# 2 – Calcula a união das interseções

ALUNOS_DESCONTO = (ING & ESP) | (ING & FRA) | (ESP & FRA)

# Exibição do resultado

print('Relação de dos alunos com desconto:')

print(ALUNOS_DESCONTO)

# dict ( o tipo de dado dict é uma coleção de itens (igual aos outros) entretanto cada elemento é um par key/value ( chave - valor ) os pares indicam que cada elemento possui um valor/value atrelado a uma chave/key)

# o dict é feito por chaves {} e as chaves (key) são unicas e imutaveis

# Dicionário onde as chaves são do tipo string

d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}

print(d1)

# Dicionário onde as chaves são do tipo inteiro

d2 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'}

print(d2)

# Dicionário com chaves de tipos mistos

d3 = {2: 'a', 5.44: True, 'key': None}

print(d3)

# Dicionário vazio

d4 = {}

print(d4)

# a única forma de acessa os elemento do dict é por meio da chave (key) entre colchetes []

# Criação dos dicionários

d1 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'}

d2 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}

# Acesso aos elementos

print(d1[0])

print(d1[2])

print(f'Meu nome é {d2["nome"]} e tenho {d2["idade"]} anos')

# se tenta acessa um elemento por uma chave que não existe retornara erro de execução alertando que a chave não existe

# mas existe uma forma de acessar os elementos (dic.get(key)) que ao invés de retorna erro retorna um valor nulo

# Criação do dicionário

d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}

# Acesso por meio do método get()

print(d1.get('endereço'))

# o valor/value são mutaveis pode adicionar novos itens ou alterar o valor, se a chave (key) não existir um novo par de (key - value) será adicionado ao dicionário

# Criação do dicionário

d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}

print(d1)

# Atualização do valor da chave 'nome'

d1['nome'] = 'Antônio Carlos'

print(d1)

# Adição da chave 'endereço' junto com o valor 'Rua 123'

d1['endereço'] = 'Rua 123'

print(d1)

# o dict também tem varios operadores, funções e métodos que operam seus elementos algumas das operações se comporta da mesma forma que os outros elementos e outras possuem diferenças

  # o min() e o max() continua retornando o minimo minimo e o máximo mais funciona só com a chave/key ignorando o seus valor/value

  # Os operadores de filiação in e not in também operam sobre as chaves, e não sobre os valores.

  # O método pop(key) remove o elemento com a chave key. Para remover o ultimo elemento existe o método popitem().

# Cria o dicionário

d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4}

print(d1)

# Encontra a maior e menor chave

print('Maior e menor chave:', max(d1), min(d1))

# Adiciona elementos de um outro dicionario

d1.update({'cinco': 5, 'seis': 6})

print(d1)

# Verifica se o dicionário possui as seguintes chaves

print("A chave 'dois' está no dicionário?", 'dois' in d1)

print("A chave 'cinco' não está no dicionário?", 'dois' in d1)

# Remove o elemento com chave 'zero' e o valor

d1.pop('zero')

print(d1)

# remove o último elemento com chave e o valor

d1.popitem()

print(d1)

# também é possível utilizar o loop for in no dict ( e em outras estruturas de dados ) entretanto devemos fica atento ao sobre o que queremos iterar

  # no dict podemos iterar sobre chaves (dict.keys()) sobre os valores (dict.values()) ou sobre os itens (dict.items()) no caso dos pares key:value se não específica, a interação sera sobre as chaves por padrão

# Cria o dicionário

d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4}

# Itera sobre as chaves

for key in d1:

    if key == 'três':

        print('Chave três encontrada!')

for key in d1.keys():

    if key == 'quatro':

        print('Chave quatro encontrada!')

# Itera sobre os valores

soma = 0

for value in d1.values():

  soma += value

print('Soma dos valores do dicionário:', soma)

# Itera sobre os itens

for key, value in d1.items():

 print(key, value)
