#! /usr/bin/python3

import html_pag_ver_usuario
import db_base_sql
import util_testes
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Sessao do admin
ses1 = obj_sessao.busca_por_identificador("S-00000001")

# Comentário de teste:
com1 = obj_video.busca_por_identificador("C-00000002")

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  modulo = html_pag_ver_usuario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

testa_gera("C-E0", ses1, com1, None)
testa_gera("C-E2", ses1, com1, ["Veja a mensagem abaixo", "Veja a mensagem acima"])

sys.stderr.write("Testes terminados normalmente")
