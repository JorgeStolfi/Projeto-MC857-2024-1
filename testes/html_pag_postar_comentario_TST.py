#! /usr/bin/python3

import html_pag_postar_comentario
import db_tabelas_do_sistema
import obj_sessao
import db_base_sql
import util_testes
from util_erros import aviso_prog

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
  modulo = html_pag_postar_comentario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

dados = { \
  'autor': "U-00000001",
  'video': 'V-00000001',
  'texto': 'Texto Teste',
}

# Testa inserir dados no form de comentarios sem um comentarios pai
ses = obj_sessao.obtem_objeto("S-00000001")
testa_gera("T1-success", str, ses, dados, None)

dados = { \
  'autor': "U-00000001",
  'video': 'V-00000001',
  'pai': 'C-00000001',
  'texto': 'Texto Teste',
}

# Testa inserir dados no form de comentarios com um comentarios pai
ses = obj_sessao.obtem_objeto("S-00000001")
testa_gera("T2-success", str, ses, dados, None)

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  aviso_erro("Alguns testes falharam")
