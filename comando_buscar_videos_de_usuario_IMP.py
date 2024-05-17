import html_bloco_lista_de_videos
import html_pag_generica
import html_pag_mensagem_de_erro
import html_bloco_titulo
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict
 
  erros = []
  
  mostra_autor = False; # Deve mostar o autor de cada vídeo?
  
  # Obtem o usuário {ses_dono} dono da sessão:
  if ses != None and obj_sessao.aberta(ses):
    ses_dono = obj_sessao.obtem_dono(ses); 
    assert ses_dono != None
    ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
    para_admin = obj_usuario.eh_administrador(ses_dono)
  else:
    ses_dono = None
    ses_dono_id = None
    para_admin = None

  # Obtém o usuário {autor} a listar e seu identificador {autor_id}:
  if 'usuario' in cmd_args:
    # Alguém quer ver videos de usuário específico:
    autor_id = cmd_args['usuario']
    autor = obj_usuario.obtem_objeto(autor_id)
    autor = obj_usuario.obtem_identificador(autor)
  else:
    # Usuário da sessão {ses} quer ver os próprios videos:
    autor = ses_dono
    autor_id = ses_dono_id
  
  if autor == None:
    erros.append(f"O usuario não foi especificado")
    ht_bloco = None
  else:
    videos_ids = obj_video.busca_por_autor(autor_id)
    if len(videos_ids) == 0:
      # Argumentos com erro ou não encontrou nada.
      erros.append(f"O usuário \"{autor_id}\"não tem nenhum vídeo")
      ht_bloco = None
    else:
      # Encontrou pelo menos um vídeo.  Mostra em forma de tabela:
      if autor == ses_dono:
        ht_titulo = html_bloco_titulo.gera("Meus vídeos")
      else:
        ht_titulo = html_bloco_titulo.gera(f"Vídeos de {autor_id}")
      
      ht_tabela = html_bloco_lista_de_videos.gera(videos_ids, mostra_autor)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
