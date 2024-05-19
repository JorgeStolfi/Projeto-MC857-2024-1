import obj_comentario
import obj_usuario
import obj_video
import html_elem_item_de_resumo
import sys
import html_elem_button_simples
import html_elem_link_text

def gera(com, mostra_autor, mostra_video, mostra_pai, mostra_nota):
  
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  atrs = obj_comentario.obtem_atributos(com) if com != None else None

  itens_resumo = []
  
  colunas = [ 'comentario', 'video', 'autor',  'pai', 'data',  'texto', 'nota', 'voto' ]
  for chave in colunas:
    if chave == 'comentario':
     mostra = True
     texto = html_elem_link_text.gera(com_id, "ver_comentario", { 'comentario': com_id }) if com != None else "Comentário"
    elif chave == 'video':
      mostra = mostra_video
      texto = html_elem_link_text.gera(obj_video.obtem_identificador(atrs['video']), "ver_video", { 'video': obj_video.obtem_identificador(atrs['video']) }) if com != None else "Vídeo"
    elif chave == 'pai':
      mostra = mostra_pai
      if com == None:
        texto = "Pai"
      else:
        pai = atrs['pai'] if 'pai' in atrs else None
        texto = html_elem_link_text.gera(obj_comentario.obtem_identificador(pai), "ver_comentario", { 'comentario': obj_comentario.obtem_identificador(pai) }) if pai != None else " "
    elif chave == 'autor':
      mostra = mostra_autor;
      texto = html_elem_link_text.gera(obj_usuario.obtem_identificador(atrs['autor']), "ver_usuario", { 'usuario': obj_usuario.obtem_identificador(atrs['autor']) }) if com != None else "Autor"
    elif chave == 'nota':
      mostra = mostra_nota;
      texto = obj_usuario.obtem_identificador(atrs['nota']) if com != None else "nota"
    elif chave == 'voto':
      mostra = True
      texto = str(atrs['voto']) if com != None else 'Voto'
    elif chave == 'texto':
      mostra = True
      if atrs["bloqueado"] == True:
        texto = "[BLOQUEADO]"
      else:
        texto = (str(atrs[chave]) if com != None else chave.capitalize()).replace("\n", "\\n")[:50]
    else:
      mostra = True
      texto = (str(atrs[chave]) if com != None else chave.capitalize()).replace("\n", "\\n")[:50]
      
    if mostra:
      cab = (com == None)
      cor_fundo = None
      alinha = "left"
      if atrs["bloqueado"] == True:
        ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo,alinha, "#FF0000")
      else:
        ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo,alinha)
      itens_resumo.append(ht_item)
  
  if com != None:
    bt_args = { 'comentario': com_id }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_comentario", bt_args, None)
    itens_resumo.append("<td>" + bt_ver + "</td>")

  return itens_resumo
