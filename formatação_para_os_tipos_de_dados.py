# Formatação de Str ( str literais formatadas ) f-str
nascimento = 1986
ano_atual = 2022
print(f'Eu tenho {ano_atual - nascimento} anos') # é possível usa operadores aritméticos no f-str

# também é possível usa metodos e funções no f-str
print(f'exemplo de f-str com um valor de 10 é uma expressão {10 == 15}')
palavra = 'consolação'
print(f'A palavra {palavra.upper()} possuí {len(palavra)} letras')

# formatação
orcamento = 7000
vlr_gasto = 430
pct = (vlr_gasto/orcamento) * 100 # multiplicado por 100 para resultado em porcentagem
print(f'Porcentagem já gasta do orçamento: {pct:.2f}%') #(.2f f nesse caso serve para indicar que o valor será formatado como float com duas casas decimais, que sera arredondado.) ( para baixo nesse caso )

# outra formatação para arredondar o numero
orcamento = 7000
vlr_gasto = 430
pct = (vlr_gasto/orcamento)
print(f'Porcentagem já gasta do orçamento: {pct:.2%}') # com o símbolo de porcentagem ( % ) permite declarar que o valor é uma porcentagem, assim não é necessário multiplica por 100
