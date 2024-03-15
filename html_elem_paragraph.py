import html_elem_paragraph_IMP

def gera(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como um parágrafo ('<p style="{estilo}">...</p>').
  Se o {estilo} for {None}, omite o atributo "style"."""
  return html_elem_paragraph_IMP.gera(estilo, conteudo)
