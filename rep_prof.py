# repositorio do modulo de professores, com as funcoes criar, ler, editar, listar e apagar
professores = []  # Criando uma lista.


# Definindo as Funções:

def pede_nome_prof():  # Função para pedir o nome.
    nome = input("Nome do prof: ")
    return (nome)


def pede_cpf_prof():  # Função para pedir o cpf.
    cpf = input("CPF do prof: ")
    return (cpf)


def pede_departamento():  # Função para pedir o departamento.
    return (input("Departamento do prof: "))




def listar_dados(nome, cpf, departamento):  # Função que mostra todos os dados do prof.
    print("Nome: %s\nCpf: %s\nDepartamento: %s" % (nome, cpf, departamento))


def pesquisa(nome):  # Função para pesquisar professor.
    name = nome.lower()  # Convertendo todas as letras em minúsculas.
    for d, e in enumerate(professores):  # Executando o loop.
        if e[0].lower() == name:  # Determinando uma condição.
            return d  # Executa caso a condição for verdadeira.
    return None  # Executa caso a condição for falsa.
3
"""
* Foi atribuído o metodo lower para que não haja problemas
quando usuário digitar maiusculo e programa não reconhecer.
* A função enumerate serve para acessar a posição do elemento
e o próprio elemento.
* Função return para indicar o valor a retornar.
* Função return None,caso o dado não seja encontrado, não vai retornar nada.
"""


def novo():  # Função para adicionar novo prof.
    global professores  # Definindo variável como Global.
    nome = pede_nome_prof()  # Entrada de dados.
    cpf = pede_cpf_prof()  # Entrada de dados.
    departamento = pede_departamento()  # Entrada de dados.
    professores.append([nome, cpf, departamento])  # Adicionando os dados na lista
    with open("professores.txt", "w") as f:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
        for professor in professores:
            f.write("Nome do prof: {}, Cpf do prof: {}, Departamento do prof: {}".format(professor[0],professor[1],professor[2]))
            f.write("\n")


"""
* Está sendo utilizada a variável global pois será possível o acesso
da mesma tanto dentro como fora da função, ou seja, pode ser acessada
por todas as funções do programa.
* Está sendo utilizado o método append para ser possível adicionar
novos dados durante a execução do programa na  lista.
"""


def apagar():  # Função para apagar um prof.
    global professores  # Definindo variável como Global.
    nome = pede_nome_prof()  # Entrada de dados.
    p = pesquisa(nome)  # Cria uma variável e chama a função pesquisa.
    if p != None:  # Determinando uma condição.
        del professores[p]  # Executa caso a condição for verdadeira.
        with open("professores.txt","w") as file:  #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for professor in professores:
                file.write("Nome do prof: {}, Cpf do prof: {}, Departamento do prof: {}".format(professor[0],professor[1],professor[2]))
                file.write("\n")
    else:
        print("Prof não encontrado.")  # Executa caso a condição for falsa.


def editar():  # Função para editar um prof.
    p = pesquisa(pede_nome_prof())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = professores[p][0]  # Procurando os dados na lista.
        cpf = professores[p][1]  # Procurando os dados na lista.
        departamento = professores[p][2]  # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, cpf, departamento)  # Mostra os dados.
        del professores[p]
        nome = pede_nome_prof()  # Entrada dos novos dados editados.
        cpf = pede_cpf_prof()  # Entrada dos novos dados editados.
        departamento = pede_departamento()  # Entrada dos novos dados editados.
        professores.append([nome,cpf,departamento])  # Armazenando os novos dados.
        with open("professores.txt", "w") as f: #Utilizando as keywords with open para abrir, em modo write, o arquivo sem que precise fechá-lo toda vez
            for professor in professores:
                f.write("Nome do prof: {}, Cpf do prof: {}, Departamento do prof: {}".format(professor[0], professor[1],
                                                                                             professor[2]))
                f.write("\n")
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.


def listar():  # Função para mostrar lista de prof.
    print("\n\n\n------")
    for e in professores:
        listar_dados(e[0], e[1], e[2])
        print("------\n")
        with open("professores.txt","r") as file: #Utilizando as keywords with open para abrir, em modo leitura, o arquivo sem que precise fechá-lo toda vez
            file.read()



def pesquisar():  # Função para Pesquisar os prof.
    p = pesquisa(pede_nome_prof())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = professores[p][0]  # Procurando os dados na lista.
        cpf = professores[p][1]  # Procurando os dados na lista.
        departamento = professores[p][2]  # Procurando os dados na lista.
        print("Encontrado:")  # Exibi informação na tela.
        listar_dados(nome, cpf, departamento)  # Mostra os dados.
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.
