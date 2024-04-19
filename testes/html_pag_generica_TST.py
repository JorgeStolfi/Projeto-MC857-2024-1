#! /usr/bin/python3

import html_pag_generica
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
  
  modulo = html_pag_generica
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True  # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

def fecha_sessoes(id_usr):
  # Obtem identificadores das sessões abertas:
  id_ses_list = obj_sessao.busca_por_usuario(id_usr, True)
  ses_list = list(map((lambda id_ses: obj_sessao.busca_por_identificador(id_ses)), id_ses_list))
  for ses in ses_list:
    assert obj_sessao.aberta(ses)
    obj_sessao.fecha(ses)

pag_conteudo = "Texto de teste"
id_usr_admin = "U-00000001"
id_usr_comum = "U-00000003"

usr_comum = obj_usuario.busca_por_identificador(id_usr_comum)
usr_admin = obj_usuario.busca_por_identificador(id_usr_admin)

# Teste sem sessao
testa_gera("sem_sessao", None, pag_conteudo, None)

# Fecha todas as sessoes
fecha_sessoes(id_usr_comum)
fecha_sessoes(id_usr_admin)

# Teste com apenas uma sessao
# - Nao admin
ses = obj_sessao.cria(usr_comum, "ASDIHADBH")
testa_gera("uma_sessao_comum", ses, pag_conteudo, None)

# - Admin
ses = obj_sessao.cria(usr_admin, "DASDASDD")
testa_gera("uma_sessao_admin", ses, pag_conteudo, None)

# Teste com multiplas sessoes
# - Nao admin
ses = obj_sessao.cria(usr_comum, "GFHFGHHFG")
testa_gera("varias_sessoes_comum", ses, pag_conteudo, None)

# - Admin
ses = obj_sessao.cria(usr_admin, "XCVJXCVVL")
testa_gera("varias_sessoes_admin", ses, pag_conteudo, None)

# Teste de mensagens de erro
testa_gera("lista_erro_vazia", ses, pag_conteudo, [])

testa_gera("lista_error_populada", ses, pag_conteudo, ["Erro 1", "Erro 2", "Erro 3"])

sys.stderr.write("Testes terminados normalmente.\n")
