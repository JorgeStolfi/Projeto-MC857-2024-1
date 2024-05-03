import html_estilo_titulo
import html_elem_span

def gera(tit):
  estilo = html_estilo_titulo.gera("#000000")
  ht_texto = html_elem_span.gera(estilo, tit)
  ht_titulo = "<h3>" + ht_texto + "</h3>"
  return ht_titulo
