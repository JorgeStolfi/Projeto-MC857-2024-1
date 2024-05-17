
import html_elem_label
import html_elem_paragraph
import html_estilo_texto
from util_erros import erro_prog, aviso_prog

import sys

def gera(rot_campo, chave, ident, val_ini, editavel, dica, cmd, obrigatorio, altura, largura):
  # sys.stderr.write("   > {html_elem_textarea.gera}: {rot_campo} = %s {largura} = %s\n" % (str(rot_campo), str(largura)))
  
  ht_rot_campo = html_elem_label.gera(rot_campo, ": ")
  ht_ident = " id=\"" + ident + "\"" if ident != None else ""
  ht_nome = " name=\"" + chave + "\""

  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  if val_ini == None and not editavel:
    erro_prog("{val_ini} não pode ser {None} se o campo não é editável")

  # Se não é editável, exibe como um paragraph seguido de um input hidden:
  if not editavel:
    ht_parag = html_elem_paragraph.gera(None, val_ini)
    ht_val_ini = " value =\"" + val_ini + "\""
    ht_hidden = " hidden" 
    ht_parms = \
      ht_hidden
    ht_fill = val_ini
  else:
    maxCaracs = 5000
    ht_parag = ""
    ht_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
    ht_obrigatorio = " required" if obrigatorio else ""
    ht_readonly = "" 
    ht_linhas = " rows=\"" + str(altura) + "\"" if altura != None else ""
    ht_colunas = " cols=\"" + str(largura) + "\"" if largura != None else ""
    ht_maxCarac = " maxlength=\"" + str(maxCaracs) + "\"" if maxCaracs != None else ""
    ht_dica = "placeholder=\"" + dica + "\"" if dica != None else ""
    ht_cmd = "onchange=\"window.location.href=" + cmd + "\"" if cmd != None else ""
    ht_fill = ( str(val_ini) if val_ini != None else "")

    cor_texto = "#000000"
    cor_fundo = None
    margens = None
    estilo = html_estilo_texto.gera("18px", "medium", cor_texto, cor_fundo, margens)
    ht_estilo = " style=\"" + estilo + "\""

    ht_parms = \
      ht_linhas + \
      ht_colunas + \
      ht_maxCarac + \
      ht_readonly + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo
  
  ht_parms = \
    ht_nome + \
    ht_ident + \
    ht_val_ini + \
    ht_parms

  ht_input_textarea = ht_rot_campo
      
  ht_input_textarea = ht_parag + "<textarea" + ht_parms + ">" + ht_fill + "</textarea>"
  return ht_input_textarea
