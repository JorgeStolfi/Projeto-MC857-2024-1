#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
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
  modulo = html_linha_resumo_de_comentario
  funcao = html_linha_resumo_de_comentario.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# sessão de admin
ses1 = obj_sessao.obtem_objeto("S-00000001")

# Um comentário sem pai:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert obj_comentario.obtem_atributo(com1, 'pai') == None

# Um comentário com pai:
com2_id = "C-00000005"
com2 = obj_comentario.obtem_objeto(com2_id)
assert obj_comentario.obtem_atributo(com2, 'pai') != None

for ms_autor in False, True:
  xaut = f"_msaut{str(ms_autor)[0]}"
  for ms_video in False, True:
    xvid = f"_msvid{str(ms_video)[0]}"
    for ms_pai in False, True:
      xpai = f"_mspai{str(ms_pai)[0]}"
      for ms_nota in False, True:
        xnota = f"_mspai{str(ms_nota)[0]}"
        tag = xaut + xvid + xpai + xnota
        testa_gera("C1" + tag,  list, ses1, com1, ms_autor, ms_video, ms_pai, ms_nota)
        testa_gera("C2" + tag,  list, ses1, com2, ms_autor, ms_video, ms_pai, ms_nota)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
