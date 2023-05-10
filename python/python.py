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

# str
q = 'str com aspas simples são mais usado para deixa o código legivel e serve para coloca "aspas duplas" dentro\n' # a função \n dá quebra de linha
s = "\tstr com aspas duplas serve para coloca 'aspas simples' dentro" # a função \t dá uma espaço horizontal
z = '''e existe str com aspas triplas que serve para coloca 'aspas simples' e "aspas duplas" dentro
da para fazer multi quebras de linhas e multi    espaços'''
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

# para usa operadores de comparação de str precisa ser do mesmo tipo de dado e a comparação é feita pela comparação lexicografica ( tabela unicode )
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
print(cool >= 12 and cu) # and só retorna True se os dois valores for verdadeiro

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
print('pega algumas letras da palavra: ',qpw[0:5:1]) # começa pelo 0 vai até o 4 (não retorna a letra do numero 5) pulando de 1 em 1

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

# parâmetros opcionais ( por padrão o print da quebra de linha )
a = 'hello'
b = 'horld'
print(a, end=' ' + b) # end='' especifica o que vai acontecer no final da linha, como quebra de linha assim o próximo texto vai estar na mesma linha ( é possível também usa end no print, print("Olá, mundo!", end='')print("Este é um exemplo.")
print("Janeiro", "Fevereiro", "Março", sep="-") # o sep especifica o que deve ser adicionado entre os valores que serão impressos

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
    if num % 21 == 0:	      
        print(f'o divisor de 21 é {num}')
      break
# também é possível fazer com o while
contador = 0
while True: # True faz a repetição nunca parar se não tiver o break no final
    print(contador)
    contador += 1
    if contador >= 10:
        print("Contador chegou a 10, interrompendo a execução.")
        break
# O continue é uma instrução em Python que é usada dentro de estruturas de repetição, como for e while, para pular uma determinada iteração do loop e passar para a próxima.
  # Quando o continue é encontrado dentro do bloco do loop, o código que vem depois dele é ignorado e a execução passa imediatamente para a próxima iteração do loop. Ou seja, o restante do bloco do loop é ignorado naquela iteração, mas o loop continua executando normalmente nas próximas iterações.
  # Por exemplo, suponha que queremos imprimir apenas os números pares de 1 a 10. Podemos usar um for loop para percorrer os números de 1 a 10 e usar o continue para pular a impressão dos números ímpares:
for i in range(1, 11):
    if i % 2 != 0: # se dá True o continue sera executado e não vai ser executado o print, se dá False o continue não vai ser executado e o print vai mostra o numero par
        continue
    print(i)
# também é possível fazer isso no while
i = 1 # acontece a mesma coisa que aconteceu no for
while i <= 10:
    if i % 2 != 0: # se dá False executa adicionando mais 1 pra variavel i e executa o continue ignorando o print e a variável
        i += 1
        continue
    print(i)
    i += 1

# existe o comando pass que faz o python ignora a função quando esta vazio que serve para depois ser preenchidos
for x in range(10):
    pass

# loops aninhados
for x in range(2): # executa primeiro e só 1 vez (atribui 0 a variável do loop)
    for y in range(2): # executa segundo e 2 vezes (primeiro atribui 0 e depois atribui 1 pra variável do loop)
        print(x,y) # retorna na tela o valor dos dois loop 00, 01, 10, 11
# outro exemplo
for i in range(1, 11): # atribui 1 a variável do loop (fileira)
    for j in range(1, 11): # executa 10 vezes para cada valor de i (coluna)
        print(i*j, end='\t') # retorna só o valor do cálculo (1x1=1 10 vezes) (2x1=2)
    print() # o print() vazio serve para dar uma quebra de linha
# primeiro numero da coluna é 1x1, 1x2, 1,10 depois na segunda coluna numero 2x2, 2x4...


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
l3 = 'string'
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
l4 = l2.copy() # copia a lista para outra variavel ( se adicionar algo para a primeira list não vai aparecer aqui )
print(l4)
# dá para tranforma qualquer objeto interavel em list os tipos são String, Tuplas, Dicionário, Conjuntos, Sequências numéricas (range, numpy arrays, etc.)
qw = list(l3)
print(qw)

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
# funções em python ( Uma função é basicamente um bloco de código, que realiza uma determinada tarefa e que pode ser reutilizado várias vezes. As funções auxiliam na divisão do programa em partes menores e modulares, e à medida que o código cresce cada vez mais, as funções o tornam mais organizado e gerenciável. )
# declaração de funções:
# define as listas com os números a serem somados
l1 = [1, 2, 3, 4, 5]
l2 = [3, 1, 5, 9, 0, 8, 2, 3, 4]
l3 = [12, 43, 23, 12, 789]
# declaraca a função que soma os elementos da lista
def soma_lista(lista): # define a função e o nome da função e o argumento listas
    soma = 0
        for item in lista:
            soma += item
    return soma # return retorna o resultado da função
# chama a função para cada lista
soma_l1 = soma_lista(l1) # chama a função com um argumento
soma_l2 = soma_lista(l2)
soma_l3 = soma_lista(l3)
print(f'Resultado: l1={soma_l1}, l2={soma_l2}, l3={soma_l3}')
# utilização de funções ( Vamos considerar o seguinte código, onde as funções são utilizadas diversas vezes e na ordem que desejarmos: )
# exibe mensagem de boas vindas à uma pessoa
def boas_vindas(nome):
    print(f'Olá {nome}. Seja bem-vindo (a)!') # essa função não retornar um valor e por isso não precisa do return
# calcula a área de um quadrado: l x l
def area_quadrado(lado): 
    return lado * lado
# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura): 
    return (base * altura)/2
# Realiza as chamadas das funções
boas_vindas('Priscila')
print(area_triangulo(4, 5))
boas_vindas('Maria')
boas_vindas('Joana')
print(area_quadrado(4)) # a área_quadrado precisa só de 1 argumento para realizar o cálculo e retorna o valor
print(area_quadrado(10))
boas_vindas('Antônio')
print(area_quadrado(10))
print(area_triangulo(5, 2)) # a area_triangulo precisa de dois argumentos para realizar o cálculo
print(area_triangulo(4, 5))
# Vamos considerar agora outro exemplo, que apresenta diferentes conceitos das funções em Python.
# Realiza uma divisão. Se o divisor é zero, retorna uma mensagem de erro. 
def div(dividendo, divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return # a função vai retorna a mensagem se o divisor for igual a zero
    return dividendo / divisor # e vai retornar o valor do cálculo
# Função similar à função div, mas que retorna o dividendo e o resto da divisão.
def div_qr(dividendo, divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return (quociente, resto) # vai retorna o quociente e o resto da divisão
print('div(10, 4) ==>', div(10, 4)) # dividento=10 e divisor=4
print('div(10, 0) ==>', div(10, 0)) # dividento=10 e divisor=0
print('div_qr(10, 4) ==>', div_qr(10, 4)) # dividento=10 e divisor=4
# atribuição dos múltiplos valores em uma variável única do tipo tupla
resultado = div_qr(21, 5)
print('resultado:', resultado, type(resultado))
# atribuição dos múltiplos valores em variáveis separadas
quociente, resto = div_qr(21, 5)
print('quociente:', quociente, type(quociente))
print('resto:', resto, type(resto))
# funções que utilizam outras funções
# Verifica se é um divisor inválido (divisor == 0)
def divisor_invalido(divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return True # retorna True se for zero
    return False # retorna False se não for zero
# Retorna o resultado de uma divisão
def div(dividendo, divisor):
    if divisor_invalido(divisor): # chama a primeira função para verificar se é zero
        return
    return dividendo / divisor
# Retorna o quociente e o resto de uma divisão
def div_qr(dividendo, divisor):
    if divisor_invalido(divisor):
        return

    quociente = dividendo // divisor

    resto = dividendo % divisor

    return (quociente, resto)

print('div(10, 4) ==>', div(10, 4)) # dividento=10 e divisor=4

print('div(10, 0) ==>', div(10, 0)) # dividento=10 e divisor=0

print('div_qr(10, 4) ==>', div_qr(10, 4)) # dividento=10 e divisor=4

# argumentos da funções ( é possível passar os valores dos argumentos em uma ordem diferente, mas neste caso precisamos declarar o nome dos argumentos na chamada da função, conforme o exemplo a seguir.)

# calcula a área de um triângulo: (b x h) / 2

def area_triangulo(base, altura): 

 return (base * altura)/2

print(area_triangulo(altura=10, base=5)) # pode dar erro se passar só 1 argumento quando chama a função

# existe também argumentos predefinidos argumentos default isso permite que os argumentos da função possam ter um valor predefinido, pode atribuir um valor padrão para um argumento por meio do operador de atribuição ( = )

def exibe_pessoa(nome, idade=30): 

 print(f'Meu nome é {nome} e tenho {idade} anos.')

exibe_pessoa('Antônio')

exibe_pessoa('Antônio', 36)

# modulos ( são bibliotecas em python feito por outros devs assim a gente pode reaproveitar esses códigos já prontos para o projetos )

  # criação e importação de módulos ( Um módulo em Python nada mais é do que um arquivo texto contendo códigos com declarações de variáveis ou funções esses módulos são sempre salvos com extensão .py )

  # Nós utilizamos módulos para poder organizar (modularizar) => ( organizar por módulos ) os nossos códigos de acordo com as funcionalidades de cada conjunto de funções.

  # Por exemplo, se estivéssemos desenvolvendo um programa para geometria, poderíamos ter um módulo para cada um das figura geométrica (quadrado, triangulo, círculo etc.) ou então um módulo para cada todos os tipos de cálculo geométrico (área, volume, perímetro etc.)

  # a criação dos módulos é essencial para a modularização dos programas, principalmente aqueles com milhares de linhas de código.

  # Por exemplo, vamos criar um modulo (arquivo), chamado areas que contém funções básicas para o cálculo da área de diferentes figuras geométricas. Para tanto, primeiro precisamos criar um arquivo e em seguida salvá-lo com o nome areas.py. Em seguida, basta adicionarmos o conteúdo do módulo, que são as funções que irão realizar os cálculos:

# Em Python, a utilização de códigos externos é realizada por meio da importação de módulos, com a sintaxe: import <modulo>. Portanto, para importamos o nosso módulo de exemplos, devemos utilizar a instrução:

import areas

# Entretanto, a importação não significa que já importamos todos os nomes de funções e variáveis declaradas no módulo diretamente. Nós apenas importamos o nome do areas, e a partir deste nome podemos acessaras as declarações contidas no módulo:

import areas

print(areas.triangulo(5, 8))

# para ter acesso direto a todos as declarações do módulo inclusive o PI

from areas import *

print(triangulo(5, 8))

print(quadrado(6))

print(PI)

# O comando from import possibilita a importação de todas as declarações de um módulo, como o exemplo anterior, ou a importação de algumas declarações específicas, como o exemplo a seguir. Desta forma, apenas as funções quadrado() e circulo() estarão disponíveis para utilização no código.

from areas import quadrado, circulo

# Também é possível atribuirmos um novo nome para o módulo quando realizamos a importação, da seguinte forma:

import areas as ar

print(ar.triangulo(5, 8))

print(ar.quadrado(6))

# modulos embutidos em python ( O Python possuí vários módulos já embutidos na linguagem, que oferecem diversas funcionalidades úteis ao desenvolvedor. Estes módulos são desenvolvidos e mantidos pela comunidade responsável pela linguagem e são exaustivamente testados e otimizados antes de serem lançados aos usuários finais. A seguir iremos exemplificar alguns dos módulos embutidos mais conhecidos e utilizados pelos desenvolvedore )

# modulo com funções matemáticas para cálculos mais complexos

import math

print('Função cosseno:', math.cos(100))

print('Função log:', math.log(10))

# modulo para construção de sequências elaboradas

import itertools

print(list(itertools.combinations('ABCD', 3))) # combinação de 3 em 3

print(list(itertools.permutations(['a', 'b', 'c'], 2))) # permutação de 2 em 2

# modulo para criação de números e sequências randômicas

import random

print('Numero aleatório entre 0 e 1:', random.random())

print('Inteiro aleatório entre 50 e 100:', random.randint(50, 100))

# modulo para funcionalidades que dependem do sistema operacional

import os

os.mkdir('pasta') # cria um diretório chamado pasta 

print('Caminho completo:', os.path.join('/home/antonio', 'pasta', 'arquivo.txt'))

# instalação de novos módulos ( existe também varios módulo que são desenvolvidos e mantidos por terceiros O módulo, ou um conjunto deles, pode ser disponibilizado na forma de packages, "empacotando" os códigos em um arquivo)

  # o repositorio oficial do python tem mais de 360 mil de pacotes disponível para download

  # a principal forma de instala um pacote é utilizando o pip, pip install <pacote>

# o pacote mais utilizado na ciência de dados para manipulação e analise de dados é o pandas essa é a forma para instalar o pacote, pip install pandas

  # Se necessário podemos também especificar uma versão específica do pacote para a instalação: pip install pandas==1.3.5

  # Também é possível atualizar um pacote para a sua versão mais atual, utilizando o pip: pip install --upgrade pandas

# manipulação de arquivos Criação, Abertura e Fechamento de Arquivos

  # A criação de arquivos (e, consequentemente, a abertura deles), é realizada por meio da função open(arquivo, modo), que permite criar e/ou abrir um arquivo com o nome (arquivo) especificado como argumento.

  # 'r' Modo somente leitura (modo padrão). ( pode ser combinado com o 't' e 'b')

  # 'w' Modo de escrita. Cria um arquivo, caso ainda não exista, ou substitui o arquivo atual. ( se o arquivo ja existir ele pode apaga os dados do arquivo anterior e permitir escrever novos dados ) ( pode ser combinado com 't' e 'b' )

  # 'x' Modo de escrita. Cria um arquivo e, se o arquivo já existir, retorna um erro.

  # 'a' Modo de escrita. Cria um arquivo, caso ainda não exista. Se o arquivo já existir, novas escritas serão adicionadas ao final dele. ( Pode ser combinado com os modos "t" ou "b", para abrir o arquivo no modo de texto ou binário, respectivamente. )

  # 't' Abre o arquivo no modo texto (modo padrão). ( Pode ser combinado com os modos "r", "w", "x" ou "a". )

  # 'b' Abre o arquivo no modo binário. ( Pode ser combinado com os modos "r", "w", "x" ou "a". )

# para abrir um arquivo em modo leitura

arquivo = open("cidades.txt", "r")

arquivo.close() # .close() serve para fechar o arquivo para não perder os dados e não ser corrompido

# leitura de arquivos ( existe três maneiras de ler arquivos a primeira é lendo todo o arquivo e retornando armazenando em uma variavel e utiliza-se o método read() que retorna os dados do arquivo em str)

arquivo = open('cidades.txt', 'r')

linhas = arquivo.read()

arquivo.close()

print(linhas)

# Outra maneira é a leitura das linhas do arquivo por meio do método readlines(). Este método retorna uma lista de strings, onde cada elemento da lista corresponde à uma linha do arquivo:

arquivo = open('cidades.txt', 'r')

linhas = arquivo.readlines()

arquivo.close()

print(linhas) # mais esse método retorna quebra de linha \n para cada item da lista precisa de um novo tratamento para remove-las

# pode-se criar outra lista (novas_linhas) onde, para cada elemento da lista anterior, fosse aplicado o método rstrip() ( rstrip() remove caracteres em branco e quebras de linha ao final de uma string )

novas_linhas = []

for linha in linhas:

    novas_linhas.append(linha.rstrip())

print(novas_linhas)

# a última maneira é iterar sobre as linhas do arquivo

arquivo = open('cidades.txt', 'r')

for linha in arquivo:

 print(linha.rstrip())

arquivo.close()

# escrita de arquivo ( agora vamos adicionar informações ao arquivo das proximas cidades no final do arquivo, podemos utilizar dois métodos. Mas antes é necessário abrirmos o arquivo em modo de escrita e de adição de dados no seu final (modo 'a'))

  # o primeiro metodo é o write('texto') que recebe como parâmetro a str que será inserido no final do arquivo

arquivo = open('cidades.txt', 'a')

arquivo.write('\nRJ; São Gonçalo; 1031903\n')

arquivo.close()

# o segundo método é writelines(linhas) que possibilita a escrita de diversos textos de uma só vez, utilizando como parâmetro uma estrutura de dados que seja iterável (ex.: list ou tuple).

linhas = [

 '\nAL; Maceió; 1005319\n',

 '\nRJ; Duque de Caxias; 878402\n',

 '\nRN; Natal; 862044\n',

 '\nMS; Campo Grande; 843120\n'

]

arquivo = open('cidades.txt', 'a')

arquivo.writelines(linhas)

arquivo.close()

# compreensão de listas ( list comprenhesion ) É um conceito que permite otimizar a criação de novas listas e, de quebra, diminuir o número de linhas de código. este recurso é mais eficiente do que o modo tradicional de criação, pois requer um uso menor de memória e a operação é realizada em menos tempo.

  # Por exemplo, tradicionalmente, para criar uma lista dos números de 1 a 10 elevado à potência 2, seria utilizado o seguinte bloco de código:

potencias = []

for item in range(1, 11):

 potencias.append(item ** 2)

print(potencias)

# A mesma operação pode ser reescrita da seguinte forma, utilizando compreensão de listas:

potencias = [item ** 2 for item in range(1, 11)] # uma lista dentro tem o loop que itera adicionando cada numero a variavel item e o cálculo é feito e o valor adicionando a lista potencias

print(potencias)

# Abaixo são apresentados mais alguns exemplos:

print( [n * 10 for n in range(1, 16)] ) # Multiplica por 10 os números de 1 a 15

print( [c.upper() for c in 'antonio'] ) # Cria lista com os caracteres em maísculo

print( [(n % 2 == 0) for n in range(0, 10)] ) # Indica se n é par ou não

# agora precisamos cria uma lista dos numeros de 1 a 10 elevado a 2 mais apenas so numeros impares devem ser considerado e os numeros pares descartado então precisa de uma condição para fazer a verificação Tradicionalmente, pode-se resolver este problema com o seguinte trecho de código:

potencias = []

for item in range(1, 11):

    if item % 2 != 0:

        potencias.append(item ** 2)

print(potencias)

# Observe que o código tem um fluxo condicional que verifica se o número é ímpar ou não (if item % 2 != 0). Por sorte, o recurso de compreensão de listas também permite que seja realizado essa verificação, com a seguinte sintaxe:

potencias = [item ** 2 for item in range(1, 11) if item % 2 != 0] # uma lista dentro tem o loop que itera adicionando cada numero a variavel item o if verifica se o numero é ímpar e o valor é adicionando a lista potencias

print(potencias)

# compreensão de dicionário ( dict comprenhesion ) Com uma sintaxe bem semelhante à compreensão de listas, podem ser utilizados com ou sem a verificação condicional

  # Considere o mesmo problema abordado anteriormente (números de 1 a 10 elevados a potência 2). Entretanto, deseja-se criar um dicionário onde a chave é o próprio número e o valor é o número elevado à potência 2. Abaixo, os dois trechos de código apresentam a solução tradicional, para todos os números e para apenas os números ímpares:

# todos os números elevado à potência 2

dict_todos = {}

for item in range(1, 11):

 dict_todos[item] = item ** 2

print('Todos numeros:', dict_todos)

# apenas números ímpares elevado à potência 2

dict_impares = {}

for item in range(1, 11):

 if item % 2 != 0:

   dict_impares[item] = item ** 2

print('Números ímpares:', dict_impares)

# usando a compreensão de dicionário o código pode ser dessa forma

# todos os números elevado à potência 2

dict_todos = {item: item ** 2 for item in range(1, 11)}

print('Todos numeros:', dict_todos)

# apenas números ímpares elevado à potência 2

dict_impares = {item: item ** 2 for item in range(1, 11) if item % 2 != 0}

print('Números ímpares:', dict_impares) # as compreensões deixam o código mais elegante e pythoninco

# funções anonimas ( funções lambda ) lambda é uma função sem nome por isso que é anônima ela pode ter varios argumentos mais só uma expressão

# Declaração da função

area_quadrado = lambda lado: lado ** 2 # a palavra lado que vem depois de lambda é o argumento e depois a expressão

# Utilização

print(area_quadrado(4)) # essa função é util quando precisamos de uma função específica em curto perido 

# Geralmente utilizamos estas funções em conjunto com outras funções que possuem como argumento outra função, como por exemplo a função map(), que permite que apliquemos uma função em todos os elementos de uma lista, como no exemplo a seguir.

# Função que calcula o triplo de número

triplo = lambda x: x * 3

# Calcula o triplo dos números de uma lista

lista = [4, 5, 9, 7, 0, 1, 8]

print(list(map(triplo, lista)))

# Ou poderíamos fazer de um jeito mais pythonico ainda, em apenas uma linha:

print(list(map(lambda x: x * 3, [4, 5, 9, 7, 0, 1, 8])))

# Atribuição Condicional em Uma Linha, pense em um código que cria uma variavel var, e atribui a ela um valor de acordo com uma das seguintes condições: Se o nome do programador tiver mais de 5 letras, o valor de var deverá ser 100. Caso contrário (o nome tem 5 ou menos letras), o valor de var deverá ser 0.Tal código pode ser escrito da seguinte forma:

nome = 'antonio'

if len(nome) > 5:

 var = 100

else:

 var = 0

print('O valor de var é:', var)

# o python tem um operador ternario que é utlizado para atribuição de um valor a variavel, condicionado a uma verificação de uma expressão

nome = 'antonio'

var = 100 if len(nome) > 5 else 0

print('O valor de var é:', var)
