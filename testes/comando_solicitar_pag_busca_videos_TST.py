import comando_solicitar_pag_buscar_videos
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import db_base_sql
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
  modulo = comando_solicitar_pag_buscar_videos
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessões de teste
ses_comum = obj_sessao.obtem_objeto("S-00000001")

# Obtém um usuário administrador
admin = obj_video.obtem_objeto("U-00000001")
assert obj_video.obtem_atributo(admin, 'administrador')
ses_admin = obj_sessao.cria(admin, "NOPQRSTUVWX")

testa_processa("NL-e0",  str, None, None)
testa_processa("NA-e2",  str, ses_comum, ["banana", "abacate"])
testa_processa("OK-e0",  str, ses_admin, None)
testa_processa("OK-e2",  str, ses_admin, ["Roubar", "Mentir"])

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  aviso_erro("Alguns testes falharam")
