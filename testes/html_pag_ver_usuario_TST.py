#! /usr/bin/python3

from util_erros import ErroAtrib, erro_prog, aviso_prog
import html_pag_ver_usuario
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

  modulo = html_pag_ver_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.busca_por_identificador(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)
usrA1 = obj_sessao.obtem_usuario(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.busca_por_identificador(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)
usrC1 = obj_sessao.obtem_usuario(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

# Usuario comum que não é dono de nenhuma das duas sessões:
usrC2_id = "U-00000003"
usrC2 = obj_usuario.busca_por_identificador(usrC2_id)
assert usrC2 != None
assert not obj_usuario.obtem_atributo(usrC2,'administrador')

for tag, erros in (
    ("N", None),
    ("V", []),
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  for id_ses in None, sesA1_id, sesC1_id:
    for id_usr in None, usrC1_id, usrC2_id, usrA1_id:
      if id_ses != None or id_usr != None:
        rot_teste = tag + "-ses" + str(id_ses) + "-usr" + str(id_usr)
        ses = obj_sessao.busca_por_identificador(id_ses)
        usr = obj_usuario.busca_por_identificador(id_usr)
        testa_gera(rot_teste, ses, id_usr, erros)

sys.stderr.write("Testes terminados normalmente.\n")
