#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_ver_usuario

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
  modulo = comando_ver_usuario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok


# Obtem uma sessao de um usuario que é de administrador:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None and obj_sessao.de_administrador(sesA)
usrA = obj_sessao.obtem_dono(sesA)

# Obtem uma sessao de um usuario comum:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None and not obj_sessao.de_administrador(sesC)
usrC = obj_sessao.obtem_dono(sesC)

# Obtem um usuário que não é nenhum dos dois:
usrD_id = "U-00000004"
usrD = obj_usuario.obtem_objeto(usrD_id)
assert usrD != None and usrD != usrA and usrD != usrC

# Identificador de usuário inexistente:
usrI_id = "U-23000004"
usrI = obj_usuario.obtem_objeto(usrI_id)
assert usrI == None 

for xses, ses in ("N", None), ("A", sesA), ("C", sesC):
  usr_ses = obj_sessao.obtem_dono(ses) if ses != None else None
  usr_ses_id = obj_usuario.obtem_identificador(usr_ses) if usr_ses != None else None
  # Usuário a ver é: implícito, o dono da sessão (explícito), terceiro, ou inexistente:
  for xusr, usr_id in ("N", None), ("P", usr_ses_id), ("T", usrD_id), ("I", usrI_id):
    # Caso {ses==None,xusr=="P"} é igual a {ses==None,xusr=="N"}:
    if not (ses == None and xusr == "P"):
      rot_teste = f"ses{xses}_usr{xusr}"
      cmd_args = { 'usuario': usr_id } if usr_id != None else {}
      testa_processa(rot_teste, str, ses, cmd_args )

if ok_global:
  sys.stderr.write("Testes terminados normalmente")
else:
  aviso_prog("Alguns testes falharam")
