#! /usr/bin/python3

import html_bloco_sessao
import db_base_sql
import util_testes
import db_tabelas
import obj_sessao
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

#sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")

def testa_html_bloco_sessao(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_sessao
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_html_bloco_sessao("Sessao", ses)

sys.stderr.write("Testes terminados normalmente.\n")

