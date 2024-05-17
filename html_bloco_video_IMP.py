import obj_usuario
import obj_video
import html_elem_button_simples
import html_elem_video
import html_bloco_cabecalho_de_video
import html_bloco_rodape_de_video

def gera(vid, bt_alterar, bt_conversa, bt_comentar):

  # Validação de tipos (paranóia):
  assert vid != None and isinstance(vid, obj_video.Classe)
  assert isinstance(bt_alterar, bool)
  assert isinstance(bt_conversa, bool)
  assert isinstance(bt_comentar, bool)

  vid_id = obj_video.obtem_identificador(vid)
  vid_atrs = obj_video.obtem_atributos(vid)
  
  ht_cabeca = html_bloco_cabecalho_de_video.gera \
    ( vid_id, vid_atrs, largura = 600, 
      mostra_id = False, mostra_data = True
    )
    
  # Janela do vídeo:
  if(not vid_atrs['bloqueado']):
    ht_video = html_elem_video.gera(vid_id, altura = 300)
  else:
    ht_video = ""
  
  ht_rodape = html_bloco_rodape_de_video.gera \
    ( vid_id, vid_atrs, largura = 600,
      mostra_nota = True, mostra_dims = True
    )

  ht_bloco = \
    ht_cabeca + "\n" + \
    ht_video + "\n" + \
    ht_rodape
  
  # Acrescenta botões para ver outras coisas do vídeo, se for o caso:
  if(not vid_atrs['bloqueado']):
    cmd_args = { 'video': vid_id }
    if bt_alterar or bt_conversa or bt_comentar:
      ht_bloco += "<br/>" 
    
    if bt_alterar:
      ht_bt_alterar = html_elem_button_simples.gera(f"Alterar", "solicitar_pag_alterar_video", cmd_args, '#eeee55')
      ht_bloco += ht_bt_alterar

    if bt_conversa:
      ht_bt_conversa = html_elem_button_simples.gera(f"Ver comentarios", "ver_conversa", cmd_args, '#eeee55')
      ht_bloco += ht_bt_conversa
    
    if bt_comentar:
      ht_bt_comentar = html_elem_button_simples.gera("Comentar", "solicitar_pag_postar_comentario", cmd_args, '#55ee55')
      ht_bloco += ht_bt_comentar
 
  return ht_bloco
