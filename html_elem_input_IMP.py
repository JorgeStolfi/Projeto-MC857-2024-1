import html_estilo_button
import html_estilo_texto

from util_erros import erro_prog, aviso_prog

# Gera um id para os componentes do form de acordo com o ident do pai
def gerar_id_customizado(ident, id):
  return str(ident) + "_" + id

def gerar_event_listener(id_alvo, tipo_evento, funcao):
  return "<script>" + \
  "document.getElementById(\"" + id_alvo + "\").addEventListener(\"" + tipo_evento + "\", " + funcao + ")" + \
  "</script>"

# Estilo para esconder botao original
# Fonte: https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications#using_a_label_element_to_trigger_a_hidden_file_input_element
def gerar_estilo_visualmente_escondido():
  return "<style>" + \
  ".visualmente-escondido { position: absolute !important; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px); }" + \
  "input.visualmente-escondido:is(:focus, :focus-within) + label { outline: thin dotted; }" + \
  "</style>" 

def input_file_wrapper(ht_input, ident, txt_botao):
  texto_nenhum_arquivo_selectionado = 'Nenhum arquivo selecionado'

  # IDs usados nos componentes
  id_botao_nativo = str(ident)
  id_botao_arquivo = gerar_id_customizado(id_botao_nativo, "botao_arquivo")
  id_label_botao_arquivo = gerar_id_customizado(id_botao_nativo, "label_botao_arquivo")

  estilo_botao = "style=\"" + html_estilo_button.gera("#a091ff") + "\""

  # Gera JS para clique do botão que substitui o nativov
  funcao_on_click_botao = "function (event) { document.getElementById('"+ id_botao_nativo +"').click() }"
  script_on_click_botao = gerar_event_listener(id_botao_arquivo, 'click', funcao_on_click_botao)

  botao_interno = "<button id=\"" + id_botao_arquivo + "\" type=\"button\" "+ estilo_botao +"/>" + str(txt_botao) + "</button>"

  # Altera o conteúdo do span de acordo com o nome do arquivo selecionado
  funcao_on_change_file = "function (event) {" + \
  "let fileName = event.target.files[0] ? event.target.files[0].name : '"+ texto_nenhum_arquivo_selectionado +"';" + \
  "document.getElementById('"+ id_label_botao_arquivo +"').textContent = fileName;" + \
  "}"
  script_on_change_file = gerar_event_listener(id_botao_nativo, 'change', funcao_on_change_file)

  estilo_label_botao_arquivo = html_estilo_texto.gera("16px", "medium", "#109F4A", None, ( "0px", "0.30em", "0px", "0.70em" ))
  ht_label_arquivo_selecionado =   "<span id=\""+ id_label_botao_arquivo +"\"" + \
    "style=\"" + estilo_label_botao_arquivo + "\">" + \
    texto_nenhum_arquivo_selectionado + \
    "</span>"

  # Junta tudo
  ht_input_wrapper_inicio = "<div>" + \
    "<label for=" + id_botao_nativo + ">" + botao_interno + "</label>" + \
    ht_label_arquivo_selecionado

  ht_input_wrapper_fim = "</div>"
  return gerar_estilo_visualmente_escondido() + ht_input_wrapper_inicio + ht_input + ht_input_wrapper_fim + script_on_click_botao + script_on_change_file

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
    ht_input = input_file_wrapper(ht_input, ident, "Escolher arquivo")

  return ht_texto_simples + ht_input
