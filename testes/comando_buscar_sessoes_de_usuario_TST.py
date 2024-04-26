#! /usr/bin/python3
import sys
import comando_buscar_sessoes_de_usuario
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_buscar_sessoes_de_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão de usuário comum:
ses1 = obj_sessao.busca_por_identificador("S-00000004")
assert not obj_sessao.de_administrador(ses1)
usr1 = obj_sessao.obtem_usuario(ses1)
usr1_id = obj_usuario.obtem_identificador(usr1)
testa_processa("teste1-N",  str, ses1, {} )
testa_processa("teste1-U",  str, ses1, {'usuario': usr1_id } )

# Administrador olhando suas sessões:
ses2 = obj_sessao.busca_por_identificador("S-00000002")
assert obj_sessao.de_administrador(ses2)
usr2_id = "U-00000002"
testa_processa("teste2-N",  str, ses2, {} )
testa_processa("teste2-U",  str, ses2, {'usuario': usr2_id } )

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
