#! /usr/bin/python3

import html_form_criar_alterar_comentario
import obj_comentario
import obj_sessao
import util_identificador
import db_base_sql
import db_tabelas_do_sistema
import util_testes

import sys

from obj_comentario import obtem_atributos, obtem_identificador

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_form_criar_alterar_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Comentario:
comC1_id = "C-00000004"
comC1 = obj_comentario.busca_por_identificador(comC1_id)
assert comC1 != None

for ses_admin in False, True:
  st = str(ses_admin)[0]
  atrs_tot = obj_comentario.obtem_atributos(comC1)
  atrs_som = { 'texto': "Alteradus", }
  atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
  for at, atrs in atrs_dic.items():
    rot_teste = f"admin{st}-atrs{at}"
    testa_gera(rot_teste, comC1_id, atrs, ses_admin)

sys.stderr.write("Testes terminados normalmente.\n")