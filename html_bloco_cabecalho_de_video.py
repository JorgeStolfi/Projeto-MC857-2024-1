import html_bloco_cabecalho_de_video_IMP

def gera(vid_id, atrs, largura, mostra_id, mostra_data):
  """
  Retorna um fragmento HTML que exibe alguns atributos imutáveis de um
  vídeo {vid} cujo identificador é {vid_id}: especificamente, identificador,
  data de upload, e autor. Este cabecalho serve para
  inserir o alto dos blocos {html_bloco_comentario} e
  {html_form_alterar_comentario}
 
  O parâmetro {vid_id} deve ser {None} ou um identificador de comentário
  (um string da forma "C-{NNNNNNNN}")
  
  O parâmetro {atrs} deve ser {None} ou um dicionário que define todos
  ou um subconjunto dos atributos de um vídeo (vide {obj_video.Classe}).
  Os valores dos atributos exibidos serão obtidos de {atrs}, ignorando
  seus os valoras atuais no vídeo {vid}. Atributos que estão ausentes ou
  tem valor nulo em {atrs} não serão exibidos. Atributos cujo valor
  deveria ser um objeto (como 'autor') podem estar representados em
  {atrs} pelos seus identificadores.
 
  O parâmetro inteiro {largura} especifica a largura do cabeçalho, em pixels
  
  Os parâmetros booleanos {mostra_id} e {mostra_data}
  especificam se devem ser exibidos o identificador do vídeo e o
  atributo 'data' que constarem do dicionário {atrs}, respectivamente.
  """
  return html_bloco_cabecalho_de_video_IMP.gera(vid_id, atrs, largura, mostra_id, mostra_data)

