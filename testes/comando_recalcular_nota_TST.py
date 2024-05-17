#! /usr/bin/python3

import comando_recalcular_nota
import db_tabelas_do_sistema
import obj_comentario
import obj_usuario
import obj_sessao
import obj_video
import db_base_sql
import util_dict
import util_testes
from util_erros import ErroAtrib, aviso_prog

import re
import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, ses, com, vid, valido, nota_esp):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, e grava esse resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  
  # Executa o comando:
  modulo = comando_recalcular_nota
  funcao = comando_recalcular_nota.processa
  if com != None:
    cmd_args = { 'comentario': obj_comentario.obtem_identificador(com) }
    if not valido: nota_esp = obj_comentario.obtem_atributo(com, 'nota')
  elif vid != None:
    cmd_args = { 'video': obj_video.obtem_identificador(vid) }
    if not valido: nota_esp = obj_video.obtem_atributo(vid, 'nota')
  else:
    assert False, "Hã?"
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, str, frag, pretty, ses, cmd_args)

  # Confere nota:
  if com != None:
    nota_nova = obj_comentario.obtem_atributo(com, 'nota')
  elif vid != None:
    nota_nova = obj_video.obtem_atributo(vid, 'nota')
  else:
    assert False, "Pô?"
  if nota_nova != nota_esp:
    sys.stderr.write(f"  ** Nota recalculada = {nota_nova} não é a esperada = {nota_esp}\n")
    ok = False
  else:
    sys.stderr.write("  CONFERE!\n")

  ok_global = ok_global and ok
  return ok

# Uma sessão de administrador:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)

# Uma sessão de usuário comum:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)

# Comentário de teste:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None

# Vídeo de teste:
vid1_id = "V-00000001"
vid1 = obj_video.obtem_objeto(vid1_id)
assert vid1 != None

sys.stderr.write("\n")

for ses_tag, ses in ("N", None), ("A", sesA), ("C", sesC):
  xses = f"_ses{ses_tag}"
  valido = (ses == sesA)
  # !!! Calcular a nota esperada na mão e corrigir abaixo: !!!
  testa_processa("C1" + xses, ses, com1, None, valido, 99.0 )
  testa_processa("V1" + xses, ses, None, vid1, valido, 99.0 )

if ok_global:
  sys.stderr.write("Teste terminado normalmente\n")
else:
  aviso_prog("Alguns testes falharam.", True)
