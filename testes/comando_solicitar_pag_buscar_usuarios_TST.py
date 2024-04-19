#! /usr/bin/python3

import comando_solicitar_pag_buscar_usuarios
import db_tabelas_do_sistema
import obj_sessao
import obj_usuario
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_processa(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = comando_solicitar_pag_buscar_usuarios
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessão de administrador:
ses_A1 = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses_A1)

# Sessão de usuário comum, aberta:
ses_C1 = obj_sessao.busca_por_identificador("S-00000003")
assert not obj_sessao.de_administrador(ses_C1)

# Sessão de usuário comum, não aberta:
ses_C2 = obj_sessao.busca_por_identificador("S-00000004")
assert not obj_sessao.de_administrador(ses_C2)
obj_sessao.fecha(ses_C2)

testa_processa("NA-e2", None,   {}) # Não logado.
testa_processa('CA-e3', ses_C1, {}) # Sessao usuário comum aberta.
testa_processa("OK-e0", ses_A1, {}) # Sessão admin aberta.

try:
  testa_processa("NL-e0", ses_C2, {}) # Sessão comum não aberta.
except AssertionError as error:
  print('Retornou o seguinte erro, pois a sessão já tinha sido fechada: {}'.format(error))

try:
  testa_processa('CA-e3', ses_C1, {"bla, bla, bla"}) # Sessao usuário comum aberta, argumentos não são do tipo dicionário.
except AssertionError as error:
  print('Retornou o seguinte erro, pois os argumentos passados não eram válidos: {}'.format(error))

try:
  testa_processa('CA-e3', ses_C1, {"error": True}) # Sessao usuário comum aberta, argumentos não vazio.
except AssertionError as error:
  print('Retornou o seguinte erro, pois os argumentos passados não eram vazios: {}'.format(error))

sys.stderr.write("Testes terminados normalmente.\n")
