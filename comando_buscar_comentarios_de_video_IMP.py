
import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import html_pag_mensagem_de_erro
import obj_comentario
import obj_sessao
import obj_video
import obj_usuario

def processa(ses, cmd_args):
  
  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict

  ses_dono = obj_sessao.obtem_dono(ses); 
  para_admin = obj_usuario.eh_administrador(ses_dono)

  erros = []
  
  # Obtém o vídeo {vid} em questão e seu identificador {vid_id}:
  vid_id = cmd_args.pop('video', None)
  if vid_id != None:
    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"O vídeo \"{vid_id}\" não existe")
  else:
    erros.append("O vídeo a buscar não foi especificado")
    vid = None
  
  ht_bloco = None
  if len(erros) == 0:
    assert vid != None
    com_ids = obj_comentario.busca_por_video(vid_id, sem_pai = True)
    if len(com_ids) == 0:
      erros.append(f"O vídeo {vid_id} não tem nenhum comentário")
    else:
      ht_titulo = html_bloco_titulo.gera(f"Comentários do video {vid_id}")
      ht_tabela = html_bloco_lista_de_comentarios.gera \
        ( com_ids, 
          mostra_autor = True,  # Podem ter autores diferentes.
          mostra_video = False, # São todos do mesmo vídeo.
          mostra_pai = True,    # Podem ter pais diferentes.
          mostra_nota = True,   # Porque não mostraria?
          forcar_mostrar_texto = para_admin # Apenas admins forçam a visualização do texto
        )
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
