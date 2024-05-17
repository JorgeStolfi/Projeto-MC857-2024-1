
import html_elem_label
from util_erros import erro_prog, aviso_prog

def gera(tipo, chave, ident, val_ini, val_min, editavel, dica, cmd, obrigatorio):
  if tipo == "hidden" and editavel:
    erro_prog("chave '%s': campo de tipo 'hidden' não pode ser editável" % chave)
    
  if dica != None and not editavel:
    erro_prog("chave '%s': {dica} tem que ser {none} se o campo não é editável" % chave)

  if val_ini != None and dica != None:
    erro_prog("chave '%s': {val_ini} e {dica} são mutuamente exclusivos" % chave)
    
  if val_ini == None and obrigatorio and not editavel:
    erro_prog("chave '%s' (obrigatoria): {val_ini} não pode ser {None} se o campo não é editável" % chave)
  
  if tipo == "hidden" or editavel or val_ini == None:
    # Gera apenas o "<input .../>":
    ht_texto_simples = ""
  else:
    # Gera um campo de texto simples seguido de um "<input type='hidden'.../>":
    ht_texto_simples = str(val_ini)
    tipo = "hidden"
  
  ht_tipo = " type =\"" + tipo + "\""
  ht_nome = " name=\"" + chave + "\""
  ht_ident = " id=\"" + ident + "\"" if ident != None else ""

  ht_val_ini = ( " value =\"" + str(val_ini) + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    ht_val_ini += ' checked '

  if tipo == "number" and val_min != None:
    if val_ini != None and float(val_ini) < float(val_min):
      erro_prog("chave '%s': {val_ini} = %s menor que {val_min} = %s" % (chave, val_ini, val_min))
    ht_val_min = " min=\"" + str(val_min) + "\""
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
      ht_val_min + \
      ht_readonly + \
      ht_readonlybackground + \
      ht_checkbox_disabled + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo + \
    "/>"
  return ht_texto_simples + ht_input
