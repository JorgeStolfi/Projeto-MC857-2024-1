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

def testa_gera(rot_teste, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  modulo = html_pag_alterar_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.busca_por_identificador(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.busca_por_identificador(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)

ses_dic = { 'A': sesA1, 'C': sesC1, }

# Usuário admnistrador dono de {sesA1}:
usrA1 = obj_sessao.obtem_usuario(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Usuário comum dono de {sesC1}:
usrC1 = obj_sessao.obtem_usuario(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

# Usuario comum que não é dono de nenhuma das duas sessões:
usrC2_id = "U-00000003"
usrC2 = obj_usuario.busca_por_identificador(usrC2_id)
assert usrC2 != None
assert not obj_usuario.obtem_atributo(usrC2,'administrador')

usr_dic = { 'N': None, 'C1': usrC1_id, 'C2': usrC2_id, 'A': usrA1_id, }

erros_vaz = []
erros_tri = ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]

erros_dic = { 'N': None, 'V': erros_vaz, 'E': erros_tri, }

for et, erros in erros_dic.items():
  for st, id_ses in ses_dic.items():
    for ut, id_usr in usr_dic.items():
      if id_usr == None or id_ses == sesA1_id or (id_ses == sesC1_id and id_usr == usrC1_id):
        ses = obj_sessao.busca_por_identificador(id_ses)
        usr = obj_usuario.busca_por_identificador(id_usr)
        atrs_tot = obj_usuario.obtem_atributos(usr)
        atrs_som = { 'nome': "Alteradus", }
        atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
        for at, atrs in atrs_dic.items():
          na = len(atrs.keys())
          rot_teste = f"ses{st}-usr{ut}-atrs{at}-erros{et}"
          testa_gera(rot_teste, ses, id_usr, atrs, erros)


sys.stderr.write("Testes terminados normalmente.\n")
