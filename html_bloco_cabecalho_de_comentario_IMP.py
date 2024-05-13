import obj_video
import obj_usuario
import obj_comentario
import html_elem_div
import html_elem_span
import html_estilo_texto

def gera(com_id, atrs, largura, mostra_id, mostra_data, mostra_video, mostra_pai):

  # Validação de tipos (paranóia):
  assert com_id == None or isinstance(com_id, str)
  assert atrs == None or isinstance(atrs, dict)
  assert isinstance(largura, int)
  assert isinstance(mostra_video, bool)
  assert isinstance(mostra_pai, bool)
  
  estilo_atr = html_estilo_texto.gera("10px", "medium", "#222222", None, None)
  estilo_cabec_div = f"display:block; width: {largura}px; word-wrap:break-word; padding: 10px 0px 5px 0px; line-height: 85%;"
   
  spacer = "&nbsp;&nbsp;"
  
  # ----------------------------------------------------------------------
  # Linha 1: data e identificador.
  
  ht_linha_1 = ""

  if mostra_data and 'data' in atrs:
    data = atrs['data']
    if data != None:
      ht_data = html_elem_span.gera(estilo_atr, data)
      ht_linha_1 += ht_data
 
  if mostra_id and com_id != None:
    ht_com_id = html_elem_span.gera(estilo_atr, com_id)
    if ht_linha_1 != "": ht_linha_1 += spacer
    ht_linha_1 += ht_com_id
    
  if ht_linha_1 != "": ht_linha_1 += "<br/>"
  
  # ----------------------------------------------------------------------
  # Linha 2: identificador e nome do autor.
  
  ht_linha_2 = ""
  
  if 'autor' in atrs and atrs['autor'] != None:
    if isinstance(atrs['autor'], obj_usuario.Classe):
      autor = atrs['autor']
      autor_id = obj_usuario.obtem_identificador(autor)
    else:
      autor_id = atrs['autor']
      autor = obj_usuario.obtem_objeto(autor_id)
    assert autor != None
    autor_nome = obj_usuario.obtem_atributo(autor, 'nome')
    assert autor_id != None
    assert autor_nome != None
    ht_autor = html_elem_span.gera(estilo_atr, "Por: " + autor_id + " " + autor_nome)
    ht_linha_2 += ht_autor
  
  if ht_linha_2 != "": ht_linha_2 += "<br/>"

  # ----------------------------------------------------------------------
  # Linha 3: vídeo e comentário-pai.
  
  ht_linha_3 = ""

  if mostra_video and 'video' in atrs and atrs['video'] != None:
    if isinstance(atrs['video'], obj_video.Classe):
      video = atrs['video']
      video_id = obj_video.obtem_identificador(video)
    else:
      video_id = atrs['video']
      video = obj_video.obtem_objeto(video_id)
    assert video != None
    assert video_id != None
    ht_video = html_elem_span.gera(estilo_atr, "Sobre: " + video_id)
    ht_linha_3 += ht_video
    
  if mostra_pai and 'pai' in atrs and atrs['pai'] != None:
    if isinstance(atrs['pai'], obj_comentario.Classe):
      pai = atrs['pai']
      pai_id = obj_comentario.obtem_identificador(pai)
    else:
      pai_id = atrs['pai']
      pai = obj_comentario.obtem_objeto(pai_id)
    assert pai != None
    assert pai_id != None
    ht_pai = html_elem_span.gera(estilo_atr, "Em resposta a: " + pai_id)
    if ht_linha_3 != "": ht_linha_3 += " "
    ht_linha_3 += ht_pai
  
  if ht_linha_3 != "": ht_linha_3 += "<br/>"
   
  # ----------------------------------------------------------------------
  # Cabeçalho:
  
  ht_cabeca = html_elem_div.gera(estilo_cabec_div, ht_linha_1 + ht_linha_2 + ht_linha_3)
  
  return ht_cabeca
