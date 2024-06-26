import sys

import db_base_sql
import html_bloco_lista_de_comentarios
import obj_comentario
import db_tabelas_do_sistema
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_bloco_lista_de_comentarios   
  funcao = html_bloco_lista_de_comentarios.gera
  frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
 
com_ids = [
  "C-00000001",
  "C-00000002",
  "C-00000003",
  "C-00000004",
  "C-00000005",
  "C-00000006",
  "C-00000007",
  "C-00000008",
  "C-00000009",
]

for para_admin in False, True:
  xadm = f"_adm{str(para_admin)[0]}"
  for ms_autor in False, True:
    xaut = f"_aut{str(ms_autor)[0]}"
    for ms_video in False, True:
      xvid = f"_vid{str(ms_video)[0]}"
      for ms_pai in False, True:
        xpai = f"_pai{str(ms_pai)[0]}"
        for ms_nota in False, True:
          xnota = f"_nota{str(ms_nota)[0]}"
            xargs = xadm + xaut + xvid + xpai + xnota
            testa_gera("muitas" + xargs, str, com_ids, para_admin, ms_autor, ms_video, ms_pai, ms_nota)
            testa_gera("lhufas" + xargs, str, [],      para_admin, ms_autor, ms_video, ms_pai, ms_nota)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.")
