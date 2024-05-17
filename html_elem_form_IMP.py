import html_elem_button_simples

def gera(conteudo, multipart):
  if multipart:
    enctype = " enctype=\"multipart/form-data\""
    metodo = "method=\"POST\""
  else:
    enctype = "" 
    metodo  = ""
  ht_form = f"<form{enctype}{metodo}>" + conteudo + "</form>"

  return ht_form
