#! /usr/bin/python3

import html_pag_generica
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)


def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_generica
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
  util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


def fecha_sessoes(id_usr):
  id_ses_list = obj_sessao.busca_por_usuario(id_usr)
  ses_list = list(map((lambda id_ses: obj_sessao.busca_por_identificador(id_ses)), id_ses_list))
  for ses in ses_list:
    if obj_sessao.aberta(ses):
      obj_sessao.fecha(ses)

pag_conteudo = "Texto de teste"
id_usr_nao_admin = "U-00000001"
id_usr_admin = "U-00000003"

usr_nao_admin = obj_usuario.busca_por_identificador(id_usr_nao_admin)
usr_admin = obj_usuario.busca_por_identificador(id_usr_admin)

# Teste sem sessao
testa("sem_sessao", None, pag_conteudo, None)

# Fecha todas as sessoes
fecha_sessoes(id_usr_nao_admin)
fecha_sessoes(id_usr_admin)

# Teste com apenas uma sessao
# - Nao admin
ses = obj_sessao.cria(usr_nao_admin, "ASDIHADBH")
testa("uma_sessao_nao_admin", ses, pag_conteudo, None)

# - Admin
ses = obj_sessao.cria(usr_admin, "DASDASDD")
testa("uma_sessao_admin", ses, pag_conteudo, None)

# Teste com multiplas sessoes
# - Nao admin
ses = obj_sessao.cria(usr_nao_admin, "GFHFGHHFG")
testa("varias_sessoes_nao_admin", ses, pag_conteudo, None)

# - Admin
ses = obj_sessao.cria(usr_admin, "XCVJXCVVL")
testa("varias_sessoes_admin", ses, pag_conteudo, None)

# Teste de mensagens de erro
testa("lista_erro_vazia", ses, pag_conteudo, [])

testa("lista_error_populada", ses, pag_conteudo, ["Erro 1", "Erro 2", "Erro 3"])
