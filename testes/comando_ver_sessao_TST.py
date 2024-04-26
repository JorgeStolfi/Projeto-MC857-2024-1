#! /usr/bin/python3

import sys
import comando_ver_sessao
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
  modulo = comando_ver_sessao
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

id_ses = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(id_ses)

# Sessão de usuário comum:
testa_processa("uso_comum",  str, ses1, {'sessao': 'S-00000001'})

# Cliente tentando acessar sessão que não e dele:
testa_processa("acesso_invalido",  str, ses1, {'sessao': 'S-00000003'})

# Chamada sem argumentos
testa_processa("sem_argumento",  str, ses1, {})

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)

