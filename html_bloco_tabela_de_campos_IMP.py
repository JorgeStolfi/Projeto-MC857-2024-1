import html_elem_label
import html_elem_input
import html_elem_table
import html_elem_textarea
from util_testes import erro_prog
import sys

tbc_debug = False;

def gera(dados_linhas, atrs, privilegio):
  if tbc_debug: sys.stderr.write("  > {html_bloco_tabela_de_campos_IMP.gera}: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rot, tipo, chave, dica, prot in dados_linhas:
    if tbc_debug: sys.stderr.write("  > privilegio: " + str(privilegio) + " prot: " + str(prot) + "\n")
    val = (atrs[chave] if chave in atrs else None)
    chmin = chave + '_min'
    vmin = (atrs[chmin] if chmin in atrs else None)
    ht_rotulo = html_elem_label.gera(rot, ": ")
    editavel = privilegio or not prot
    if (tipo == 'checkbox' and not editavel and val == None):
      val = False
    ht_campo = gera_campo(tipo, chave, val, vmin, dica, editavel)
    if ht_campo != None:
      linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, None)
  return ht_table

def gera_campo(tipo, chave, val, vmin, dica, editavel):
  """Retorna o HTML de um item "input" do formulário
  de dados de usuário. Pode devolver {None} para não mostrar esse item.

  O elemento terá o dado {tipo} ("text", "password", etc.), nome {chave},
  valor inicial {val}, valor mínimo {vmin}, e a {dica} especificada 
  (se {val} for {None}).  O valor inicial {val} é convertido para string 
  de maneira adequada ao seu tipo.

  Se a chave for 'senha', não mostra o {val}.  Se {tipo}
  não for "number", ignora {vmin}."""

  if chave == 'senha': val = None
  
  if tipo == 'number': 
    ht_vmin = str(vmin)
  else:
    ht_vmin = None

  # Converte val para HTML:
  if val == None:
    ht_valor = None
  elif type(val) is str:
    ht_valor = val
  elif type(val) is bool:
    ht_valor = ('on' if val else 'off')
  elif type(val) is float:
    ht_valor = ("%.2f" % val)
  elif type(val) is int:
    ht_valor = ("%d" % val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")

  # Dica e valor inicial são mutuamente exclusivos:
  if ht_valor == None:
    ht_dica = dica
  else:
    ht_dica = None

  if tipo != "textarea":
    ht_campo = html_elem_input.gera(None, tipo, chave, ht_valor, ht_vmin, editavel, ht_dica, None, False)
  else:
    ht_campo = html_elem_textarea.gera(None, tipo, chave, ht_valor, ht_vmin, editavel, ht_dica, None)
  
  return ht_campo
