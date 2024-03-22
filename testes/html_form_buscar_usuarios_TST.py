#! /usr/bin/python3
 
# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_buscar_usuarios
import util_testes


def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_buscar_usuarios
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

atrs = { 'nome': "User Test", 'email': "usertest@test.com" }
admin = True
testa_gera("Valores_Incompletos_Admin", atrs, admin)
admin = False
testa_gera("Valores_Incompletos_Comum", atrs, admin)

atrs = {"id_usr": "U-00000001", "nome": "Roberto", "email": "robertin@email.com"}
admin = True
testa_gera("Valores_Completos_Admin", atrs, admin)
admin = False
testa_gera("Valores_Completos_Comum", atrs, admin)

atrs = {}
admin = True
testa_gera("Sem_Valores_Admin", atrs, admin)
admin = False
testa_gera("Sem_Valores_Comum", atrs, admin)

