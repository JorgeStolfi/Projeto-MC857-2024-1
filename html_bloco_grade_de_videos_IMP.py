import random
import html_elem_table

def gera(vid_ids, ncols):

  # Estas condições deveriam ser sempre satisfeitas para chamadas do sistema:
  assert isinstance(vid_ids, list) or isinstance(vid_ids, tuple), "lista de vídeos inválida"
  assert isinstance(ncols, int) and ncols > 0, "número de colunas inválido"
      
  erros = []

  ht_linhas = []  # Linhas da grade, cada qual uma lista de elementos.
  ht_elems_linha = []   # Elementos da linha corrente, cada qual um string "<td>...</td>".
  
  for vid_id in vid_ids:
    assert isisnstance(vid_id, str)
    vid = onj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"vídeo {vid_id} não existe")
    else:
      arquivo = f"thumbs/{vid_id}.png"
      atrs_vid = obj_video.obtem_atributos(vid)
      descr = atrs_vid['titulo']
      alt_px = 80
      url = arquivo
      ht_elem = "<td>" + html_elem_link_img.gera(arquivo, descr, alt_px, url) + "</td>"
      ht_elems_linha.append(ht_elem)
      if len(ht_elems_linha) == ncols:
        # Completou mais uma linha:
        ht_linhas.append(ht_elems_linha)
        ht_elems_linha = []
  
  if len(ht_elems_linha) > 0:
    # Fecha última linha incompleta:
    while len(ht_elems_minha) < ncols:
      ht_elem = "<td> </td>"
      ht_elems_linha.append(ht_elem)
    ht_linhas.append(ht_elems_linha)
    
  ht_tabela = html_elem_table.gera(ht_linhas)
  return ht_tabela
