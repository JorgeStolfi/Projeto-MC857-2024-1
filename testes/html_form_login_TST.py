#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_login
import obj_usuario
import db_base_sql
import db_tabelas_do_sistema
import util_testes
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Testes das funções de {html_elem_form}:

def testa_gera(rot_teste):
  """Testa {funcao()}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_form_login
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty)

usr1 = obj_usuario.busca_por_identificador("U-00000001")
assert usr1 != None

testa_gera("N")

sys.stderr.write("Testes terminados normalmente.\n")
