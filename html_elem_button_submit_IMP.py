import html_estilo_de_botao
import html_elem_input

def gera(texto, URL, cmd_args, cor_fundo):
  args_html = ""
  if cmd_args != None:
    # Acrescenta argumentos ao {args_html}:
    for key, val in cmd_args.items():
      kv_html = html_elem_input.gera(None, 'hidden', key, val, None, False, None, None)
      args_html += kv_html

  # O botão propriamente dito:
  estilo = html_estilo_de_botao.gera(cor_fundo)
  html = args_html + \
    "<input" + \
    " type=\"submit\"" + \
    " style=\"" + estilo + "\n\"" + \
    " formaction=\"" + URL + "\"" + \
    " value=\"" + texto + "\"" + \
    "/>"
  return html
