import obj_video
import obj_usuario
import html_elem_div
import html_elem_span
import html_estilo_texto

def gera(vid_id, atrs, largura, mostra_nota, mostra_dims):

  # Validação de tipos (paranóia):
  assert vid_id == None or isinstance(vid_id, str)
  assert atrs == None or isinstance(atrs, dict)
  assert isinstance(largura, int)
  assert isinstance(mostra_nota, bool)
  assert isinstance(mostra_dims, bool)
  
  estilo_tit = html_estilo_texto.gera("16px", "bold", "#000000", None, None)
  estilo_atr = html_estilo_texto.gera("10px", "medium", "#222222", None, None)
  estilo_cabec_div = f"display:block; width: {largura}px; word-wrap:break-word; padding: 10px 0px 5px 0px; line-height: 85%;"
   
  spacer = "&nbsp;&nbsp;"
  
  # ----------------------------------------------------------------------
  # Linha 1: nota e dimensões:
  
  ht_linha_1 = ""

  if mostra_nota and 'nota' in atrs and atrs['nota'] != None:
    nota = float(atrs['nota'])
    ht_nota = html_elem_span.gera(estilo_atr, "Nota: " + f"{nota:.2f}")
    ht_linha_1 += ht_nota
    
  if mostra_dims:
    # Ou todas as dimensões existem, ou nenhuma existe:
    todas  = True
    nenhuma = True
    for chave in 'duracao', 'altura', 'largura':
      if chave in atrs and atrs[chave] != None:
        nenhuma = False
      else:
        todas = False
    assert todas or nenhuma
    if todas:
      # Formata dimensões:
      duracao = float(atrs['duracao'])/1000 # Em segundos.
      altura = int(atrs['altura'])
      latgura = int(atrs['largura'])
      dims = f"Duracão: {duracao:.3f}s {largura}x{altura}px" 
      ht_dims = html_elem_span.gera(estilo_atr,  dims)
      if ht_linha_1 != "": ht_linha_1 += " "
      ht_linha_1 += ht_dims
  
  if ht_linha_1 != "": ht_linha_1 += "<br/>"
   
  # ----------------------------------------------------------------------
  # Cabeçalho:
  
  ht_rodape = html_elem_div.gera(estilo_cabec_div, ht_linha_1)
  
  return ht_rodape
