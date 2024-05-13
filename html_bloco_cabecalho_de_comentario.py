import html_bloco_cabecalho_de_comentario_IMP

def gera(com_id, atrs, largura, mostra_id, mostra_data, mostra_video, mostra_pai):
  """
  Retorna um fragmento HTML que exibe os atributos inutáveis
  (identificador, data, autor, vídeo, etc.) de um comentário {com} cujo
  identificador é {com_vid}.
 
  O parâmetro {com_id} deve ser {None} ou um identificador de comentário
  (um string da forma "C-{NNNNNNNN}")
  
  O parâmetro {atrs} deve ser {None} ou um dicionário que define todos
  ou um subconjunto dos atributos de um comentário (vide
  {obj_comentario.Classe}). Os valores dos atributos exibidos serão
  obtidos de {atrs}, ignorando seus os valoras atuais no comentário
  {com}. Atributos que estão ausentes ou tem valor nulo em {atrs} não
  serão exibidos.  Atributos cujo valor deveria ser um objeto 
  podem estar representados em {atrs} pelos seus identificadores.
 
  O parâmetro inteiro {largura} especifica a largura do cabeçalho, em pixels
  
  Os parâmetros booleanos {mostra_id}, {mostra_data}, {mostra_video} e
  {mostra_pai} especificam se devem ser exibidos o identificador e os
  atributos 'data', 'video' e 'pai' do dicionário {atrs},
  respectivamente.
  """
  return html_bloco_cabecalho_de_comentario_IMP.gera(com_id, atrs, largura, mostra_id, mostra_data, mostra_video, mostra_pai)

