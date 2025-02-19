# Lista de alunos
alunos = []

# função lambda para inserir um novo aluno
inserir_novo_aluno = lambda alunos, nome, matricula, idade: alunos.append({"nome": nome, "matricula": matricula, "idade": idade}) or alunos

# função lambda para exibir a lista de alunos
exibir_lista_de_alunos = lambda alunos: "\n".join([f"{aluno['nome']} - Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}" for aluno in alunos])

# Adicionando aluno pelo input
nome = input("Nome: ")
matricula = int(input("Matrícula: "))
idade = int(input("Idade: "))

# função lambda para adicionar o aluno
inserir_novo_aluno(alunos, nome, matricula, idade)

# Exibindo a lista de alunos
print("\nLista de alunos:")
print(exibir_lista_de_alunos(alunos))