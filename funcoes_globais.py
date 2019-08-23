# repositorios com funções que serao usadas em todo o programa
import rep_prof
import rep_aluno
import rep_disciplina
import rep_turma


def menu_principal():  # Função que exibe o menu de opções.
    while True:
        print("""
                          1 - Professor
                          2 - Aluno
                          3 - Disciplina
                          4 - Turmas
                          0 - Sair do programa
                       """)
        try:    #O bloco try-except serve para lançar uma exceção caso seja digitado algo fora de 0 a 4
            opcao = int(input())
            if opcao == 0:
                break
            elif opcao == 1:
                menu_prof()
            elif opcao == 2:
                menu_alunos()
            elif opcao == 3:
                menu_disciplinas()
            elif opcao == 4:
                menu_turmas()
        except ValueError:
            print("Opcao invalida")




def menu_prof():  # Função que exibe o menu de opções de professores.

    while True:
        print("""
                           1 - Adicionar novo professor
                           2 - Editar um professor
                           3 - Pesquisar professor
                           4 - Lista de professor
                           5 - Apagar um professor
                           0 - Sair
                        """)
        try:  #O bloco try-except serve para lançar uma exceção caso seja digitado algo fora de 0 a 5
            opcao = int(input())
            if opcao == 0:
                break
            elif opcao == 1:
                rep_prof.novo()
            elif opcao == 2:
                rep_prof.editar()
            elif opcao == 3:
                rep_prof.pesquisar()
            elif opcao == 4:
                rep_prof.listar()
            elif opcao ==5:
                rep_prof.apagar()
        except ValueError:
            print("Opcao nao valida")




def menu_alunos():  # Função que exibe o menu de opções de alunos.

    while True:
        print("""
                          1 - Adicionar novo aluno
                          2 - Editar um aluno
                          3 - Pesquisar aluno
                          4 - Lista de aluno
                          5 - Apagar um aluno
                          0 - Sair
                       """)
        try:     #O bloco try-except serve para lançar uma exceção caso seja digitado algo fora de 0 a 5

            opcao = int(input())
            if opcao == 0:
                break
            elif opcao == 1:
                rep_aluno.novo()
            elif opcao == 2:
                rep_aluno.editar()
            elif opcao == 3:
                rep_aluno.pesquisar()
            elif opcao == 4:
                rep_aluno.listar()
            elif opcao ==5:
                rep_aluno.apagar()
        except ValueError:
            print("opcao nao valida")



def menu_disciplinas():  # Função que exibe o menu de opções de disciplinas.

    while True:
        print("""
                          1 - Adicionar novo disciplina
                          2 - Editar uma disciplina
                          3 - Pesquisar disciplina
                          4 - Lista de disciplina
                          5 - Apagar uma disciplina
                          0 - Sair
                       """)
        try:     #O bloco try-except serve para lançar uma exceção caso seja digitado algo fora de 0 a 5

            opcao = int(input())
            if opcao == 0:
                break
            elif opcao == 1:
                rep_disciplina.novo()
            elif opcao == 2:
                rep_disciplina.editar()
            elif opcao == 3:
                rep_disciplina.pesquisar()
            elif opcao == 4:
                rep_disciplina.listar()
            elif opcao ==5:
                rep_disciplina.apagar()
        except ValueError:
            print("opcao nao valida")




def menu_turmas():  # Função que exibe o menu de opções de turmas.

    while True:
        print("""
                                1 - Adicionar novo turma
                                2 - Editar uma turma
                                3 - Pesquisar turma
                                4 - Lista de turma
                                5 - Apagar uma turma
                                0 - Sair
                             """)
        try:     #O bloco try-except serve para lançar uma exceção caso seja digitado algo fora de 0 a 5
            opcao = int(input())
            if opcao == 0:
                break
            elif opcao == 1:
                rep_turma.novo()
            elif opcao == 2:
                rep_turma.editar()
            elif opcao == 3:
                rep_turma.pesquisar()
            elif opcao == 4:
                rep_turma.listar()
            elif opcao ==5:
                rep_turma.apagar()
        except ValueError:
            print("opcao nao valida")










