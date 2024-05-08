import html_elem_button_simples

def gera(conteudo, multipart):
  if multipart:
    enctype = " enctype=\"multipart/form-data\""
    metodo = "method=\"POST\""
  else:
    enctype = "" 
    metodo  = ""
  ht_form = f"<form{enctype}{metodo}>" + conteudo + "</form>"
  
  # Botão de conversa
  ht_bt_conversa = html_elem_button_simples.gera("Ver conversa", 'html_pag_ver_conversa', None, '#808080')

  return ht_form + ht_bt_conversa
