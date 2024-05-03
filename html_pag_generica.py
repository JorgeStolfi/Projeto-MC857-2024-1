import html_pag_generica_IMP

def gera(ses, ht_conteudo, erros):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto,
  o {ht_conteudo} dado (um {string} em formato HTML5), e as mensagens {erros}.
  
  O parâmetro {erros} pode ser {None}, um string com várias mensagens de erro/aviso
  separadas por "\n", ou uma lista de strings."""
  return html_pag_generica_IMP.gera(ses, ht_conteudo, erros)
