import html_estilo_botao
import html_elem_input
import html_estilo_button

def gera(texto, URL, cmd_args, cor_fundo):
  args_html = ""
  if cmd_args != None:
    # Acrescenta argumentos ao {args_html}:
    for chave, val in cmd_args.items():
      tipo = "hidden"
      ident = None # Por enquanto. Devia ser argumento.
      val_min = None
      editavel = False
      dica = None
      cmd = None
      obrigatorio = False
      ht_input = html_elem_input.gera(tipo, chave, ident, val, val_min, editavel, dica, cmd, obrigatorio)
      args_html += ht_input

  # O botão propriamente dito:
  if cor_fundo == None:
    cor_fundo = html_estilo_button.escolhe_cor_fundo(texto)
  estilo = html_estilo_botao.gera(cor_fundo)
  html = args_html + \
    "<input" + \
    " type=\"submit\"" + \
    " style=\"" + estilo + "\n\"" + \
    " formaction=\"" + URL + "\"" + \
    " value=\"" + texto + "\"" + \
    "/>"
  return html
