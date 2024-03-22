#! /usr/bin/python3

import db_tabelas
import db_base_sql
import obj_sessao
import obj_usuario
import html_bloco_tabela_de_campos
import util_testes

import sys

def testa_html_bloco_tabela_de_campos(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_tabela_de_campos
  funcao = modulo.gera
  frag = False # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

dados_linhas = [("Nome",          "text",     "entradaNome",   "", True),
                ("Idade",         "number",   "entradaIdade",  "XX", True),
                ("Telefone",      "tel",      "entradaTel",    "+XX (XX) XXXXX-XXXX", False),
                ("Email",         "email",    "entradaEmail",  "email@domain.com", False),
                ("Carro",         "text",     "entradaCarro",  "Marca-ano", True),
                ("Administrador", "checkbox", "checkboxAdmin", "", True)]

atrs = {"entradaNome":"João Pedro II",
        "entradaIdade":22,
        "entradaTel":"+55 (19) 12345-6789",
        "entradaEmail":"joaopedroii@email.com",
        "entradaCarro":"Cybertruck-2019",
        "checkboxAdmin":True}

testa_html_bloco_tabela_de_campos("comum", dados_linhas, atrs, False)
testa_html_bloco_tabela_de_campos("admin", dados_linhas, atrs, True)

sys.stderr.write("Testes terminados normalmente.\n")
 
