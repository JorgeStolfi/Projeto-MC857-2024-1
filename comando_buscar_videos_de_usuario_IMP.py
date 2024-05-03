import html_bloco_lista_de_videos
import html_pag_generica
import html_pag_mensagem_de_erro
import html_bloco_titulo
import obj_sessao
import obj_usuario
import obj_video

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão do comando inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
 
  erros = [].copy()
  
  mostra_autor = False; # Deve mostar o autor de cada vídeo?
  
  # Obtem o usuário {usr_ses} dono da sessão:
  usr_ses = obj_sessao.obtem_usuario(ses); assert usr_ses != None
  id_usr_ses = obj_usuario.obtem_identificador(usr_ses)

  # Obtém o usuário {autor} a listar e seu identificador {id_autor}:
  if 'usuario' in cmd_args:
    # Alguém quer ver videos de usuário específico:
    id_autor = cmd_args['usuario']
    autor = obj_usuario.obtem_objeto(id_autor)
    autor = obj_usuario.obtem_identificador(autor)
  else:
    # Usuário da sessão {ses} quer ver os próprios videos:
    autor = usr_ses
    id_autor = id_usr_ses
  
  if autor == None:
    erros.append(f"Usuario indeterminado")
    ht_bloco = None
  else:
    lista_ids_videos = obj_video.busca_por_autor(id_autor)
    if len(lista_ids_videos) == 0:
      # Argumentos com erro ou não encontrou nada.
      erros.append("Usuário não tem nenhum vídeo")
      ht_bloco = None
    else:
      # Encontrou pelo menos um vídeo.  Mostra em forma de tabela:
      if autor == usr_ses:
        ht_titulo = html_bloco_titulo.gera("Meus vídeos")
      else:
        ht_titulo = html_bloco_titulo.gera(f"Vídeos de {id_autor}")
      
      ht_tabela = html_bloco_lista_de_videos.gera(lista_ids_videos, mostra_autor)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
