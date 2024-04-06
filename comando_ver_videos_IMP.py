import html_bloco_lista_de_videos
import html_pag_generica
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  usr_ses = obj_sessao.obtem_usuario(ses)
  id_usr_ses = obj_usuario.obtem_identificador(usr_ses)
  assert usr_ses != None
  if 'id_usuario' in cmd_args:
    # Alguém quer ver videos de usuário específico:
    id_usr = cmd_args['id_usuario']
    assert (id_usr == id_usr_ses) or obj_sessao.eh_administrador(ses) # Deveria ser o caso.
  else:
    # Usuário da sessão {ses} quer ver os próprios videos:
    usr = usr_ses
    id_usr = id_usr_ses

  # Com o identificador do usuário, podemos buscar seus videos no banco:
  lista_ids_videos = obj_video.busca_por_campo('usr', id_usr)
  ht_conteudo = html_bloco_lista_de_videos.gera(lista_ids_videos)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag