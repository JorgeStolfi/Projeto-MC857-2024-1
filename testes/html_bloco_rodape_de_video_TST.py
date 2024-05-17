#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import db_base_sql
import db_tabelas_do_sistema
import html_bloco_rodape_de_video
import obj_video
import obj_sessao
import obj_usuario
import obj_video
import util_identificador
import util_testes

import sys

from obj_usuario import obtem_atributos, obtem_identificador

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
  modulo = html_bloco_rodape_de_video
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Vídeo existente:
vid1_id = "V-00000009"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None
vid1_atrs = obj_video.obtem_atributos(vid1)

largura = 600
for mostra_nota in False, True:
  xmnta = f"_mvid{str(mostra_nota)[0]}"
  for mostra_dims in False, True:
    xmdim = f"_mpai{str(mostra_dims)[0]}"
    tag = xmnta + xmdim
    testa_gera \
      ( "C1" + tag, str, 
        vid1_id, vid1_atrs, largura, mostra_nota, mostra_dims
      )

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
