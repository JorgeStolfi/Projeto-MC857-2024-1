#! /usr/bin/python3

import comando_solicitar_pag_postar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_sessao
import util_testes

import sys

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
  modulo = comando_solicitar_pag_postar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# ----------------------------------------------------------------------
# Dados para testes:
 
# Uma sessão qualquer, aberta:
ses_C_id = "S-00000005"
ses_C = obj_sessao.obtem_objeto(ses_C_id)
assert ses_C != None
assert obj_sessao.aberta(ses_C)
assert not obj_sessao.de_administrador(ses_C)
 
# Uma sessão já fechada:
ses_F_id = "S-00000003"
ses_F = obj_sessao.obtem_objeto(ses_F_id)
assert ses_F != None
obj_sessao.fecha(ses_F)
assert not obj_sessao.aberta(ses_F)

# Argumentos com vídeo apenas:
args_V_gud = { 'video': "V-00000003", }

# Argumentos com vídeo inválido:
args_V_bad = { 'video': "V-00010003", }

# Argumentos com pai apenas:
args_P_gud = { 'pai': "C-00000006", }

# Argumentos com pai inválido:
args_P_bad = { 'pai': "C-00010006", }

# Argumentos com vídeo e pai, consistentes:
args_VP_gud = { 'video': "V-00000003", 'pai': "C-00000006", }

# Argumentos com vídeo e pai, inconsistentes:
args_VP_bad = { 'video': "V-00000003", 'pai': "C-00000003", }

# ----------------------------------------------------------------------
# Testes

# Usuário não logado:
testa_processa("BAD_sesNul",  str, None, args_V_gud )

# Sessão já fechada:
testa_processa("BAD_sesOut",  str, ses_F, args_V_gud )

# Falta vídeo e pai:
testa_processa("BAD_atrNul",  str, ses_C, { })

# Vídeo inexistente:
testa_processa("BAD_vidInv",  str, ses_C, args_V_bad )

# Pai inexistente:
testa_processa("BAD_paiInv",  str, ses_C, args_P_bad )

# Apenas vídeo especificado:
testa_processa("GUD_soVid",   str, ses_C, args_V_gud )

# Apenas pai especificado:
testa_processa("GUD_soPai",   str, ses_C, args_P_gud )

# Vídeo e pai, consistentes:
testa_processa("GUD_ambos",   str, ses_C, args_VP_gud )

# Vídeo e pai, inconsistentes:
testa_processa("BAD_ambos",   str, ses_C, args_VP_bad )

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.")
