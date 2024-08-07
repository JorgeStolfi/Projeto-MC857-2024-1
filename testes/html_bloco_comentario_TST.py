#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import db_base_sql
import db_tabelas_do_sistema
import html_bloco_comentario
import obj_comentario
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
  modulo = html_bloco_comentario
  funcao = html_bloco_comentario.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Comentário existente não bloqueado:
com9_id = "C-00000009"
com9 = obj_comentario.obtem_objeto(com9_id)
assert com9 != None

# Comentário existente bloqueado:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None

largura = 700
for mostra_id in False, True:
  xmide = f"_mid{str(mostra_id)[0]}"
  for mostra_data in False, True:
    xmdat = f"_mvid{str(mostra_data)[0]}"
    for mostra_video in False, True:
      xmvid = f"_mvid{str(mostra_video)[0]}"
      for mostra_pai in False, True:
        xmpai = f"_mpai{str(mostra_pai)[0]}"
        for mostra_bloqueado in False, True:
          xm_bloqueado = f"_mbloqueado{str(mostra_bloqueado)[0]}"
          for botoes in False, True:
            xbots = f"_bots{str(botoes)[0]}"
            for calcnota in False, True:
              xcalc = f"_calc{str(calcnota)[0]}"
              for bloq in False, True:
                xbloq = f"_bloq_desbloq{str(bloq)[0]}"
                tag = xmide + xmdat + xmvid + xmpai + xm_bloqueado + xbots + xcalc + xbloq
                bt_conversa = botoes
                bt_responder = botoes
                bt_editar = botoes
                bt_calcnota = calcnota
                bt_bloq_desbloq = bloq
                testa_gera(
                  "C9" + tag, str, 
                  com9, largura, mostra_id, mostra_data, mostra_video, mostra_pai, mostra_bloqueado,
                  bt_conversa, bt_responder, bt_editar, bt_calcnota, bt_bloq_desbloq
                )
                testa_gera(
                  "C1" + tag, str, 
                  com1, largura, mostra_id, mostra_data, mostra_video, mostra_pai, mostra_bloqueado,
                  bt_conversa, bt_responder, bt_editar, bt_calcnota, bt_bloq_desbloq
                )

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
