#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import html_bloco_dados_de_usuario
import obj_usuario
import obj_sessao
import db_base_sql
import db_tabelas_do_sistema
import util_testes
import util_identificador

import sys

from obj_usuario import obtem_atributos, obtem_identificador

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_bloco_dados_de_usuario
  funcao = modulo.gera
  frag = True # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.obtem_objeto(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)
usrA1 = obj_sessao.obtem_dono(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.obtem_objeto(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)
usrC1 = obj_sessao.obtem_dono(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

# Usuario comum que não é dono de nenhuma das duas sessões:
usrC2_id = "U-00000003"
usrC2 = obj_usuario.obtem_objeto(usrC2_id)
assert usrC2 != None
assert not obj_usuario.obtem_atributo(usrC2,'administrador')

for ses_id in None, sesA1_id, sesC1_id:
  for usr_a_ver_id in None, usrC1_id, usrC2_id, usrA1_id:
    ses = obj_sessao.obtem_objeto(ses_id) if ses_id != None else None
    para_admin = obj_sessao.de_administrador(ses) if ses != None else False
    usr_a_ver = obj_usuario.obtem_objeto(usr_a_ver_id) if usr_a_ver_id != None else None
    usr_ses = obj_sessao.obtem_dono(ses) if ses != None else None
    usr_ses_id = obj_usuario.obtem_identificador(usr_ses) if usr_ses != None else None
    para_proprio = ( usr_a_ver_id != None and usr_a_ver_id == usr_ses_id )
    atrs_pairs = ( ( 'N', {}, ), ('U', obj_usuario.obtem_atributos(usr_a_ver), ), ) if usr_a_ver != None else ( ('N', {}, ), )
    for editavel in False, True:
      if (editavel or usr_a_ver_id != None) and (not editavel or ( para_admin or para_proprio )):
        for atrs_tag, atrs_basic in atrs_pairs:
          atrs = atrs_basic.copy()
          xatrs = "_atrs" + atrs_tag
          if usr_a_ver_id != None and editavel:
            # Tenta apresentar outro 'nome':
            atrs.update({ 'nome': "Seracomeço Nãoquerubim" })
            xatrs += "_nomeDif"
            if para_admin:
              # Tenta apresentar outro atributo 'administrador':
              usr_a_ver_admin = obj_usuario.eh_administrador(usr_a_ver)
              atrs.update({ 'administrador': not usr_a_ver_admin })
              xatrs += "_adminMod"
          xses = f"_S{ses_id[-3:]}" if ses_id != None else "_SNone"
          xusr = f"_U{usr_a_ver_id[-3:]}" if usr_a_ver_id != None else "_UNone"
          rot_teste = "D" + xatrs + xses + xusr
          testa_gera(rot_teste, str, usr_a_ver_id, atrs, editavel, para_admin, para_proprio)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Alguns testes falharam", True)
