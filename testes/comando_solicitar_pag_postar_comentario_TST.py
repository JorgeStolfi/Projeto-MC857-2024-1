#! /usr/bin/python3

import comando_solicitar_pag_postar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_sessao
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = comando_solicitar_pag_postar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
 
# Uma sessão de admnistrador:
ses_A1_id = "S-00000001"
ses_A1 = obj_sessao.busca_por_identificador(ses_A1_id)
assert ses_A1 != None
assert obj_sessao.de_administrador(ses_A1)

# Uma sessão de usuário comum:
ses_C1_id = "S-00000003"
ses_C1 = obj_sessao.busca_por_identificador(ses_C1_id)
assert ses_C1 != None
assert not obj_sessao.de_administrador(ses_C1)

cmd_args = {
  "video": "V-00000001",
  "pai": "C-00000001",
  "autor": "U-00000001"
}

testa_processa("T1",  str, ses_A1, *args)

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  aviso_erro("Alguns testes falharam")
