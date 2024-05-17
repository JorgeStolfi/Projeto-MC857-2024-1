#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import html_pag_ver_comentario
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video
import util_testes

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
  modulo = html_pag_ver_comentario
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
sesA_dono = obj_sessao.obtem_dono(sesA)
assert obj_usuario.obtem_identificador(sesA_dono) == "U-00000001"

# Sessao de usuário comum:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)
sesC_dono = obj_sessao.obtem_dono(sesC)
assert obj_usuario.obtem_identificador(sesC_dono) == "U-00000002"

# Um comentário do administrador:
comA_id = "C-00000001"
comA = obj_comentario.obtem_objeto(comA_id)
assert comA != None
comA_autor = obj_comentario.obtem_atributo(comA, 'autor')
assert comA_autor == sesA_dono

# Um comentário do usuário {sesC_dono}:
comC_id = "C-00000002"
comC = obj_comentario.obtem_objeto(comC_id)
assert comC != None
comC_autor = obj_comentario.obtem_atributo(comC, 'autor')
assert comC_autor == sesC_dono

# Um comentário de terceira pessoa:
comT_id = "C-00000010"
comT = obj_comentario.obtem_objeto(comT_id)
assert comT != None
comT_autor = obj_comentario.obtem_atributo(comT, 'autor')
assert comT_autor != sesA_dono and comT_autor != sesC_dono

for ses_tag, ses in ( "N", None, ), ( "A", sesA, ), ( "C", sesC, ):
  xses = f"_ses{ses_tag}"
  comP = comA if ses == sesA else comC
  for com_tag, com in ( "P", comP, ), ( "T", comT ):
    xcom = f"_com{com_tag}"
    for erros_tag, erros in ( "E0", None, ), ( "E2", [ "Veja a mensagem abaixo", "Veja a mensagem acima" ], ):
      xerr = f"_erros{erros_tag}"
      rot_teste = "VC" + xses + xcom + xerr
      testa_gera(rot_teste, str, ses, com, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
