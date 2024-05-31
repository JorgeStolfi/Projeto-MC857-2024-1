#! /usr/bin/python3

import db_tabelas_do_sistema
import db_base_sql
import obj_sessao
import obj_usuario
import html_bloco_tabela_de_campos
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_bloco_tabela_de_campos
  funcao = modulo.gera
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

linhas = []
for ed in False, True:
  linhas += \
    [ ("Nome",          "text",     "itNome",        ed, (""                    if ed else None), False,),
      ("Carro",         "text",     "itCarro",       ed, ("Marca-ano"           if ed else None), False,),
      ("Idade",         "number",   "itIdade",       ed, ("XX"                  if ed else None), False,),
      ("Telefone",      "tel",      "itTel",         ed, ("+XX (XX) XXXXX-XXXX" if ed else None), False,),
      ("Email",         "email",    "itEmail",       ed, ("email@domain.com"    if ed else None), False,),
      ("Administrador", "checkbox", "checkboxAdmin", ed, (""                    if ed else None), False,),
      ("Patrocinador",  "text",     "itPatro",       ed, ("U-NNNNNNNN"          if ed else None), False,),
      ("Lema",          "textarea", "itLema",        ed, ("Seu lema"            if ed else None), False,),
    ]

linhas.append( ("Segredo", "hidden", "itSegredo", False, None, False, ) )

  
usr3_id = "U-00000003"
usr3 = obj_usuario.obtem_objeto(usr3_id)
assert usr3 != None

atrs = \
  { 'itNome': "João Pedro II",
    'itIdade': 22,
    'itTel': "+55(19)12345-6789",
    'itEmail': "joaopedroii@email.com",
    'itCarro': "Cybertruck 2019",
    'checkboxAdmin': True,
    'itPatro': usr3,
    'itLema': "Unidos Grudaremos",
    'itSegredo': "Polichinelo é fofoqueiro",
  }

testa_gera("teste", str, linhas, atrs)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
 
