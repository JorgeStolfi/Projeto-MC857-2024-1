#! /usr/bin/python3

import os,sys,inspect
import db_base_sql 
import db_tabela_generica
import db_tabelas
import obj_sessao
import obj_usuario
import util_testes
from util_testes import erro_prog, mostra, aviso_prog

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
obj_usuario.cria_testes(True)

sys.stderr.write("Inicializando módulo {sessao}, limpando tabela:\n")
obj_sessao.inicializa_modulo(True)

# ----------------------------------------------------------------------
sys.stderr.write("Obtendo dois usuários para teste:\n")

usr1 = obj_usuario.busca_por_identificador("U-00000001")
usr2 = obj_usuario.busca_por_identificador("U-00000002")

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_sessao(rotulo, ses, ident, usr, abrt, cookie):
  """Testes básicos de consistência do objeto {ses} da classe {obj_sessao.Classe}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando sessão %s\n" % rotulo)
  atrs = { 'usr': usr, 'abrt': abrt, 'cookie': cookie }
  ok = obj_sessao.verifica(ses, ident, atrs)
  
  if ses != None and type(ses) is obj_sessao.Classe:
    
    sys.stderr.write("testando {obtem_usuario()}:\n")
    usr1 = obj_sessao.obtem_usuario(ses)
    if usr1 != usr:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(usr),True)
      ok = False
      
    sys.stderr.write("testando {aberta()}:\n")
    abrt1 = obj_sessao.aberta(ses)
    if abrt1 != abrt:
      aviso_prog("retornou " + str(abrt1) + ", deveria ter retornado " + str(abrt),True)
      ok = False
       
    sys.stderr.write("testando {obtem_cookie()}:\n")
    cookie1 = obj_sessao.obtem_cookie(ses)
    if cookie1 != cookie:
      aviso_prog("retornou " + str(cookie1) + ", deveria ter retornado " + str(cookie),True)
      ok = False
 
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {obj_sessao.cria}:\n")
scook1 = "ABCDEFGHIJK"
s1 = obj_sessao.cria(usr1, scook1)
sindice1 = 1
sident1 = "S-00000001"
verifica_sessao("s1", s1, sident1, usr1, True, scook1)

scook2 = "BCDEFGHIJKL"
s2 = obj_sessao.cria(usr2, scook2)
sindice2 = 2
sident2 = "S-00000002"
verifica_sessao("s2", s2, sident2, usr2, True, scook2)

scook3 = "CDEFGHIJKLM"
s3 = obj_sessao.cria(usr1, scook3)
sindice3 = 3
sident3 = "S-00000003"
verifica_sessao("s3", s3, sident3, usr1, True, scook3)

obj_sessao.fecha(s1)
verifica_sessao("fecha s1", s1, sident1, usr1, False, scook1)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
