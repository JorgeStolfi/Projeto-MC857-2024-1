import html_elem_video
import html_pag_ver_video
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  # Obtém o vídeo {vid}:
  vid_id = cmd_args.pop('video', None)
  if vid_id == None:
    erros.append("O identificador do vídeo não foi especificado")
    vid = None
  else:
    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"O vídeo \"{vid_id}\" não existe")
      
  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""
  
  if len(erros) == 0:
    assert vid !=None
    obj_video.muda_atributos(vid, { 'vistas': obj_video.obtem_atributo(vid, 'vistas') + 1 })
    pag = html_pag_ver_video.gera(ses, vid, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
