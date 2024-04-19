#! /usr/bin/python3

import db_tabelas_do_sistema
import db_base_sql
import obj_sessao
import obj_usuario
import html_bloco_tabela_de_campos
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_html_bloco_tabela_de_campos(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_bloco_tabela_de_campos
  funcao = modulo.gera
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

dados_linhas = \
  [ ("Nome",          "text",     "itNome",        True,  "",                    ),
    ("Idade",         "number",   "itIdade",       True,  "XX",                  ),
    ("Telefone",      "tel",      "itTel",         False, "+XX (XX) XXXXX-XXXX", ),
    ("Email",         "email",    "itEmail",       False, "email@domain.com",    ),
    ("Carro",         "text",     "itCarro",       True,  "Marca-ano",           ),
    ("Administrador", "checkbox", "checkboxAdmin", True,  "",                    ),
    ("Patrocinador",  "text",     "itPatro",       False, "U-NNNNNNNN",          ),
  ]
  
usr3_id = "U-00000003"
usr3 = obj_usuario.busca_por_identificador(usr3_id)
assert usr3 != None

atrs = \
  { 'itNome': "João Pedro II",
    'itIdade': 22,
    'itTel': "+55(19)12345-6789",
    'itEmail': "joaopedroii@email.com",
    'itCarro': "Cybertruck-2019",
    'checkboxAdmin': True,
    'itPatro': usr3
  }

testa_html_bloco_tabela_de_campos("teste", dados_linhas, atrs)

sys.stderr.write("Testes terminados normalmente.\n")
 
