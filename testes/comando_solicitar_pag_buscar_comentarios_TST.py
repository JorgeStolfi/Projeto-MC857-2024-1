import comando_solicitar_pag_buscar_comentarios
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import db_base_sql
import util_testes
import obj_usuario
import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_processa(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = comando_solicitar_pag_buscar_comentarios
  funcao = modulo.processa
  frag = False  
  pretty = True 
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

aviso_prog("!!! programa de teste de {comando_solicitar_pag_buscar_comentarios} ainda não escrito !!!")
