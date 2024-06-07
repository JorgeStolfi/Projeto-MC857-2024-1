
import html_elem_label
import html_estilo_button

from util_erros import erro_prog, aviso_prog

def input_file_wrapper(ht_input, ident, txt_botao):
  # Estilo para esconder botao original
  # Fonte: https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications#using_a_label_element_to_trigger_a_hidden_file_input_element
  estilo_visualmente_escondido = "<style>" + \
  ".visualmente-escondido { position: absolute !important; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px); }" + \
  "input.visualmente-escondido:is(:focus, :focus-within) + label { outline: thin dotted; }" + \
  "</style>" 
  estilo_botao = "style=\"" + html_estilo_button.gera("#a091ff") + "\""

  # Junta tudo
  ht_input_wrapper_inicio = "<div>" + \
  "<label "+ estilo_botao +" for=" + str(ident) + ">" + str(txt_botao) + "</label>"
  ht_input_wrapper_fim = "</div>"
  return estilo_visualmente_escondido + ht_input_wrapper_inicio + ht_input + ht_input_wrapper_fim

def gera(tipo, chave, ident, val_ini, val_min, editavel, dica, cmd, obrigatorio, decimal):
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
  ht_decimal = (" step=\"0.01\"" if decimal else "" )
  # Se for input de upload de arquivo, esconder estilo do browser e utilizar o nosso
  ht_classe = ("class=\"visualmente-escondido\"" if tipo == "file" else "")
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
      ht_decimal + \
      ht_classe + \
    "/>"
  
  if tipo == "file":
    # Envolve o input com nosso estilo
    ht_input = input_file_wrapper(ht_input, ident, "Subir video")

  return ht_texto_simples + ht_input
