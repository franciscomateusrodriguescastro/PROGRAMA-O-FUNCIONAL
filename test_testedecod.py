import unittest
from testedecod import inserir_novo_aluno, remover_aluno_por_matricula, exibir_lista_de_alunos

class TesteDecod(unittest.TestCase):

    def setUp(self):
        self.alunos = [
            {"nome": "Carla Alves", "idade": 20, "matricula": 2314457},
            {"nome": "Marcos Lima", "idade": 22, "matricula": 2314587},
            {"nome": "Maria Silva", "idade": 20, "matricula": 2315547},
            {"nome": "João Lucas", "idade": 20, "matricula": 2311698}
        ]

    def test_inserir_novo_aluno(self):
        novo_aluno = {"nome": "Ana Paula", "idade": 21, "matricula": 2319999}
        alunos_atualizados = inserir_novo_aluno(self.alunos, novo_aluno["nome"], novo_aluno["matricula"], novo_aluno["idade"])
        self.assertIn(novo_aluno, alunos_atualizados)

    def test_remover_aluno_por_matricula(self):
        matricula_para_remover = 2314587
        alunos_atualizados = remover_aluno_por_matricula(self.alunos, matricula_para_remover)
        self.assertNotIn({"nome": "Marcos Lima", "idade": 22, "matricula": 2314587}, alunos_atualizados)

    def test_exibir_lista_de_alunos(self):
        lista_esperada = (
            "Carla Alves - Matrícula: 2314457, Idade: 20\n"
            "Marcos Lima - Matrícula: 2314587, Idade: 22\n"
            "Maria Silva - Matrícula: 2315547, Idade: 20\n"
            "João Lucas - Matrícula: 2311698, Idade: 20"
        )
        self.assertEqual(exibir_lista_de_alunos(self.alunos), lista_esperada)

if __name__ == '__main__':
    unittest.main()