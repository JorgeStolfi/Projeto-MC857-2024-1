#! /usr/bin/python3

import comando_solicitar_pag_alterar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
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
  modulo = comando_solicitar_pag_alterar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Uma sessão de administrador, aberta:
ses_A_id = "S-00000001"
ses_A = obj_sessao.obtem_objeto(ses_A_id)
assert ses_A != None
assert obj_sessao.aberta(ses_A)
usr_A = obj_sessao.obtem_dono(ses_A)  # U-00000001.
assert obj_usuario.eh_administrador(usr_A)

# Uma sessão de usuário comum, aberta:
ses_C_id = "S-00000005"
ses_C = obj_sessao.obtem_objeto(ses_C_id)
assert ses_C != None
assert obj_sessao.aberta(ses_C)
usr_C = obj_sessao.obtem_dono(ses_C) # U-00000005.
assert not obj_usuario.eh_administrador(usr_C)
 
# Uma sessão já fechada:
ses_F_id = "S-00000003"
ses_F = obj_sessao.obtem_objeto(ses_F_id)
assert ses_F != None
obj_sessao.fecha(ses_F)
assert not obj_sessao.aberta(ses_F)

# Um comentário de {usr_C}:
com_C_id = "C-00000012"
com_C = obj_comentario.obtem_objeto(com_C_id)
assert com_C != None
com_C_autor = obj_comentario.obtem_atributo(com_C, 'autor')
assert com_C_autor == usr_C

# Um comentário de outro usuário:
com_T_id = "C-00000010"
com_T = obj_comentario.obtem_objeto(com_T_id)
assert com_T != None
com_T_autor = obj_comentario.obtem_atributo(com_T, 'autor')
assert com_T_autor != usr_C
assert com_T_autor != usr_A

# Usuário não logado:
testa_processa("BAD_sesNul",  str, None, { 'comentario': com_T_id })

# Sessão já fechada:
testa_processa("BAD_sesOut",  str, ses_F, { 'comentario': com_T_id })

# Comentário não especificado:
testa_processa("BAD_comNul",  str, ses_A, {})

# Comentario inexistente:
com_X_id = "C-01010101"
testa_processa("BAD_comInv",  str, ses_A, { 'comentario': com_X_id })

# Usuário comum não é autor:
testa_processa("BAD_DeOutro",  str, ses_C, { 'comentario': com_T_id })

# Usuário comum é o autor:
testa_processa("GUD_DoProprio",  str, ses_C, { 'comentario': com_C_id })

# Administrador editando página de outro:
testa_processa("GUD_peloAdm",  str, ses_A, { 'comentario': com_T_id })

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
