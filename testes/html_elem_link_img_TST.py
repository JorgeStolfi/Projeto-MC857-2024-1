#! /usr/bin/python3

import html_elem_link_img
import util_testes

import sys

ok_global = True # Vira {False} se algum teste falha.

def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  global ok_global
  modulo = html_elem_link_img
  funcao = modulo.gera
  frag = True  # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
 
for arquivo in None, "imagens/wikimedia_dog.png":
  for descr in None, ("Careta canina" if arquivo != None else "Use sua imaginação!"):
    for url in None, "vai_catar_coquinho?fofoca=Est%E3o+Juntos%21":
      tag_arq = "arq" + ("N" if arquivo == None else "Y")
      tag_descr = "descr" + ("N" if descr == None else "Y")
      tag_url = "url" + ("N" if url == None else "Y")
      rot_teste = f"{tag_arq}-{tag_descr}-{tag_url}"
      testa_gera(rot_teste, str, arquivo, descr,  100, url)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n");
else:
  aviso_prog("Alguns testes falharam.", True)
