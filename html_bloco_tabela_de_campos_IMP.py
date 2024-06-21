import html_elem_label
import html_elem_label
import html_elem_input
import html_elem_table
import html_elem_textarea
import html_elem_link_text
import obj_usuario
import obj_raiz
from util_erros import erro_prog, aviso_prog
import sys

tbc_debug = False;

def gera(dados_linhas, atrs):
  if tbc_debug: sys.stderr.write("  > {html_bloco_tabela_de_campos_IMP.gera}: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  dados_linhas = [linha if len(linha) == 6 else linha + (True,) for linha in dados_linhas]
  linhas = []
  for rotulo, tipo, chave, editavel, dica, decimal in dados_linhas:
    val = (atrs[chave] if chave in atrs else None)
    ident = chave
    chmin = chave + '_min'
    vmin = (atrs[chmin] if chmin in atrs else None)
    ht_rotulo = html_elem_label.gera(rotulo, ": ")
    if (tipo == 'checkbox' and not editavel and val == None):
      val = False
    ht_input = gera_input_ou_textarea(tipo, chave, ident, val, vmin, dica, editavel, decimal)
    if ht_input != None:
      linhas.append(("<td>" + ht_rotulo + "</td>", "<td>" + ht_input + "</td>",))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, None)
  return ht_table

def gera_input_ou_textarea(tipo, chave, ident, val, val_min, dica, editavel, decimal):
  """Retorna o HTML de um item "<input.../>" ou "<textarea>...</textarea>".
  Pode devolver {None} para não mostrar esse item.

  Se o {tipo} for "textarea", gera um elemento "<textarea>{val_ini}</textarea>"
  onde {val_ini} é {val} (ou a {dica} se {val} é {None}).

  Se o {tipo} for "number", utiliza {decimal} para definir o atributo "step", permitindo
  ou não números decimais.
  
  Nos demais casos, gera um elemento "<input type='{tipo}' name='{chave}' id='{ident}' val='{val}'
  min='{val_min}' placeholder='{dica}'/>".
  
  Os valores {val}, {val_min} são convertidos para string de maneira adequada ao seu tipo.
  A {dica} não é convertida.

  Se a chave for 'senha', não mostra o {val}.  Se {tipo}
  não for "number", ignora {val_min}."""

  if chave == 'senha': 
    # Ignora os valores {val}, {val_min}:
    val = None
    val_min = None

  if chave == 'dono':
    id_usuario = obj_usuario.obtem_identificador(val)
    ht_val = html_elem_link_text.gera(id_usuario, "ver_usuario", {"usuario": id_usuario})
    return ht_val

  ht_val = converte_valor(val)
    
  # Determina {ident} do campo:
  ident = None if not ident else ident
    
  # Dica e valor inicial são mutuamente exclusivos:
  if ht_val != None:
    dica = None

  if tipo == "textarea":
    ht_input = html_elem_textarea.gera(None, chave, ident, ht_val, editavel, dica, None, False, 2, 70)
  else:
    if tipo != 'number':
      # Ignora {val_min}:
      val_min = None
      decimal = False
    ht_val_min = converte_valor(val_min)
    ht_input = html_elem_input.gera(tipo, chave, ident, ht_val, ht_val_min, editavel, dica, None, False, decimal)
  
  return ht_input

def converte_valor(val):
  """Converte val de um tipo python para um string que pode ser usado
  no atributo "val=" ou "min=" de um "<input>"."""
  if val == None:
    ht_val = None
  elif type(val) is str:
    ht_val = val
  elif type(val) is bool:
    ht_val = ('on' if val else 'off')
  elif type(val) is float:
    ht_val = ("%.2f" % val)
  elif type(val) is int:
    ht_val = ("%d" % val)
  elif isinstance(val, obj_raiz.Classe):
    ht_val = obj_raiz.obtem_identificador(val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")
  return ht_val
