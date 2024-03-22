
def gera(nome, alt, tam):
  """Constrói o HTML para a imagem com nome {nome} e texto alternativo {alt},
  com {tam} pixels de altura."""

  #Se receber valor {None}, converte string para vazia
  if nome is None or nome == "": nome = "virus.mp4"

  port_size_x = tam
  port_size_y = tam
  estilo = f"width:{port_size_x}px; height:{port_size_y}px;"
  ht_video = \
    f'<video style="{estilo}" controls>' + \
    f'<source src="videos/{nome}" type="video/mp4">' + \
    f'Your browser does not support the video tag.' + \
    f'</video>'

  return ht_video
