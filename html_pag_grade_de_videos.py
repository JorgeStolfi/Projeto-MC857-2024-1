import html_pag_grade_de_videos_IMP

def gera(ses, vid_ids, ncols, erros):
  """Retorna uma página HTML que mostra um conjunto de vídeos na forma de
  uma grade de thumbnails. Quando o mouse paira sobre cada thumbnail,
  aparece um popup com o título do vídeo e possivelmente outros dados.
  Clicando no thumbnail de um vídeo gera um comando "ver_video" para o mesmo.
  
  O parâmetro {ses} deve ser a sessão de login que pediu a página
  (on objeto de tipo {obj_sessao.Classe}, aberto) ou {None} se 
  quem pediu não está logado.
  
  O parâmetro {vid_ids} deve ser uma lista de identificadores de videos
  (strings da forma "V-{NNNNNNNN}".
  
  O parâmetro inteiro {ncols} especifica o número de colunas da grade.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens 
  de aviso ou erro a serem mostradas no alto da página.
  """
  return html_pag_grade_de_videos_IMP.gera(ses, vid_ids, ncols, erros)
