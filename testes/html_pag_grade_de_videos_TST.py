#! /usr/bin/python3

import html_pag_grade_de_videos
import db_base_sql
import util_testes
import db_tabelas_do_sistema
import obj_sessao
import obj_video

import sys
import random

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
  modulo = html_pag_grade_de_videos
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao do admin
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)

# Sessão de usuário comum:
sesC_id = "S-00000004"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)

# Índice do último vídeo carregado:
vidL_id = obj_video.ultimo_identificador()
vidL_index = int(vidL_id[2:])
sys.stderr.write(f"  last video in system = {vidL_id}\n")

# Número de vídeos a escolher:
ngrid = min(12, vidL_index)

# Lista de vídeos aleatórios:
vidR_indices = random.sample(range(1,vidL_index+1), ngrid)
vidR_ids = list(map(lambda index: f"V-{index:08d}", vidR_indices))
assert len(vidR_ids) == ngrid
sys.stderr.write(f"  video ids = {vidR_ids}\n")

for ses_tag, ses in ("N", None), ("A", sesA), ("C", sesC):
  xses = f"_ses{ses_tag}"
  for ncols in 4, 6:
    xncols = f"_ncols{ncols:02d}"
    for erros_tag, erros in ( "E0", None, ), ( "E2", [ "Veja a mensagem abaixo", "Veja a mensagem acima" ], ):
      xerr = f"_erros{erros_tag}"
      tag = xses + xncols + xerr
      testa_gera("G1" + tag, str, ses, vidR_ids, ncols, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.")
