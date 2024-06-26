#! /usr/bin/python3

import html_pag_buscar_videos
import db_tabelas_do_sistema
import obj_sessao
import obj_usuario
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_pag_buscar_videos
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de administrador:
ses_A = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses_A)

# Sessao de usuário comum:
ses_C = obj_sessao.obtem_objeto("S-00000003")
assert not obj_sessao.de_administrador(ses_C)

ses_dic = { 'N': None, 'A': ses_A, 'C': ses_C, }

atrs_aut = { 'autor': "U-00000001", }
atrs_tit = { 'titulo': "fuk", }
atrs_bad = { 'neto': "N-00000001", }

atrs_dic = { 'N': {}, 'A': atrs_aut, 'T': atrs_tit, 'B': atrs_bad, }

erros_1 = "Tente novamente"
erros_2 = [ "Não gostei", "Tente novamente" ]

erros_dic = { 'N': None, 'S': erros_1, 'L': erros_2, }

for st, ses in ses_dic.items():
  for at, atrs in atrs_dic.items():
    for et, erros in erros_dic.items():
      rot_teste = f"ses{st}-atrs{at}-erros{et}"
      testa_gera(rot_teste,  str, ses, atrs, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
