# tipos primitivos de dados em python
# int
x = 817  # x esta atribuido ao valor 817
v = -x # a variável esta retornando a primeira variavel com o valor negativo e continua int
print(x,v)

# float
f = 28.39
a = -f
print(f,a)

# bool
ds = True # 1
we = False # 0
print(ds,we)

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

# tipos não primitivo ( estrutura de dados ) ( Listas [list] Tuplas (tuple) Dicionários {dict} Conjuntos {set} String 'str' )
# str
q = 'str com aspas simples são mais usado para deixa o código legivel e serve para coloca "aspas duplas" dentro\n' # \n essa função faz quebra de linha
s = "str com aspas duplas serve para coloca 'aspas simples' dentro"
z = '''\te existe str com aspas triplas que serve para coloca 'aspas simples' e "aspas duplas" dentro

da para fazer multi quebras de linhas e multi    espaços''' # a função \t adiciona um espaço horizontal
print(q, s, z)

# list
# criação de Listas e Acesso dos Elementos ( existe list homogênea os elementos são do mesmo tipo ) ( existe list heterogêneo os elementos são diferentes tipos )
s = [2, 'a', 5.44, True] # lista com valores heterogêneo
print(s)
c = ['um', 'dois', None, 4] # lista com valor nulo dentro
print(c)
l = [0, 1] # listas com outras listas dentro (listas aninhadas)
l = [l, 'dois', 'três', [4, 5], 'seis']
print(l)
i = [] # lista vazia
print(i)
