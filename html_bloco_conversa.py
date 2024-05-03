import html_bloco_conversa_IMP

def gera(conversa):
  """
  Retorna um fragmento HTML que exibe os comentários cujos
  identificadores aparecem na {conversa} dada.
  
  O parâmetro {conversa} deve ser uma floresta de comentários representada
  por listas encaixadas, como devolvida por {obj_comentario.obtem_conversa}.
  
  O resultado desta função será um texto HTML consistindo
  de instâncias de {html_bloco_dados_de_comentario.gera},
  uma para cada comentário na {conversa}, indentados segundo sua
  profundidade na mesma.
  """
  return html_bloco_conversa_IMP.gera(conversa)

