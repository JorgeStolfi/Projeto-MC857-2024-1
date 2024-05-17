import html_bloco_rodape_de_video_IMP

def gera(vid_id, atrs, largura, mostra_nota, mostra_dims):
  """
  Retorna um fragmento HTML que exibe alguns atributos imutáveis
  de um vídeo {vid} cujo identificador é {vid_id}: especificamente,
  'nota', e dimensões ('duracao', 'altura', e 'largura').
 
  O parâmetro {vid_id} deve ser {None} ou um identificador de comentário
  (um string da forma "C-{NNNNNNNN}")
  
  O parâmetro {atrs} deve ser {None} ou um dicionário que define todos
  ou um subconjunto dos atributos de um comentário (vide
  {obj_video.Classe}). Os valores dos atributos exibidos serão obtidos
  de {atrs}, ignorando seus os valoras atuais no vídeo {vid}. Atributos
  que estão ausentes ou tem valor nulo em {atrs} não serão exibidos.
 
  O parâmetro inteiro {largura} especifica a largura do cabeçalho, em pixels
  
  Os parâmetros booleanos {mostra_nota} e {mostra_dims}
  especificam se devem ser exibidos o atributo 'nota' e as dimensões
  que constarem do dicionário {atrs}, respectivamente.
  """
  return html_bloco_rodape_de_video_IMP.gera(vid_id, atrs, largura, mostra_nota, mostra_dims)

