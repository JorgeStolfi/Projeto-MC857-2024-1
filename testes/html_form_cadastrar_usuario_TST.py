#! /usr/bin/python3

import html_form_cadastrar_usuario
import obj_usuario
import obj_sessao
import util_identificador
import db_base_sql
import db_tabelas_do_sistema
import util_testes

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
  modulo = html_form_cadastrar_usuario
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Dados para teste:

atrs_nul = dict()
atrs_nom = { 'nome': "Felix Felisberto Feliciano", }
atrs_ema = { 'email': "satanas@fundos.inferno.com", }
atrs_adm = { 'administrador': True, }

for erros_tag, erros in (
    ("N", None),
    ("V", []),
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  xerrs = f"_errs{erros_tag}"
  for para_admin in False, True:
    xpadm = f"_padm{str(para_admin)[0]}"
    for atrs_tag, atrs in ("None", atrs_nul, ), ("Nome", atrs_nom, ), ("Email", atrs_ema, ), ("Adm", atrs_adm, ):
      xatrs = f"_atrs{atrs_tag}"
      rot_teste = "C" + xerrs + xpadm + xatrs
      testa_gera(rot_teste, str, atrs, para_admin)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
