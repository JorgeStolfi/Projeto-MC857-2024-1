#! /usr/bin/python3

import html_pag_buscar_sessoes
import db_tabelas_do_sistema
import obj_sessao
import obj_usuario
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_buscar_sessoes
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Esta página só é usada por administradores, logo:

# Sessao de administrador:
ses_A = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses_A)

atrs_todos = \
  { 'sessao': "S-00000001", 
    'usuario': "U-00000001", 
    'aberta': True, 
    'data': "2004",
  }
  
atrs_alguns = \
  { 'aberta': False, 
    'data': None,
  }
  
atrs_ruins = \
  { 'aberta': False, 
    'cadeiras': 33,
  } 

atrs_dic = { 'N': {}, 'T': atrs_todos, 'A': atrs_alguns, 'R': atrs_ruins }

erros_1 = "Tente novamente"
erros_2 = [ "Não gostei", "Tente novamente" ]

erros_dic = { 'N': None, 'S': erros_1, 'L': erros_2, }

for at, atrs in atrs_dic.items():
  for et, erros in erros_dic.items():
    rot_teste = f"atrs{at}-erros{et}"
    testa_gera(rot_teste, ses_A, atrs, erros)

sys.stderr.write("Testes terminados normalmente.\n")
