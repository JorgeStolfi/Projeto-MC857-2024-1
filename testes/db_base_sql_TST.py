#! /usr/bin/python3

import sys
import db_base_sql

db_base_sql.conecta("DB",None,None)
nome_tb = "testabela"
num_ents = 0
descr_cols = \
  "indice integer PRIMARY KEY," + \
  "nome varchar(40) NOT NULL," + \
  "cpf char(14) NOT NULL," + \
  "cep char(9) NOT NULL," + \
  "peso fixed(8,2)," + \
  "pernas int(4)"

def testa_insert(atrs):
  global nome_tb, num_ents
  sys.stderr.write("  > testando INSERT:\n")
  res = db_base_sql.executa_comando_INSERT(nome_tb,atrs)
  sys.stderr.write("    > resultado: " + str(res) + "\n\n")
  num_ents += 1
  
def do_various_tests(rot_teste):
  global nome_tb, num_ents
  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write(rot_teste + "\n")

  testa_insert({ 'nome': 'zeca', 'cpf': '123.456.789-10', 'cep':  '13083-851', 'peso':  30.22, 'pernas': 3 })
  testa_insert({ 'nome': 'juca', 'cpf': '987.654.321-00', 'cep':  '13083-851', 'peso': 120.01, 'pernas': 2 })
  testa_insert({ 'nome': 'caco', 'cpf': '111.222.333-44', 'cep':  '13083-851', 'peso':  12.10, 'pernas': 4 })
  
  sys.stderr.write("  > testando num_entradas:\n")
  res =  db_base_sql.num_entradas(nome_tb, 'indice');
  sys.stderr.write("    resultado: " + str(res) + "\n\n")
  if type(res) is int:
    assert res == num_ents

  sys.stderr.write("    > testando UPDATE:\n")
  res = db_base_sql.executa_comando_UPDATE(nome_tb, "nome = 'juca'", { 'cep': '13083-705' })
  sys.stderr.write("      resultado: " + str(res) + "\n\n")

  sys.stderr.write("    > testando SELECT:\n")
  res = db_base_sql.executa_comando_SELECT(nome_tb,"cep = '13083-851'", ('nome', 'cpf' ))
  sys.stderr.write("      resultado: " + str(res) + "\n\n")

  sys.stderr.write("    > testando DELETE:\n")
  res = db_base_sql.executa_comando_DELETE(nome_tb, "nome =  'juca'")
  sys.stderr.write("      resultado: " + str(res) + "\n\n")
  num_ents -= 1

  sys.stderr.write("    > testando SELECT:\n")
  res = db_base_sql.executa_comando_SELECT(nome_tb,"cep ='13083-851'", ('nome', 'cpf' ))
  sys.stderr.write("      resultado: " + str(res) + "\n\n")

  testa_insert({ 'nome': 'sara', 'cpf': '123.321.123-45', 'cep': '13083-852', 'peso':  45.99, 'pernas': 3 })

  sys.stderr.write("    > testando SELECT:\n")
  res = db_base_sql.executa_comando_SELECT(nome_tb,"pernas = 3", ('nome', 'cpf', 'peso', 'pernas' ))
  sys.stderr.write("      resultado: " + str(res) + "\n\n")

  sys.stderr.write("%s\n" % ("-" * 70))
  return
 
sys.stderr.write("  > testando TABLE_EXISTS (sem tabela):\n")
res = db_base_sql.executa_comando_TABLE_EXISTS (nome_tb)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
assert type(res) is bool and not res # Meaning does not exist
 
sys.stderr.write("  > testando DROP_TABLE sem tabela:\n")
res = db_base_sql.executa_comando_DROP_TABLE(nome_tb)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
assert res == None # Meaning OK
 
sys.stderr.write("  > testando CREATE_TABLE:\n")
res = db_base_sql.executa_comando_CREATE_TABLE (nome_tb, descr_cols)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
assert res == None # Meaning OK
 
sys.stderr.write("  > testando TABLE_EXISTS (cem tabela):\n")
res = db_base_sql.executa_comando_TABLE_EXISTS (nome_tb)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
assert type(res) is bool and res # Meaning exists

do_various_tests("  > testes com tabela existente")

sys.stderr.write("  > testando DROP_TABLE:\n")
res = db_base_sql.executa_comando_DROP_TABLE(nome_tb)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
 
sys.stderr.write("  > testando TABLE_EXISTS (de novo sem tabela):\n")
res = db_base_sql.executa_comando_TABLE_EXISTS (nome_tb)
sys.stderr.write("    resultado: " + str(res) + "\n\n")
assert type(res) is bool and not res # Meaning does not exist

do_various_tests("  > testes com tabela destruída")

sys.stderr.write("Testes terminados normalmente.\n")
