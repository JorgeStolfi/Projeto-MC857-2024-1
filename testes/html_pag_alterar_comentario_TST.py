#! /usr/bin/env python3

import html_pag_alterar_comentario
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
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
  modulo = html_pag_alterar_comentario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Sessao de usuário  administrador:
sesA1_id = "S-00000006"
sesA1 = obj_sessao.obtem_objeto(sesA1_id)
assert sesA1 != None
assert obj_sessao.aberta(sesA1)
assert obj_sessao.de_administrador(sesA1)
usrA1 = obj_sessao.obtem_usuario(sesA1)
usrA1_id = obj_usuario.obtem_identificador(usrA1)
assert usrA1_id == "U-00000008"

# Sessão de usuário comum:
sesC1_id = "S-00000003"
sesC1 = obj_sessao.obtem_objeto(sesC1_id)
assert sesC1 != None
assert obj_sessao.aberta(sesC1)
assert not obj_sessao.de_administrador(sesC1)
usrC1 = obj_sessao.obtem_usuario(sesC1)
usrC1_id = obj_usuario.obtem_identificador(usrC1)
assert usrC1_id == "U-00000002"

ses_dic = { 'A': sesA1, 'C': sesC1, }

# Um comentário de {usrC1}:
comC1_id = "C-00000002"
comC1 = obj_comentario.obtem_objeto(comC1_id)
assert comC1 != None
assert obj_comentario.obtem_atributo(comC1, 'autor') == usrC1

# Um comentário de outro usuário, nenhum dos dois:
comC2_id = "C-00000005"
comC2 = obj_comentario.obtem_objeto(comC2_id)
assert comC2 != None
assert obj_comentario.obtem_atributo(comC2, 'autor') != usrC1
assert obj_comentario.obtem_atributo(comC2, 'autor') != usrA1

com_dic = { 'C1': comC1_id, 'C2': comC2_id, }

erros_vaz = []
erros_tri = ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]

erros_dic = { 'N': None, 'V': erros_vaz, 'E': erros_tri, }

for st, ses in ses_dic.items():
  for vt, id_vid in com_dic.items():
    for et, erros in erros_dic.items():
      if ses == sesA1 or (ses == sesC1 and id_vid == comC1_id):
        com = obj_comentario.obtem_objeto(id_vid)
        atrs_tot = obj_comentario.obtem_atributos(com)
        atrs_som = { 'texto': "Alteradus", }
        atrs_dic = { 'N': {}, 'T': atrs_tot, 'S': atrs_som, }
        for at, atrs in atrs_dic.items():
          rot_teste = f"ses{st}-com{vt}-atrs{at}-erros{et}"
          testa_gera(rot_teste,  str, ses, id_vid, atrs, erros)

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
