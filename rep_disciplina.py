# repositorio do modulo de disciplinas, com as funcoes criar, ler, editar, listar e apagar
disciplinas = []  # Criando uma lista.


# Definindo as Funções:

def pede_nome_disciplina():  # Função para pedir o nome.
    return (input("Nome da Disciplina: "))


def pede_codigo_disciplina():  # Função para pedir o codigo.
    return (input("Codigo da disciplina: "))


def listar_dados(nome, codigo,):  # Função que mostra todos os dados
    print("Nome: %s\nCodigo: %s\n" % (nome, codigo))


def pesquisa(nome):  # Função para pesquisar disciplina.
    name = nome.lower()  # Convertendo todas as letras em minúsculas.
    for d, e in enumerate(disciplinas):  # Executando o loop.
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

def novo():  # Função para adicionar nova disciplina.
    global disciplinas  # Definindo variável como Global.
    nome = pede_nome_disciplina()  # Entrada de dados.
    codigo = pede_codigo_disciplina()  # Entrada de dados.
    disciplinas.append([nome, codigo])  # Adicionando os dados na lista
    with open("disciplinas.txt","w") as file:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
        for disciplina in disciplinas:
            file.write("Nome: {}, Codigo: {}"  .format(disciplina[0], disciplina[1]))
            file.write("\n")
"""
* Está sendo utilizada a variável global pois será possível o acesso
da mesma tanto dentro como fora da função, ou seja, pode ser acessada
por todas as funções do programa.
* Está sendo utilizado o método append para ser possível adicionar
novos dados durante a execução do programa na lista.
"""


def apagar():  # Função para apagar uma disciplina.
    global disciplinas  # Definindo variável como Global.
    nome = pede_nome_disciplina()  # Entrada de dados.
    p = pesquisa(nome)  # Cria uma variável e chama a função pesquisa.
    if p != None:  # Determinando uma condição.
        del disciplinas[p]  # Executa caso a condição for verdadeira.
        with open("disciplinas.txt", "w") as file:   #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for disciplina in disciplinas:
                file.write("Nome: {}, Codigo: {}".format(disciplina[0], disciplina[1]))
                file.write("\n")
    else:
        print("Disciplina não encontrado.")  # Executa caso a condição for falsa.


def editar():  # Função para editar uma disciplina.
    p = pesquisa(pede_nome_disciplina())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = disciplinas[p][0]  # Procurando os dados na lista.
        codigo = disciplinas[p][1]  # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, codigo)  # Mostra os dados.
        del disciplinas[p]
        nome = pede_nome_disciplina()  # Entrada dos novos dados editados.
        codigo = pede_codigo_disciplina()  # Entrada dos novos dados editados.
        disciplinas.append([nome, codigo])  # Armazenando os novos dados.
        with open("disciplinas.txt", "w") as file:   #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for disciplina in disciplinas:
                file.write("Nome: {}, Codigo: {}".format(disciplina[0], disciplina[1]))
                file.write("\n")
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.


def listar():  # Função para mostrar lista de disciplina.
    print("\n\n\n------")
    for e in disciplinas:
        listar_dados(e[0], e[1])
    with open("disciplinas.txt","r") as file:   #Utilizando as keywords with open para abrir, em modo leitura, o arquivo sem que precise fechá-lo toda vez
        file.read()
    print("------\n")


def pesquisar():  # Função para Pesquisar as disciplinas.
    p = pesquisa(pede_nome_disciplina())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = disciplinas[p][0]  # Procurando os dados na lista.
        codigo = disciplinas[p][1]  # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, codigo)  # Mostra os dados.
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.



