#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

from util_erros import aviso_prog
import db_base_sql
import db_tabelas_do_sistema
import html_bloco_cabecalho_de_comentario
import obj_comentario
import obj_video
from util_erros import aviso_prog
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
  modulo = html_bloco_cabecalho_de_comentario
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Comentário existente:
com1_id = "C-00000009"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None
com1_atrs = obj_comentario.obtem_atributos(com1)

largura = 600
for mostra_id in False, True:
  xmide = f"_mide{str(mostra_id)[0]}"
  for mostra_data in False, True:
    xmdat = f"_mdat{str(mostra_data)[0]}"
    for mostra_video in False, True:
      xmvid = f"_mvid{str(mostra_video)[0]}"
      for mostra_pai in False, True:
        xmpai = f"_mpai{str(mostra_pai)[0]}"
        tag = xmide + xmdat + xmvid + xmpai
        testa_gera \
          ( "C1" + tag, str, 
            com1_id, com1_atrs, largura, mostra_id, mostra_data, mostra_video, mostra_pai
          )
          
# Valida a truncagem dos título e do comentário

## Validação do título
### Comentário sem pai e título do vídeo pequeno (menos de 40 caracteres, não precisa ser truncado)
com2_id = "C-00000008"
com2 = obj_comentario.obtem_objeto(com2_id)
assert com2 != None
com2_atrs = obj_comentario.obtem_atributos(com2)
testa_gera("ComentarioSemPai_TituloPequeno", str, com2_id, com2_atrs, largura, True, True, True, True)

### Comentário sem pai e título grande (precisa ser truncado!)
video_do_comentario = com2_atrs['video']
titulo_original = obj_video.obtem_atributo(video_do_comentario, 'titulo')
titulo_grande = "Eu sou um título de vídeo muito grande mesmo!! Me trunque!"
obj_video.muda_atributos(video_do_comentario, { 'titulo': titulo_grande })
testa_gera("ComentarioSemPai_TituloGrande", str, com2_id, com2_atrs, largura, True, True, True, True)
obj_video.muda_atributos(video_do_comentario, { 'titulo': titulo_original }) # Volta o título original para manter a consistência nos outros testes!


## Validação do texto do comentário
### Comentário com pai e texto pequeno (não precisa ser truncado)
com3_id = "C-00000009"
com3 = obj_comentario.obtem_objeto(com3_id)
assert com3 != None
com3_atrs = obj_comentario.obtem_atributos(com3)
testa_gera("ComentarioComPai_TextoPequeno", str, com3_id, com3_atrs, largura, True, True, True, True)

### Comentário com pai e texto grande (precisa ser truncado!)
comentario_pai = obj_comentario.obtem_atributo(com3, 'pai')
comentario_original = obj_comentario.obtem_atributo(comentario_pai, 'texto')
comentario_grande = "Um comentário muito grande, que passa dos limites!"
obj_comentario.muda_atributos(comentario_pai, { 'texto': comentario_grande })
testa_gera("ComentarioComPai_TextoGrande", str, com3_id, com3_atrs, largura, True, True, True, True)
obj_comentario.muda_atributos(comentario_pai, { 'texto': comentario_original }) # Volta ao comentário original para manter consistência!

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
