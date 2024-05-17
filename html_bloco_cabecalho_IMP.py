import html_elem_link_img
import html_estilo_texto
import html_elem_span
import html_elem_div
import html_elem_paragraph

def gera(titulo, grande):
  
  tam_fonte = 60 if grande else 30

  # Logotipo:
  logo_arq = "imagens/logotipo.png"
  logo_descr = "Logotipo do site"
  logo_link = logo_arq
  ht_img = html_elem_link_img.gera(logo_arq, logo_descr, tam_fonte, logo_link)

  # Texto do cabecalho:
  cor_texto = "#000000"
  cor_fundo = "#ffdf31"
  margens = None
  estilo_tit = html_estilo_texto.gera(f"{tam_fonte}px", "bold", cor_texto, cor_fundo, margens)
  margin_tit = f"padding: {tam_fonte//6}px 0px 0px 0px;"
  ht_tit = html_elem_div.gera(estilo_tit + margin_tit, ht_img + " " + titulo)

  ht_cab = "<nav>" +  ht_tit + "</nav>"

  return ht_cab
