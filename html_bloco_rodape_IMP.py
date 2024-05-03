import html_estilo_texto
import html_elem_paragraph
import html_elem_span

from datetime import datetime, timezone

def gera():
  data_bin = datetime.now(timezone.utc)
  data_fmt = data_bin.strftime("%Y-%m-%d %H:%M:%S %Z")

  cor_texto = "#557799"
  cor_fundo = None
  margens = None
  estilo_data = html_estilo_texto.gera("16px", "medium", cor_texto, cor_fundo, margens)
  ht_data = html_elem_paragraph.gera(None, html_elem_span.gera(estilo_data, "Página gerada em " + data_fmt))
  ht_bloco = ht_data
  return ht_bloco
