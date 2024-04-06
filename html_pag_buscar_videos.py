import html_pag_buscar_videos_IMP


def gera(ses, atrs, admin, erros):
  """ Retorna uma página contendo o formulário para buscar videos.
  Normalmente é usada por administradores. Os campos do formulário são 
  um subconjuto dos atributos de um objeto da classe {Class}.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos.  Por exemplo, se uma 
  busca dá erro, o sistema deve re-apresentar a página de busca
  com os valores já preenchidos.
  
  A página terá um botão de tipo 'submit' com texto "Buscar" que,
  quando acionado, emite uma ação POST com comando 'buscar_trechos. 
  Haverá também um botão simples com texto "Cancelar" que emite
  o comando 'pag_principal'."""
  return html_pag_buscar_videos_IMP.gera(ses, atrs, admin, erros)
