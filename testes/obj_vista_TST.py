???
#! /usr/bin/python3

import obj_sessao

import db_base_sql 
import obj_usuario
import util_testes
from util_erros import erro_prog, mostra, aviso_prog

import sys

sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
obj_usuario.cria_testes(True)

sys.stderr.write("  Inicializando módulo {sessao}, limpando tabela:\n")
obj_sessao.inicializa_modulo(True)

ok_global = True # Vira {False} se um teste falha.

def verifica_sessao(rot_teste, ses, ident, dono, aberta, cookie, data):
  """Testes básicos de consistência do objeto {ses} da classe {obj_sessao.Classe}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  verificando sessão %s\n" % rot_teste)
  atrs = { 'dono': dono, 'aberta': aberta, 'cookie': cookie }
  ok = obj_sessao.verifica_criacao(ses, ident, atrs)
  
  if ses != None and type(ses) is obj_sessao.Classe:
    
    sys.stderr.write("  testando {obj_sessao.obtem_dono()}:\n")
    usr1 = obj_sessao.obtem_dono(ses)
    if usr1 != dono:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(dono),True)
      ok = False
      
    sys.stderr.write("  testando {obj_sessao.aberta()}:\n")
    aberta1 = obj_sessao.aberta(ses)
    if aberta1 != aberta:
      aviso_prog("retornou " + str(aberta1) + ", deveria ter retornado " + str(aberta),True)
      ok = False
       
    sys.stderr.write("  testando {obj_sessao.obtem_cookie()}:\n")
    cookie1 = obj_sessao.obtem_cookie(ses)
    if cookie1 != cookie:
      aviso_prog("retornou " + str(cookie1) + ", deveria ter retornado " + str(cookie),True)
      ok = False
      
    sys.stderr.write("  testando {obj_sessao.obtem_data_de_criacao()}:\n")
    data1 = obj_sessao.obtem_data_de_criacao(ses)
    if data != None and data1 != data:
      aviso_prog("retornou " + str(data1) + ", deveria ter retornado " + str(data),True)
      ok = False
 
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("  Obtendo dois usuários para teste:\n")

usr1 = obj_usuario.obtem_objeto("U-00000001")
usr2 = obj_usuario.obtem_objeto("U-00000002")
ses1 = obj_sessao.busca_por_dono(usr1, False)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_sessao.cria}:\n")
scook1 = "ABCDEFGHIJK"
data1 = None
s1 = obj_sessao.cria(usr1, scook1, data1)
sindice1 = 1
sident1 = "S-00000001"
verifica_sessao("s1", s1, sident1, usr1, True, scook1, data1)

scook2 = "BCDEFGHIJKL"
data2 = "2024-03-01 10:10:10 UTC"
s2 = obj_sessao.cria(usr2, scook2, data2)
sindice2 = 2
sident2 = "S-00000002"
verifica_sessao("s2", s2, sident2, usr2, True, scook2, data2)

scook3 = "CDEFGHIJKLM"
data3 = None
s3 = obj_sessao.cria(usr1, scook3, data3)
sindice3 = 3
sident3 = "S-00000003"
verifica_sessao("s3", s3, sident3, usr1, True, scook3, data3)

obj_sessao.fecha(s1)
verifica_sessao("fecha s1", s1, sident1, usr1, False, scook1, data1)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
