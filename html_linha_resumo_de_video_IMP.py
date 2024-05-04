import obj_video
import obj_usuario
import html_elem_item_de_resumo
import html_elem_span
import html_elem_button_simples
import html_estilo_texto
import html_elem_link_img

def gera(vid, mostra_autor):

  atrs = obj_video.obtem_atributos(vid) if vid != None else None

  itens_resumo = []

  colunas = [ 'thumb','video', 'autor', 'data', 'duracao', 'largura', 'altura', 'titulo' ]
  
  destaque = False
  for chave in colunas:
    if chave == 'video':
      mostra = True
      texto = obj_video.obtem_identificador(vid) if vid != None else "Vídeo"
    elif chave == 'autor':
      mostra = mostra_autor
      texto = obj_usuario.obtem_identificador(atrs['autor']) if vid != None else "Autor"
    elif chave == 'duracao':
      mostra = True
      texto = f"{atrs[chave]/1000:.3f} s" if vid != None else "Duração"
    elif chave == 'altura' or chave == 'largura':
      mostra = True
      texto = f"{str(atrs[chave])} px" if vid != None else chave.capitalize()
    elif chave == 'thumb':

      mostra=True
      texto = html_elem_link_img.gera(atrs[chave],None,40,None)

    else:
      mostra = True
      texto = atrs[chave] if vid != None else chave.capitalize()
      
    if mostra:
      cab = (vid == None)
      cor_fundo = None
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha)
      itens_resumo.append(ht_item)

  if vid != None:
    bt_args = { 'video': obj_video.obtem_identificador(vid) }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_video", bt_args, "#ffcc88")
    itens_resumo.append("<td>" + bt_ver + "</td>")

  return itens_resumo
