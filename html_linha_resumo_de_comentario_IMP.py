import obj_comentario
import obj_usuario
import obj_video
import html_elem_item_de_resumo
import sys
import html_elem_button_simples

def gera(com, mostra_autor, mostra_video, mostra_pai):
  
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  atrs = obj_comentario.obtem_atributos(com) if com != None else None

  itens_resumo = []
  
  colunas = [ 'comentario', 'video', 'autor',  'pai', 'data',  'texto' ]
  for chave in colunas:
    if chave == 'comentario':
     mostra = True
     texto = com_id if com != None else "Comentário"
    elif chave == 'video':
      mostra = mostra_video
      texto = obj_video.obtem_identificador(atrs['video']) if com != None else "Vídeo"
    elif chave == 'pai':
      mostra = mostra_pai
      if com == None:
        texto = "Pai"
      else:
        pai = atrs['pai'] if 'pai' in atrs else None
        texto = obj_comentario.obtem_identificador(pai) if pai != None else " "
    elif chave == 'autor':
      mostra = mostra_autor;
      texto = obj_usuario.obtem_identificador(atrs['autor']) if com != None else "Autor"
    else:
      mostra = True
      texto = (str(atrs[chave]) if com != None else chave.capitalize()).replace("\n", "\\n")[:50]
      
    if mostra:
      cab = (com == None)
      cor_fundo = None
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo,alinha)
      itens_resumo.append(ht_item)
  
  if com != None:
    bt_args = { 'comentario': com_id }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_comentario", bt_args, None)
    itens_resumo.append("<td>" + bt_ver + "</td>")

  return itens_resumo
