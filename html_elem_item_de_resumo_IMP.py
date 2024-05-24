import html_estilo_texto
import html_elem_span

def gera(texto, cab, cor_fundo, alinha, cor_texto):
  if cab:
    # Força estilo e cores padronizadas do cabeçalho de coluna:
    peso_fonte = "bold"
    cor_texto = "white"
    cor_fundo = "#60a3bc"
  else:
    peso_fonte = "medium"
    if cor_texto == None: cor_texto = "#000000"

  tam_fonte = "20px"
  margens = ( "0px", "0.30em", "0px", "0.70em" )
  estilo = html_estilo_texto.gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens)
  halign = f"text-align: {alinha}"
  valign = "vertical-align: center"
  html = f"<td style=\"{estilo}; {halign}; {valign};\">" + texto + "</td>"
  return html
