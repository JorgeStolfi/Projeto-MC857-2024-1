#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import html_estilo_botao
import html_estilo_button
import util_testes
from util_erros import aviso_prog

import sys
import re

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {gera_e_usa_estilo(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = html_estilo_button   
  funcao = gera_e_usa_estilo
  frag = True     # Resultado é só um fragmento de página?
  pretty = False  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

def gera_e_usa_estilo(texto, cor_fundo):
  if cor_fundo == None:
    cor_fundo = html_estilo_button.escolhe_cor_fundo(texto)
  estilo = html_estilo_button.gera(cor_fundo)
  ht_botao = f"<button style=\"{estilo}\">{texto}</button>"
  return ht_botao

testa_gera("Ver-Cor", str, "Ver fantasmas", '#60a3bc')

for texto in \
    "Ver fantasmas", \
    "Buscar encrenca", \
    "Minhas queridas", \
    "Meus queridos", \
    "Entrar correndo", \
    "Sair de fininho", \
    "Ok", \
    "OK", \
    "Principal", \
    "Examinar com cuidado", \
    "Alterar o humor", \
    "Cadastrar laranja", \
    "Recalcular o troco", \
    "Rebimbocar a parafuseta" :
  rot_teste = re.sub(r' ', "_", texto)
  testa_gera(rot_teste, str, texto, None)

# ----------------------------------------------------------------------
# Veredito final:
  
if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
