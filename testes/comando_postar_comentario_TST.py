#! /usr/bin/python3

import comando_postar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video
import util_testes
from util_erros import erro_prog, aviso_prog, mostra

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.

def testa_processa(rot_teste, ses, cmd_args, res_esp, deveria_postar):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  
  sys.stderr.write("  " + ("~"*70) + "\n")

  ult_id_old = obj_comentario.ultimo_identificador()
  sys.stderr.write(f"  ultimo comentário antes = {ult_id_old}\n")

  frag = False
  pretty = False
  modulo = comando_postar_comentario
  funcao = comando_postar_comentario.processa
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, ses, cmd_args)
  ok_global = ok_global and ok

  ult_id_new = obj_comentario.ultimo_identificador()
  sys.stderr.write(f"  ultimo comentário depois = {ult_id_new}\n")
  
  if ult_id_new != ult_id_old:
    com_new_obj = obj_comentario.obtem_objeto(ult_id_new)
    com_new_atrs = obj_comentario.obtem_atributos(com_new_obj) if com_new_obj != None else None
    sys.stderr.write(f"  comentario postado = {com_new_obj} atrs = {str(com_new_atrs)}\n")
    if deveria_postar:
      sys.stderr.write("  CONFERE!\n")
    else:
      sys.stderr.write("  ** Postou comentario quando não deveria postar\n")
      ok_global = False
  else:
    sys.stderr.write(f"  comentario não postado\n")
    if deveria_postar:
      sys.stderr.write("  ** Não postou comentario quando deveria postar\n")
      ok_global = False
    else:
      sys.stderr.write("  CONFERE!\n")
    
  sys.stderr.write("  " + ("~"*70) + "\n\n")

# ----------------------------------------------------------------------
# Sessão para teste:
ses1_id = "S-00000001"
ses1 = obj_sessao.obtem_objeto(ses1_id)
assert ses1 != None
ses1_dono = obj_sessao.obtem_dono(ses1)
assert ses1_dono != None

# ----------------------------------------------------------------------
# Testa chamada OK sem pai:
dados1 = { 'video': "V-00000001", 'pai': None, 'texto': "Repúdio ao pódio espúrio!", }
testa_processa("GUD-SemPai", ses1, dados1, str, True)

# Testa chamada OK com pai:
dados2 = { 'video': "V-00000003", 'pai': "C-00000004", 'texto': "Concordo discordando.", }
testa_processa("GUD-ComPai", ses1, dados2, str, True)

# Testa chamada com pai inválido:
dados3 = { 'video': "V-00000003", 'pai': "C-00001007", 'texto': "Discordo concordando.", }
testa_processa("BAD-MauPai", ses1, dados3, str, False)

# Testa chamada com pai mas sem texto:
dados4 = { 'video': "V-00000003", 'pai': "C-00000004", }
testa_processa("BAD-SemTexto", ses1, dados4, str, False)

# Testa chamada com argumentos espúrios:
dados5 = { 'video': "V-00000003", 'pai': "C-00000004", 'texto': "Celeuma cerúlea?", 'neto': "C-00000007", }
testa_processa("BAD-Lixo", ses1, dados5, "AssertionError", False)

# Testa chamada com pai de outro vídeo:
dados6 = { 'video': "V-00000003", 'pai': "C-00000003", 'texto': "Fenômeno fenomenal!", }
testa_processa("BAD-OutroVid", ses1, dados6, str, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
