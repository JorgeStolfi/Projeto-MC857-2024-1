#! /usr/bin/python3

# Este programa executável Python3 é o daemon servidor HTTP do website do projeto de MC857.
#
# Ele roda sem parar no computador local ou no computador host do projeto, escutando
# na porta internet 8081. Ao receber um comando HTTP (GET, POST, ou
# HEAD) enviado por um usuário, ele chama outros módulos do projeto para
# criar uma página HTML5 com a resposta aproriada, e envia a mesma de
# volta para o usuário.

# Interfaces do projeto usadas por este programa:
import db_base_sql
import db_tabelas
import processa_comando_http
import sys

def dispara():
  """Esta função inicia a execução do servidor."""
  
  sys.stderr.write("conectando com a base de dados...\n")
  dir = "DB"
  usr = None
  senha = None
  res = db_base_sql.conecta(dir,usr,senha); assert res == None
  
  sys.stderr.write("inicializando as tabelas de objetos...\n")
  testando = True # Que base de dados deve usar?
  if testando:
    # Inicializa a base com algumas entradas para testes:
    db_tabelas.cria_todos_os_testes(False)
  else:
    # Usa a base de dados existente:
    limpa = False # Começa com tabelas vazias?
    db_tabelas.inicializa_todas(limpa)
  sys.stderr.write("criando o objeto servidor...\n")
  host = '0.0.0.0' # Aceita pedidos de qualquer IP.
  porta = 8081 # Porta 8081 em vez de 80, para não precisar de acesso "root"
  objeto_servidor = processa_comando_http.cria_objeto_servidor(host,porta)
  
  sys.stderr.write("disparando o processo servidor...\n")
  objeto_servidor.serve_forever()

# Programa principal do servidor:
dispara()
 
