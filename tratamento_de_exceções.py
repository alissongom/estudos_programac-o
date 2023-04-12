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
# o bloco de código pode ter varios except
