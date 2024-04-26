#! /usr/bin/python3

import html_pag_cadastrar_usuario
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
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
  modulo = html_pag_cadastrar_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de teste cujo usuario não é admin:
ses = obj_sessao.busca_por_identificador("S-00000004")
assert ses != None

# Atributos de usuario para teste:
atrs1 = {
  'nome': "José Primeiro", 
  'senha': "123456789", 
  'email': "primeiro@gmail.com",
  'administrador': False
}

for tag, atrs, erros in ( 
    ("NN", None,  None), 
    ("NA", atrs1, None), 
    ("VN", None,  []), 
    ("VA", atrs1, []), 
    ("EN", None,  ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
    ("EA", atrs1, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
  ):
  rot_teste = tag
  testa_gera(rot_teste,  str, ses, atrs, erros)

# Sessao de teste cujo usuario é admin:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

for tag, atrs, erros in ( 
    ("NN", None,  None), 
    ("NA", atrs1, None), 
    ("VN", None,  []), 
    ("VA", atrs1, []), 
    ("EN", None,  ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
    ("EA", atrs1, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
  ):
  rot_teste = tag
  testa_gera(rot_teste,  str, ses, atrs, erros)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
