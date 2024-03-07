#! /usr/bin/python3

import html_pag_cadastrar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste cujo usuario não é admin:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

# Atributos de usuario para teste:
atrs1 = {
  'nome': "José Primeiro", 
  'senha': "123456789", 
  'email': "primeiro@gmail.com",
  'administrador': False
}

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_cadastrar_usuario
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for tag, atrs, erros in ( 
    ("NN", None,  None), 
    ("NA", atrs1, None), 
    ("VN", None,  []), 
    ("VA", atrs1, []), 
    ("EN", None,  ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
    ("EA", atrs1, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
  ):
  rotulo = tag
  testa(rotulo, ses, atrs, erros)

# Sessao de teste cujo usuario é admin:
ses = obj_sessao.busca_por_identificador("S-00000004")
assert ses != None

for tag, atrs, erros in ( 
    ("NN", None,  None), 
    ("NA", atrs1, None), 
    ("VN", None,  []), 
    ("VA", atrs1, []), 
    ("EN", None,  ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
    ("EA", atrs1, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
  ):
  rotulo = tag
  testa(rotulo, ses, atrs, erros)
