import obj_usuario
import obj_video
import html_elem_button_simples
import html_elem_video
import html_bloco_cabecalho_de_video
import html_bloco_rodape_de_video
import html_elem_img
import html_elem_table

def gera(vid, bt_alterar, bt_conversa, bt_comentar, bt_calcnota):

  # Validação de tipos (paranóia):
  assert vid != None and isinstance(vid, obj_video.Classe)
  assert isinstance(bt_alterar, bool)
  assert isinstance(bt_conversa, bool)
  assert isinstance(bt_comentar, bool)
  assert isinstance(bt_calcnota, bool)

  vid_id = obj_video.obtem_identificador(vid)
  vid_atrs = obj_video.obtem_atributos(vid)
  
  ht_cabeca = html_bloco_cabecalho_de_video.gera(vid_id, vid_atrs, largura=600, mostra_id=False, mostra_data=True)
  
  # Janela do vídeo:
  if(not vid_atrs['bloqueado']):
    ht_video = html_elem_video.gera(vid_id, altura = 300)
  else:
    ht_video = ""
  
  ht_rodape = html_bloco_rodape_de_video.gera(vid_id, vid_atrs, largura=600, mostra_nota=True, mostra_dims=True)

  ht_bloco = ht_cabeca + "\n" + ht_video + "\n" + ht_rodape + "\n"

  # Acrescenta quadros
  alt_px = 32
  ht_elems_quadros = []

  NQ = 6 # Por enquanto.  Tem que casar com {obv_video.cria}.
  for iq in range(NQ):
    arquivo = f"quadros/{vid_id}-{iq:03d}.png"
    ht_img = html_elem_img.gera(arquivo, f"{iq:03d}", alt_px)
    ht_elem_quadro = "<td style=\"text-align: center; border: 1px solid blue; padding:5px;\">&nbsp;" + ht_img + "&nbsp;</td>"
    ht_elems_quadros.append(ht_elem_quadro)
  
  ht_tabela_quadros = html_elem_table.gera([ ht_elems_quadros ], None)

  ht_bloco += ht_tabela_quadros + "\n"
  
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
 
    if bt_calcnota:
      ht_bt_calcnota = html_elem_button_simples.gera("Recalcular nota", "recalcular_nota", cmd_args, '#ff5555')
      ht_bloco += ht_bt_calcnota
      
  return ht_bloco
