import requests
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula_final",
)
meucursor = banco.cursor()

print("Verificando endereço")
nome= input("Digite o nome: ")
cep = input("Digite o cep: ")

link= f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)
endereco = requisicao.json()

cep1=endereco['cep']
logradouro= endereco['logradouro']
bairro=endereco['bairro']
localidade=endereco['localidade']
uf =endereco['uf']
sql = "insert into endereco (nome,cep,logradouro,bairro,localidade,uf) values (%s,%s,%s,%s,%s,%s)"
data = (nome,cep,logradouro,bairro,localidade,uf)
meucursor.execute(sql,data)
banco.commit()