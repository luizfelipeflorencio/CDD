import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula_final",
)

cont = 1

while cont != 3:
    cont = int(input("\nMenu: \n"
                     "1 Para ver a tabela \n"
                     "2 Para inserir o aluno \n"
                     "3 Para sair do sistema \n"
                     ))

    if cont == 1:
        meucursor = banco.cursor()
        pesquisa = 'select * from alunos;'
        meucursor.execute(pesquisa)
    # fetchall recebe tudo da pesquisa e retorna atraves de uma tupla(lista que não pode alterar um item)
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)


    elif cont == 2:
        nome=input("Digite o nome do aluno: ")
        telefone=int(input("Digite o numero do aluno: "))
        sql = "insert into alunos (nome,telefone) values (%s,%s)"
        data = (nome,telefone)
        meucursor.execute(sql,data)
        banco.commit()

    elif cont == 3:
        meucursor.close()
        banco.close()
        print("Sistema finalizado")