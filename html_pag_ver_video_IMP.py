import html_bloco_titulo
import html_bloco_video
import html_pag_generica
import obj_sessao
import obj_video

def gera(ses, vid, erros):

  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert vid != None and isinstance(vid, obj_video.Classe)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)

  vid_id = obj_video.obtem_identificador(vid)
  vid_atrs = obj_video.obtem_atributos(vid)
  
  # Título da página:
  if(vid_atrs['bloqueado']):
    tit = "[BLOQUEADO]"
  else:
    tit = f"Vídeo {vid_id}: {vid_atrs['titulo']}"
  ht_titulo = html_bloco_titulo.gera(tit)
  
  # Determina botões a mostar:
  ses_dono = obj_sessao.obtem_dono(ses) if ses != None else None
  vid_autor = obj_video.obtem_autor(vid)
  assert vid_autor != None
  para_admin = ses != None and obj_sessao.de_administrador(ses)
  para_autor = ses != None and ( ses_dono == vid_autor )
  
  bt_alterar = para_admin or para_autor
  bt_conversa = True
  bt_comentar = ses != None
  bt_calcnota = para_admin or para_autor
  ht_bloco_vid = html_bloco_video.gera(vid, bt_alterar, bt_conversa, bt_comentar, bt_calcnota)
  
  ht_conteudo = \
    ht_titulo + "\n" + \
    ht_bloco_vid

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
