import html_bloco_conversa_IMP

def gera(conversa, ses_dono):
  """
  Retorna um fragmento HTML que exibe os comentários cujos
  identificadores aparecem na {conversa} dada.
  
  O parâmetro {conversa} deve ser uma floresta de comentários representada
  por listas encaixadas, como devolvida por {obj_comentario.obtem_conversa}.
  
  O parâmetro {ses_dono} deve ser o dono da sessão de login que pediu
  estes dados; ou {None} se o usuário que pediu não está logado.
  Este parâmetro afeta os campos e 
  
  O resultado desta função será um texto HTML consistindo
  de instâncias de {html_bloco_comentario.gera},
  uma para cada comentário na {conversa}, indentados segundo sua
  profundidade na mesma.
  """
  return html_bloco_conversa_IMP.gera(conversa, ses_dono)

