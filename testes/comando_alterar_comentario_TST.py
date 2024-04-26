#! /usr/bin/python3

import comando_alterar_comentario
import db_tabelas_do_sistema
import obj_comentario
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes
from util_erros import ErroAtrib

import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_alterar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses)

# Executar o teste
cmd_args = {
  #"C-00000001", "V-00000001", "U-00000001", "2024-04-05 08:00:00 UTC", None,         "Supimpa!\nDeveras!"
  'comentario': "C-00000001", 'autor' : "U-00000001", 'video' : "V-00000001", 'texto' : "Texto de teste" 
}
testa_processa("Dup", str, ses, *args)

# !!! Deveria ter mais testes !!!

if ok_global:
  sys.stderr.write("Teste terminado normalmente\n")
else:
  aviso_erro("Alguns testes falharam", True)
