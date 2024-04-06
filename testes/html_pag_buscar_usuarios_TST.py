#! /usr/bin/python3

import html_pag_buscar_usuarios
import db_tabelas
import obj_sessao
import obj_usuario
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste:
usr1 = obj_sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = obj_usuario.obtem_identificador(usr1)
usr1_atrs = obj_usuario.obtem_atributos(usr1)

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_buscar_usuarios
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for admin in (False, True):
  ad = "-a" + str(admin)
  testa_gera("N-e0" + ad, ses, {},                                           admin, None) # Sem defaults
  testa_gera("D-e0" + ad, ses, { 'id_usuario': "UAD8291-20", 'nome': "Primeiro", 'email': "fulano@gmail.com" }, admin, None) # Com defaults
  testa_gera("D-e1" + ad, ses, { 'id_usuario': "UAD8291-20", 'nome': "Primeiro", 'email': "fulano@gmail.com" }, admin, "Tente novamente") # Com defaults e erro
  testa_gera("D-e2" + ad, ses, { 'id_usuario': "UAD8291-20", 'nome': "Primeiro", 'email': "fulano@gmail.com", 'documento': "Lenço" }, admin, "Tente novamente") # Com defaults e erro
