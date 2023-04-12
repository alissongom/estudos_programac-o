# Operações de Acesso das Str [indice] (o espaço também conta como caractere)
# o acesso a indice positivo sempre começa com 0 e o acesso com indice negativo começa com -1
# indices positivo
qpw = 'consolação'
print('primeira letra da str: ',qpw[0]) # c
print('ultima letra da str: ',qpw[9]) # o
print('pega a letra L da str: ',qpw[5]) # l

# indices negativos
print('pega a primeira letra da str: ',qpw[-10]) # c
print('pega a ultima letra da str: ', qpw[-1]) # 0
print('pega a letra L da str: ',qpw[-5]) # L

# também é possível fazer uma sub-str que é uma str feita pela str original
print(qpw[3:6]) # palavra sol
print(qpw[-4:]) # palavra ação
print(qpw[3:7]) # palavra sola
print(qpw[:7]) # palavra consola
print('pega algumas letras da palavra: ',qpw[0:1:3:4]) # coso
print('inverte a str: ',qpw[::-1]) # inverte a palavra

# operadores de string ( * repete a str N vezes ) ( + Concatena (une) duas strings em uma única )
jk = 'belo'
jn = 'horizonte'
# repetição
print(4 * jk) # retorna belobelobelobelo
print((jk + ',') * 4) # retorna belo 4 vezes com vírgula

# cocatenacão
print(jk + jn)
print(jk + ' ' + jn)
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
