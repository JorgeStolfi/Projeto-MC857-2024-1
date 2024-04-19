#! /usr/bin/python3

import comando_alterar_video
import obj_video
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

# Obtem sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")
assert obj_sessao.de_administrador(ses)

def testa_comando_alterar_video(rot_teste, *args):
  """Testa {funcao(*cmd_args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = comando_alterar_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

sys.stderr.write("!!! falta o progama de teste {comando_alterar_video_TST.py} !!!\n")
