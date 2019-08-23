# repositorio do modulo de turma, com as funcoes criar, ler, editar, listar e apagar
import rep_prof
import rep_aluno
import rep_disciplina

turmas = []  # Criando uma lista.

# Definindo as Funções:

def pede_codigo_turma():  # Função para pedir o codigo da turma.
    return (input("Codigo da turma: "))


def pede_periodo():  # Função para pedir o periodo.
    return (input("Periodo: "))


def listar_dados(codigo_turma, periodo, codigo_disciplina, cpf_prof,cpf_aluno):  # Função que mostra todos os dados.
    print("Codigo da turma: %s\nPeriodo: %s\nCodigo da disciplina: %s\nCpf do prof: %s\nCpf do aluno: %s" % (codigo_turma, periodo, codigo_disciplina, cpf_prof,cpf_aluno))


def pesquisa(nome):  # Função para pesquisar turmas.
    name = nome.lower()  # Convertendo todas as letras em minúsculas.
    for d, e in enumerate(turmas):  # Executando o loop.
        if e[0].lower() == name:  # Determinando uma condição.
            return d  # Executa caso a condição for verdadeira.
    return None  # Executa caso a condição for falsa.


"""
* Foi atribuído o metodo lower para que não haja problemas
quando usuário digitar maiusculo e programa não reconhecer.
* A função enumerate serve para acessar a posição do elemento
e o próprio elemento.
* Função return para indicar o valor a retornar.
* Função return None,caso o dado não seja encontrado, não vai retornar nada.
"""


def novo():  # Função para adicionar nova turma.
    global turmas  # Definindo variável como Global.
    codigo_turma = pede_codigo_turma()  # Entrada de dados.
    periodo = pede_periodo()  # Entrada de dados.
    codigo_disciplina = rep_disciplina.pede_codigo_disciplina()  # Entrada de dados.
    cpf_prof = rep_prof.pede_cpf_prof()  # Entrada de dados.
    cpf_aluno = rep_aluno.pede_cpf_aluno()  # Entrada de dados.
    turmas.append([codigo_turma, periodo, codigo_disciplina, cpf_prof,cpf_aluno])  # Adicionando os dados na lista
    with open("turmas.txt","w") as file:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
        for turma in turmas:
            file.write("Codigo da turma: {}, Periodo: {}, Codigo da disciplina: {}, Cpf prof: {}, Cpf aluno: {}"  .format(turma[0], turma[1],turma[2],turma[3],turma[4]))
            file.write("\n")


"""
* Está sendo utilizada a variável global pois será possível o acesso
da mesma tanto dentro como fora da função, ou seja, pode ser acessada
por todas as funções do programa.
* Está sendo utilizado o método append para ser possível adicionar
novos dados durante a execução do programa na lista.
"""


def apagar():  # Função para apagar uma turma.
    global turmas  # Definindo variável como Global.
    codigo_turma = pede_codigo_turma()  # Entrada de dados.
    p = pesquisa(codigo_turma)  # Cria uma variável e chama a função pesquisa.
    if p != None:  # Determinando uma condição.
        del turmas[p]  # Executa caso a condição for verdadeira.
        with open("turmas.txt", "w") as file:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for turma in turmas:
                file.write(
                    "Codigo da turma: {}, Periodo: {}, Codigo da disciplina: {}, Cpf prof: {}, Cpf aluno: {}".format(
                        turma[0], turma[1], turma[2], turma[3], turma[4]))
                file.write("\n")
    else:
        print("Turma não encontrada.")  # Executa caso a condição for falsa.


def editar():  # Função para editar uma turma.
    p = pesquisa(pede_codigo_turma())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        codigo_turma = turmas[p][0]  # Procurando os dados na lista.
        periodo = turmas[p][1]  # Procurando os dados na lista.
        codigo_disciplina = turmas[p][2]  # Procurando os dados na lista.
        cpf_prof = turmas[p][3]  # Procurando os dados na lista.
        cpf_aluno = turmas[p][4]  # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(codigo_turma, periodo, codigo_disciplina, cpf_prof,cpf_aluno)  # Mostra os dados.
        del turmas[p]
        codigo_turma = pede_codigo_turma()  # Entrada dos novos dados editados.
        periodo = pede_periodo()  # Entrada dos novos dados editados.
        codigo_disciplina = rep_disciplina.pede_codigo_disciplina()  # Entrada dos novos dados editados.
        cpf_prof = rep_prof.pede_cpf_prof()# Entrada dos novos dados editados.
        cpf_aluno = rep_aluno.pede_cpf_aluno()  # Entrada dos novos dados editados.
        turmas.append([codigo_turma, periodo, codigo_disciplina, cpf_prof,cpf_aluno])  # Armazenando os novos dados.
        with open("turmas.txt", "w") as file:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for turma in turmas:
                file.write(
                    "Codigo da turma: {}, Periodo: {}, Codigo da disciplina: {}, Cpf prof: {}, Cpf aluno: {}".format(
                        turma[0], turma[1], turma[2], turma[3], turma[4]))
                file.write("\n")
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.


def listar():  # Função para mostrar lista de turmas.
    print("\n\n\n------")
    for e in turmas:
        listar_dados(e[0], e[1], e[2],e[3],e[4])
        with open("turmas.txt","r") as file:  #Utilizando as keywords with open para abrir, em modo leitura, o arquivo sem que precise fechá-lo toda vez
           file.read()
    print("------\n")


def pesquisar():  # Função para Pesquisar as turmas.
    p = pesquisa(pede_codigo_turma())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        codigo_turma = turmas[p][0]  # Procurando os dados na lista.
        periodo = turmas[p][1]  # Procurando os dados na lista.
        codigo_disciplina = turmas[p][2]  # Procurando os dados na lista.
        cpf_prof = turmas[p][3]  # Procurando os dados na lista.
        cpf_aluno = turmas[p][4] # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(codigo_turma, periodo, codigo_disciplina,cpf_prof,cpf_aluno)  # Mostra os dados.
    else:
        print("Turma não encontrada.")  # Executa caso a condição seja falsa.


