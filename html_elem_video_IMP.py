
def gera(vid_id, altura):
  #Se receber valor {None}, converte string para vazia
  if vid_id is None or vid_id == "": vid_id = "V-00000001.mp4"

  # port_size_x = altura
  # estilo = f"width:{port_size_x}px;"
  port_size_y = altura
  estilo = f"height:{port_size_y}px;"
  ht_video = \
    f'<video style="{estilo}" controls>' + \
    f'<source src="videos/{vid_id}.mp4" type="video/mp4">' + \
    f'Seu browser não entende o elemento HTML &lt;video&gt;' + \
    f'</video>'

  return ht_video
