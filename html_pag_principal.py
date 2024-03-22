import html_pag_principal_IMP

# Nas funções abaixo,.
#
# Nas funções abaixo, o parâmetro {erros} é uma lista de mensagens de erro
# que serão mostradas no alto da página devolvida.  Se for um string, ele é
# dividido em mensagens separadas nas quebtas de linha '\n'.
# Se for {None}. ou uma cadeia ou lista vazia, supõe que não há mensagens.

def gera(ses, erros):
  """Retorna a página de entrada da loja (homepage).
  O parâmetro {ses} é um objeto da classe {obj_sessao.Classe} que 
  representa a sessão de login corrente; ou {None} se o usuário
  nao está logado"""
  return html_pag_principal_IMP.gera(ses, erros)
