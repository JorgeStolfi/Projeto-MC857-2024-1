#! /usr/bin/python3

# Interfaces usadas por este script:

import html_linha_resumo_de_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_html_linha_resumo_de_comentario(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_linha_resumo_de_comentario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

usr1_ident = "C-00000001"
usr1 = obj_comentario.busca_por_identificador(usr1_ident)

usr2_ident = "C-00000002"
usr2 = obj_comentario.busca_por_identificador(usr2_ident)

usr5_ident = "C-00000005"
usr5 = obj_comentario.busca_por_identificador(usr5_ident)

testa_html_linha_resumo_de_comentario("TCOMENT1",  usr1)
testa_html_linha_resumo_de_comentario("TCOMENT2",  usr2)
testa_html_linha_resumo_de_comentario("TCOMENT5",  usr5)

sys.stderr.write("Testes terminados normalmente.\n")
