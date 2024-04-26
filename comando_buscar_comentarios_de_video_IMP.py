
import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import html_pag_mensagem_de_erro
import obj_comentario
import obj_sessao
import obj_video

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão do comando inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  assert 'video' in cmd_args, "Vídeo não especificado"

  erros = [].copy()
  
  # Obtém o vídeo {vid} em questão e seu identificador {id_vid}:
  id_vid = cmd_args['video']
  vid = obj_video.busca_por_identificador(id_vid)
  
  if vid == None:
    erros.append(f"Vídeo {id_vid} não existe")
    ht_bloco = None
  else:
    lista_ids_com = obj_comentario.busca_por_video(id_vid)
    if len(lista_ids_com) == 0:
      # Não encontrou nada.
      erros.append(f"Vídeo {id_vid} não tem nenhum comentário")
      ht_bloco = None
    else:
      ht_titulo = html_bloco_titulo.gera(f"Comentários do video {id_vid}")
      mostra_autor = True  # Podem ter autores diferentes.
      mostra_video = False # São todos do mesmo vídeo.
      mostra_pai = True    # Podem ter pais diferentes.
      ht_tabela = html_bloco_lista_de_comentarios.gera(lista_ids_com, mostra_autor, mostra_video, mostra_pai)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
