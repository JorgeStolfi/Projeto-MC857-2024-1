import html_estilo_de_botao
import re

def gera(texto, URL, args, cor_fundo):
  if args != None:
    # Acrescenta argumentos ao {URL}:
    sep = '?'
    for key, val in args.items():

      # Verifica se {key} tem caracteres invalidos
      key_invalid_characters = re.findall("[^a-zA-Z0-9\.\-_]", key)

      if val != None and val != "" and len(key_invalid_characters) == 0:

        # Verifica se {val} tem caracteres invalidos
        val_invalid_characters = re.findall("[^a-zA-Z0-9\.\,\-_]", val)

        # Adiciona parametro no URL somente se {key} e {val} nao tiverem caracteres invalidos
        if (len(val_invalid_characters) == 0):
            URL += (sep + key + "=" + str(val))
            sep = '&'

  # Constrói o botão propriamente dito:
  estilo = html_estilo_de_botao.gera(cor_fundo)
  html = "<button type=\"button\" style=\"" + estilo + "\" onclick=\"location.href='" + URL + "'\">" + texto + "</button>"
  return html
