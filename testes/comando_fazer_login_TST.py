#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_fazer_login

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.

def testa_processa(rot_teste, email, senha, deveria_logar):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  cmd_args = {
    "email": email,
    "senha": senha
  }
  res_esp = (str, obj_sessao.Classe) if deveria_logar else (str, None)
  modulo = comando_fazer_login
  funcao = modulo.processa
  html = False 
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, None, cmd_args)
  ok_global = ok_global and ok
  return ok
     
# ----------------------------------------------------------------------
# Executa chamadas
testa_processa("OK",   "primeiro@gmail.com",  "U-00000001", True)
testa_processa("Erro", "nao_existo@gmail.com", "123456789", False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
