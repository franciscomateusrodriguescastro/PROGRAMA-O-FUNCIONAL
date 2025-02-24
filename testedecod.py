# Lista de alunos
alunos = [
    {"nome": "Carla Alves", "idade": 20, "matricula": 2314457},
    {"nome": "Marcos Lima", "idade": 22, "matricula": 2314587},
    {"nome": "Maria Silva", "idade": 20, "matricula": 2315547},
    {"nome": "João Lucas", "idade": 20, "matricula": 2311698}
]

# Lambda para inserir um novo aluno
inserir_novo_aluno = lambda alunos, nome, matricula, idade: alunos.append({"nome": nome, "matricula": matricula, "idade": idade}) or alunos

# Lambda para remover um aluno
remover_aluno_por_matricula = lambda alunos, matricula: [aluno for aluno in alunos if aluno["matricula"] != matricula]

# Lambda para exibir a lista de alunos
exibir_lista_de_alunos = lambda alunos: "\n".join([f"{aluno['nome']} - Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}" for aluno in alunos])

# Menu interativo
while True:
    print("\nMENU:")
    print("1 - Ver lista de alunos")
    print("2 - Adicionar aluno")
    print("3 - Remover aluno")
    print("4 - Sair")

    opcao = input("Escolha uma opo: ")

    if opcao in ["1", "2", "3", "4"]:
        opcao = int(opcao)


    if opcao == 1:
        print("\nLista de alunos:")
        print(exibir_lista_de_alunos(alunos))

    elif opcao == 2:
        nome = input("Nome: ")
        matricula = int(input("Matrícula: "))
        idade = int(input("Idade: "))
        alunos = inserir_novo_aluno(alunos, nome, matricula, idade)
        print("\nAluno cadastrado com sucesso!")
        print("\nLista de alunos atualizada:")
        print(exibir_lista_de_alunos(alunos))  

    elif opcao == 3:
        matricula = int(input("Digite a matrícula do aluno a ser removido: "))
        alunos = remover_aluno_por_matricula(alunos, matricula)
        print("\nAluno removido com sucesso!")
        print("\nLista de alunos atualizada:")
        print(exibir_lista_de_alunos(alunos))  

    elif opcao == 4:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!Escolha um número entre 1 e 4.")
