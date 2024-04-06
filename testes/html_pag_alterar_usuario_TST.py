#! /usr/bin/env python3

import sys #mudança de linha
sys.path.insert (0, "/home/cc2018-ceb/ra074126/Downloads/Projeto_2024_03_15/Projeto-MC857-2024-1") #linha acrescentada

import html_pag_alterar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

#import sys #linha original

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste usuario 1:
ses = obj_sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste 1 (nao administrador):
usr1 = obj_sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = obj_usuario.obtem_identificador(usr1)
usr1_atrs = obj_usuario.obtem_atributos(usr1)

# Sessao de teste usuario 2:
ses = obj_sessao.busca_por_identificador("S-00000004")
assert ses != None

# Usuario teste 2 (administrador):
usr2 = obj_sessao.obtem_usuario(ses)
assert usr2 != None
usr2_id = obj_usuario.obtem_identificador(usr2)
usr2_atrs = obj_usuario.obtem_atributos(usr2)

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_alterar_usuario
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for admin in (False, True):
  ad = "-adm"+str(admin)
  for tag, erros in (
      ("N"+ad, None),
      ("V"+ad, []),
      ("B"+ad, "Mensagem UM\nMensagem DOIS\nMensagem TRÊS"),
      ("L"+ad, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
      ("LB"+ad, ["Mensagem UM-A\nMensagem UM-B", "Mensagem DOIS", "Mensagem TRÊS",]),
    ):
    rotulo = tag
    testa_gera(rotulo, ses, usr1_id, usr1_atrs, admin, erros)

sys.stderr.write("Testes terminados normalmente.\n")
