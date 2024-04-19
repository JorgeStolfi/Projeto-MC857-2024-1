
import html_elem_label
from util_erros import erro_prog

def gera(tipo, chave, ident, val_ini, val_min, editavel, dica, cmd, obrigatorio):
  ht_tipo = " type =\"" + tipo + "\""
  ht_nome = " name=\"" + chave + "\""
  ht_ident = " id=\"" + ident + "\"" if ident != None else ""

  if val_ini != None and dica != None:
    erro_prog("rot_campo '%s' chave '%s': {val_ini} e {dica} são mutuamente exclusivos" % (rot_campo, chave))
    
  if val_ini == None and obrigatorio and (tipo == "hidden" or not editavel):
    erro_prog("rot_campo obrigatorio '%s' chave '%s': {val_ini} não pode ser {None} se o campo não é editável" % (rot_campo, chave))

  ht_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    ht_val_ini += ' checked '

  if tipo == "number" and val_min != None:
    ht_val_min = " min=\"" + val_min + "\""
  else:
    ht_val_min = ""

  ht_checkbox_disabled = (" disabled" if tipo == "checkbox" and not editavel else "")
  ht_obrigatorio = (" required" if obrigatorio else "")
  ht_readonly = ( " readonly" if not editavel else "" )
  ht_readonlybackground = ( " style=\"background-color:#BCBCBC\"" if not editavel else "" )
  ht_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  ht_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  ht_estilo = ( " style=\"background-color:#c7c7c7\"" if not editavel else "" )
  ht_input = \
    "<input" + \
      ht_tipo + \
      ht_nome + \
      ht_ident + \
      ht_val_ini + \
      ht_readonly + \
      ht_readonlybackground + \
      ht_checkbox_disabled + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo + \
    "/>"
  return ht_input
