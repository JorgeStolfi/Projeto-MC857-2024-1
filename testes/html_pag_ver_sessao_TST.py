#! /usr/bin/python3

import html_pag_ver_sessao
import db_base_sql
import util_testes
import db_tabelas_do_sistema
import obj_sessao
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
  modulo = html_pag_ver_sessao
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de um administrador:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)
sesA_dono = obj_sessao.obtem_dono(sesA)

# Sessao de usuário comum:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)
sesC_dono = obj_sessao.obtem_dono(sesC)

# Sessao a ver, de usuário diferente dos dois:
sesT_id = "S-00000005"
sesT = obj_sessao.obtem_objeto(sesT_id)
assert sesT != None
sesT_dono = obj_sessao.obtem_dono(sesT)
assert sesT_dono != sesA_dono and sesT_dono != sesC_dono

for ses_login_tag, ses_login in ( "A", sesA, ), ( "C", sesC, ):
  xlog = f"_seslog{ses_login_tag}"
  for ses_a_ver_tag, ses_a_ver in ( ses_login_tag, ses_login, ), ("T", sesT, ):
    xver = f"_sesver{ses_a_ver_tag}"
    for erros_tag, erros in ( "E0", None, ), ( "E2", ["Veja a mensagem abaixo", "Veja a mensagem acima"], ):
      xerr = f"_erros{erros_tag}"
      rot_teste = "S" + xlog + xver + xerr
      testa_gera(rot_teste,  str, ses_login, ses_a_ver, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
