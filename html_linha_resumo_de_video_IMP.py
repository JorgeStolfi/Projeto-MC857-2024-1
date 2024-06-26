import obj_video
import obj_usuario
import html_elem_item_de_resumo
import html_elem_span
import html_elem_button_simples
import html_estilo_texto
import html_elem_link_img
import html_elem_link_text
import util_bloqueado
import util_nota
import util_testes
import obj_sessao

#def gera(vid, mostra_autor):#Original
def gera(vid, mostra_autor, para_admin):#Alterado

  vid_id = obj_video.obtem_identificador(vid) if vid != None else None
  atrs = obj_video.obtem_atributos(vid) if vid != None else None

  itens_resumo = []

  colunas = [ 'capa','video', 'autor', 'nota', 'vistas', 'data', 'duracao', 'tamanho', 'titulo', 'bloqueado']

  cor_fundo = None
  cor_texto = None
  alinha = "left"
  cab = (vid == None)
  for chave in colunas:
    if chave == 'video':
      mostra = True
      texto = "Vídeo" if cab else html_elem_link_text.gera(vid_id, "ver_video", { 'video': vid_id })
    elif chave == 'titulo':
      mostra = True
      alinha = "left"
      if cab:
        texto = "Título"
      else:
        if(atrs['bloqueado']):
          texto = "[BLOQUEADO]"
          cor_fundo = "#FF2222"
        else:
          texto = util_testes.trunca_valor(str(atrs['titulo']), 15, None)
    elif chave == 'autor':
      mostra = mostra_autor
      if cab:
        texto = "Autor"
      else:
        autor_id = obj_usuario.obtem_identificador(atrs['autor'])
        texto = html_elem_link_text.gera(autor_id, "ver_usuario", { 'usuario': autor_id })
    elif chave == 'duracao':
      mostra = True
      texto = "Duração" if cab else f"{atrs[chave]/1000:.3f} s"
      alinha = "right"
    elif chave == 'tamanho':
      mostra = True
      texto = chave.capitalize() if cab else f"{str(atrs['largura'])}x{str(atrs['altura'])} px"
      alinha = "right"
    elif chave == 'nota':
      mostra = True
      if cab:
        texto = "Nota"
      else:
        texto = util_nota.formata(atrs['nota'])
    elif chave == 'capa':
      mostra=True
      if cab:
        texto = "Capa"
      else:
        arq_capa = f"capas/{vid_id}.png"
        texto = html_elem_link_img.gera(arq_capa, None, 40, None)
    elif chave == 'bloqueado':
      mostra = True
      if cab:
        texto = "🔒"
      ##else:
        ##texto = util_bloqueado.formata(atrs['bloqueado'])
      else:
        if atrs['bloqueado']:
          texto = "🔒"
          cor_fundo = "#FFFF55"
        else:
          texto = ""
    else:
      mostra = True
      texto = chave.capitalize() if cab else str(atrs[chave])
      
    if mostra:
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha, cor_texto)
      itens_resumo.append(ht_item)

  if vid != None:
    bt_args = { 'video': obj_video.obtem_identificador(vid) }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_video", bt_args, None)
    itens_resumo.append("<td>" + bt_ver + "</td>")

    # Se o usuário é administrador, adicionar botões Bloquear/Desbloquear
    objeto_usr = obj_usuario.obtem_objeto(autor_id)
    #para_admin = obj_usuario.eh_administrador(objeto_usr)#Original
    if para_admin:
      bt_bloq_args = { 'video': vid_id, 'bloqueado': str(not atrs['bloqueado']) }
    
      if atrs['bloqueado']:
        bt_bloq_texto = 'Desbloquear'
        bt_bloq_cor = '#11dd11'
      else:
        bt_bloq_texto = 'Bloquear'
        bt_bloq_cor = '#fb1528'

      ht_bt_bloquear = html_elem_button_simples.gera(bt_bloq_texto, "buscar_videos", bt_bloq_args, bt_bloq_cor)
      itens_resumo.append("<td>" + ht_bt_bloquear + "</td>") 

  return itens_resumo
