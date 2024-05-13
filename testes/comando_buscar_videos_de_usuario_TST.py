#! /usr/bin/python3

import sys
import comando_buscar_videos_de_usuario
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
    """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_buscar_videos_de_usuario
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
 
ses1_id = "S-00000001"
ses1 = obj_sessao.obtem_objeto(ses1_id)

# Sessão de usuário comum:
testa_processa("teste1",  str, ses1, {'usuario': 'U-00000001'})  

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
 
