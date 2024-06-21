import html_pag_grade_de_videos_IMP

def gera(ses, vid_ids, ncols, catalogo, erros):
  """Retorna uma página HTML que mostra os vídeos {vid_ids} na forma de
  uma grade com as imagens de capa dos mesmos. Quando o mouse paira sobre cada
  imagem, aparece um popup com o título do vídeo e possivelmente outros dados.
  Clicando na capa de um vídeo gera um comando "ver_video" para o mesmo.
  
  O parâmetro {ses} deve ser a sessão de login que pediu a página
  (on objeto de tipo {obj_sessao.Classe}, aberto) ou {None} se 
  quem pediu não está logado.
  
  O parâmetro {vid_ids} deve ser uma lista de identificadores de videos
  (strings da forma "V-{NNNNNNNN}".
  
  O parâmetro inteiro {ncols} especifica o número de colunas da grade.
  
  O parametro booleano {catalogo} especifica se e pra exibir a pagina de
  catalogo de video ou a pagina de grade de video. Se True, exibe a pagina de 
  catalogo de video.

  O parâmetro {erros} deve ser {None} ou uma lista de mensagens 
  de aviso ou erro a serem mostradas no alto da página.
  """
  return html_pag_grade_de_videos_IMP.gera(ses, vid_ids, ncols, catalogo, erros)
