import html_pag_ver_conversa_IMP

def gera(ses, titulo, conversa, erros):
  """
  Retorna uma página HTML que mostra uma conversa, que é uma árvore de 
  comentários e respostas.  
  
  O parâmetro {ses} deve ser um objeto da classe {obj_sessao.Classe}
  que representa a sessão corrente.
  
  O parâmetro {conversa} deve ser uma floresta de comentários,
  como devolvida por {obj_comentario.obtem_conversa}
  
  O resultado da função é uma página que mostra todos os comentários 
  cujos identificadores aparecem na {conversa}, cada qual indentado 
  de acordo com a profundidade na mesma.
  """
  return html_pag_ver_conversa_IMP.gera(ses, titulo, conversa, erros)
