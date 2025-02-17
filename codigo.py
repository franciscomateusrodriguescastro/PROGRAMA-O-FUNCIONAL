# Função lambda
quadrado = lambda x: x ** 2

# List comprehension
numeros = [1, 2, 3, 4, 5]
quadrados = [quadrado(x) for x in numeros]

# Closure
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

saudar_ola = criar_saudacao("Olá")
mensagem = saudar_ola("João")

# Função de alta ordem
def aplicar_funcao(func, valor):
    return func(valor)

resultado = aplicar_funcao(quadrado, 5)

print(quadrados)  # Saída: [1, 4, 9, 16, 25]
print(mensagem)   # Saída: Olá, João!
print(resultado)  # Saída: 25