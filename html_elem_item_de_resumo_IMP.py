import html_estilo_texto
import html_elem_span

def gera(texto, cab, cor_fundo, alinha):

  if cab:
    peso_fonte = "bold"
    cor_texto = "white"
    # Ignora a cor do fundo especificada:
    cor_fundo = "#60a3bc"
  else:
    peso_fonte = "medium"
    cor_texto = "#000000"
    
  # !!! Cada linha do {texto} deveria ser truncada por um limite dado. !!!
  # !!! Se o texto tem várias linhas deveria envolver em <p>...</p> !!!
  # !!! Nesse caso as margens deveriam ir no <p> não no <span> !!!
  # !!! Talvez com estilo_parag = "\n display:block; word-wrap:break-word; width: 100%; text-indent: 0px; line-height: 75%;" !!!

  tam_fonte = "20px"
  margens = ( "0px", "0.30em", "0px", "0.70em" )
  estilo = html_estilo_texto.gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens)
  halign = f"text-align: {alinha}"
  valign = "vertical-align: center"
  html = f"<td style=\"{estilo}; {halign}; {valign};\">" + texto + "</td>"
  return html
