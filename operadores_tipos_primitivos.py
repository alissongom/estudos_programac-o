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
# calculo grande precisa da logica de pemdas
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
c //= 3 # equivalente a c = c // 3
print(c)
b **= 3 # equivalente a b = b ** 3
print(b)

# operadores comparação
y = 48
yu = 10
uy = 29
print(y > uy) #True
print(y >= yu) #True
print(uy < yu) #False
print(uy <= yu) #False
print(uy == y) #False
print(y != uy) #True

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

# só é possível fazer comparação com outros operadores de comparação com str se for com o mesmo tipo de dado e é feito pela comparação lexicografica ( tabela unicode )
er = 'gato'
qs = 'largato'
li = 'cachorro'
print(li > qs) #False
print(qs < er) #False
print(li > er) #False
print(qs > li) #True

# operadores logicos and, or, not
cu = True
cool = 18
print(cool >= 12 and cu)#and só retorna True se os dois valores for verdadeiro

# or
ver = 12
fg = True
print(ver > 18 or fg) # or retorna True se 1 dos valores for verdadeiro

# e tem o operador not que inverte o valor de True para False e False para True
kj = 18
pr = False
print(not(kj > 18 or pr))
