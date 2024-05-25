import obj_comentario
import obj_usuario
import obj_video
import html_elem_item_de_resumo
import html_elem_button_simples
import html_elem_link_text
import util_nota
import util_voto

import sys

def gera(com, mostra_autor, mostra_video, mostra_pai, mostra_nota, forcar_mostrar_texto):
  
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  atrs = obj_comentario.obtem_atributos(com) if com != None else None

  itens_resumo = []
  
  colunas = [ 'comentario', 'data', 'nota', 'autor',  'video', 'pai', 'voto', 'texto' ]

  cor_fundo = None
  cor_texto = None
  alinha = "left"
  cab = (com == None)
  for chave in colunas:
    if chave == 'comentario':
     mostra = True
     texto = "Comentário" if cab else html_elem_link_text.gera(com_id, "ver_comentario", { 'comentario': com_id })
    elif chave == 'video':
      mostra = mostra_video
      if cab:
        texto = "Vídeo"
      else:
        vid = atrs['video']
        assert vid != None
        vid_id = obj_video.obtem_identificador(vid)
        texto = html_elem_link_text.gera(vid_id, "ver_video", { 'video': vid_id })
    elif chave == 'pai':
      mostra = mostra_pai
      if cab:
        texto = "Pai"
      else:
        pai = atrs['pai'] if 'pai' in atrs else None
        if pai == None:
          texto = ""
        else:
          pai_id = obj_comentario.obtem_identificador(pai)
          texto = html_elem_link_text.gera(pai_id, "ver_comentario", { 'comentario': pai_id })
    elif chave == 'autor':
      mostra = mostra_autor;
      if cab:
        texto = "Autor"
      else:
        autor = atrs['autor']
        assert autor != None
        autor_id = obj_usuario.obtem_identificador(autor)
        texto = html_elem_link_text.gera(autor_id, "ver_usuario", { 'usuario': autor_id })
    elif chave == 'nota':
      mostra = mostra_nota;
      texto = "Nota" if cab else util_nota.formata(atrs['nota'])
    elif chave == 'voto':
      mostra = True
      texto = "Voto" if cab else util_voto.formata(atrs['voto'])
    elif chave == 'texto':
      mostra = True
      if cab:
        texto = "Texto"
      elif atrs["bloqueado"] and not forcar_mostrar_texto:
        texto = "[BLOQUEADO]"
        cor_fundo = "#FFFF55"
      else:
        texto = ((str(atrs[chave])).replace("\n", "\\n"))[:50]
    else:
      mostra = True
      if cab:
        texto = chave.capitalize()
      else:
        val = atrs[chave]
        texto = (str(val).replace("\n", "\\n"))[:50]
      
    if mostra:
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha, cor_texto)
      itens_resumo.append(ht_item)
  
  if not cab:
    bt_args = { 'comentario': com_id }
    ht_bt_ver = html_elem_button_simples.gera("Ver", "ver_comentario", bt_args, None)
    itens_resumo.append("<td>" + ht_bt_ver + "</td>")

  return itens_resumo
