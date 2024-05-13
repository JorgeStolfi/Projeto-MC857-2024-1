#! /usr/bin/python3

import html_pag_ver_conversa
import html_bloco_titulo
import util_testes
import obj_sessao
import obj_comentario
import obj_video
from util_erros import erro_prog, aviso_prog

import db_base_sql
import db_tabelas_do_sistema

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_pag_ver_conversa
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao do admin
ses1 = obj_sessao.obtem_objeto("S-00000001")

# Comentários de teste:
com1_id = "C-00000002"
com1 = obj_comentario.obtem_objeto(com1_id)

com2_id = "C-00000002"
com2 = obj_comentario.obtem_objeto(com2_id)

titulo = html_bloco_titulo.gera("Fofocas")
erros = [ "Cuidado com a cobra", "O silêncio é de ouro", ]
raizes = [ com1_id, com2_id, ]
max_coms = 10
max_nivel = 3
conversa = obj_comentario.obtem_conversa(raizes, max_coms, max_nivel)

testa_gera("C1", str, ses1, titulo, conversa, erros)

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  aviso_prog("Alguns testes falharam", True)
