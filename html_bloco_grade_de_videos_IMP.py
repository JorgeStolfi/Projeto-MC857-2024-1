import obj_video
import html_elem_table
import html_elem_link_img
import html_elem_button_simples

def gera_form_botoes_de_ordenacao():
  cor_bt_ordem = "#eeccff"

  ht_bt_melhores = html_elem_button_simples.gera("Melhores", 'ver_grade_de_videos', { 'ordem': "-1" }, cor_bt_ordem)
  ht_bt_aleatorios = html_elem_button_simples.gera("Aleatórios", 'ver_grade_de_videos', { 'ordem': "0" }, cor_bt_ordem)
  ht_bt_piores = html_elem_button_simples.gera("Piores", 'ver_grade_de_videos', { 'ordem': "+1" }, cor_bt_ordem)

  ht_botoes = ht_bt_melhores + " " + ht_bt_aleatorios + " " + ht_bt_piores
  return ht_botoes

def gera(vid_ids, ncols):

  # Estas condições deveriam ser sempre satisfeitas para chamadas do sistema:
  assert isinstance(vid_ids, list) or isinstance(vid_ids, tuple), "lista de vídeos inválida"
  assert isinstance(ncols, int) and ncols > 0, "número de colunas inválido"
      
  erros = []

  ht_linhas = []  # Linhas da grade, cada qual uma lista de elementos.
  ht_elems_linha = []   # Elementos da linha corrente, cada qual um string "<td>...</td>".
  
  for vid_id in vid_ids:
    assert isinstance(vid_id, str)
    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"O vídeo {vid_id} não existe")
    else:
      arquivo = f"thumbs/{vid_id}.png"
      atrs_vid = obj_video.obtem_atributos(vid)
      descr = atrs_vid['titulo']
      alt_px = 80
      url = f"ver_video?video={vid_id}"
      ht_link = html_elem_link_img.gera(arquivo, descr, alt_px, url)
      ht_elem = "<td style=\"text-align: center; border: 1px solid blue; padding:5px;\">&nbsp;" + ht_link + "&nbsp;</td>"
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
    
  ht_tabela = html_elem_table.gera(ht_linhas, None)
  ht_botoes_ordenacao = gera_form_botoes_de_ordenacao()

  ht_bloco = ht_tabela + "\n" + ht_botoes_ordenacao
  
  return ht_bloco
