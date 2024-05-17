import comando_solicitar_pag_buscar_videos
import db_tabelas_do_sistema
import obj_sessao
import obj_video
import db_base_sql
import util_testes
import obj_usuario
import sys
from util_erros import ErroAtrib, aviso_prog, erro_prog

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_solicitar_pag_buscar_videos
  funcao = modulo.processa
  frag = False  
  pretty = True 
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessão para teste:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)

testa_processa("sesN",  str, None, {})
testa_processa("sesA",  str, sesA, {})

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  #aviso_prog("Alguns testes falharam.")
  aviso_prog("Alguns testes falharam.", True)
