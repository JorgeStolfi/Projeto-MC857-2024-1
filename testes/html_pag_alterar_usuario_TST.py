#! /usr/bin/env python3

import html_pag_alterar_usuario
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

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
  modulo = html_pag_alterar_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.obtem_objeto(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.obtem_objeto(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)

ses_dic = { 'A': sesA1_id, 'C': sesC1_id, }

# Usuário admnistrador dono de {sesA1}:
usrA1 = obj_sessao.obtem_dono(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Usuário comum dono de {sesC1}:
usrC1 = obj_sessao.obtem_dono(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

# Usuario comum que não é dono de nenhuma das duas sessões:
usrC2_id = "U-00000003"
usrC2 = obj_usuario.obtem_objeto(usrC2_id)
assert usrC2 != None
assert not obj_usuario.obtem_atributo(usrC2,'administrador')

usr_dic = { 'C1': usrC1_id, 'C2': usrC2_id, 'A': usrA1_id, }

erros_vaz = []
erros_tri = ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]

erros_dic = { 'N': None, 'V': erros_vaz, 'E': erros_tri, }

for et, erros in erros_dic.items():
  for st, ses_id in ses_dic.items():
    for ut, usr_id in usr_dic.items():
      if usr_id == None or ses_id == sesA1_id or (ses_id == sesC1_id and usr_id == usrC1_id):
        usr = obj_usuario.obtem_objeto(usr_id)
        atrs_tot = obj_usuario.obtem_atributos(usr) if usr != None else {}
        atrs_som = { 'nome': "Alteradus", }
        atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
        for at, atrs in atrs_dic.items():
          na = len(atrs.keys())
          ses = obj_sessao.obtem_objeto(ses_id)
          assert ses != None
          rot_teste = "AU" + f"_ses{st}_usr{ut}_atrs{at}_erros{et}"
          # html_pag_alterar_usuario.gera
          testa_gera(rot_teste,  str, ses, usr_id, atrs, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
