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
