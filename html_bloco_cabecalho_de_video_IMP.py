import obj_video
import obj_usuario
import html_elem_div
import html_elem_span
import html_estilo_texto
import html_estilo_div_dados
import html_elem_link_text

def gera(vid_id, atrs, largura, mostra_id, mostra_data):

  # Validação de tipos (paranóia):
  assert vid_id == None or isinstance(vid_id, str)
  assert atrs == None or isinstance(atrs, dict)
  assert isinstance(largura, int)
  assert isinstance(mostra_id, bool)
  assert isinstance(mostra_data, bool)
  
  estilo_atr = html_estilo_texto.gera("10px", "medium", "#222222", None, None)

  width = f"{largura}px"
  padding = ( "10px", "0px", "5px", "0px" )
  estilo_cabec_div = html_estilo_div_dados.gera("block", width, "break-word", padding, "85%")
   
  spacer = "&nbsp;&nbsp;"
  
  # ----------------------------------------------------------------------
  # Linha 1: data e identificador.
  
  ht_linha_1 = ""

  if mostra_data and 'data' in atrs:
    data = atrs['data']
    if data != None:
      ht_data = html_elem_span.gera(estilo_atr, data)
      ht_linha_1 += ht_data
 
  if mostra_id and vid_id != None:
    ht_vid_id = html_elem_span.gera(estilo_atr, vid_id)
    if ht_linha_1 != "": ht_linha_1 += spacer
    ht_linha_1 += ht_vid_id
    
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
    btn_autor = html_elem_link_text.gera(autor_id, "ver_usuario", { 'usuario': autor_id })
    ht_autor = html_elem_span.gera(estilo_atr, "Autor: " + btn_autor + " " + autor_nome)
    ht_linha_2 += ht_autor
  
  if ht_linha_2 != "": ht_linha_2 += "<br/>"
   
   # ----------------------------------------------------------------------
  # Linha 3: Num de visualizacoes.
  
  ht_linha_3 = ""
  
  if 'vistas' in atrs and atrs['vistas'] != None:
    vistas = str(atrs['vistas'])
    assert vistas != None
    ht_vistas = html_elem_span.gera(estilo_atr, "Visualizações: " + vistas)
    ht_linha_3 += ht_vistas
  
  if ht_linha_3 != "": ht_linha_3 += "<br/>"
   
  # ----------------------------------------------------------------------
  # Cabeçalho:
  
  ht_cabeca = html_elem_div.gera(estilo_cabec_div, ht_linha_1 + ht_linha_2 + ht_linha_3)
  
  return ht_cabeca
