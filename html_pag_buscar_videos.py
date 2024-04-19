import html_pag_buscar_videos_IMP


def gera(ses, atrs, erros):
  """ Retorna uma página contendo o formulário para buscar videos.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais de alguns campos.
  
  Se {erros} não é {None}, deve ser uma lista de strings,
  cada uma delas sendo uma mensagem a mostrar na página.
  
  A página terá um botão de tipo 'submit' com texto "Buscar" que,
  quando acionado, emite uma ação POST com comando 'buscar_videos. 
  Haverá também um botão simples com texto "Cancelar" que emite
  o comando 'pag_principal'.
  
  Os argumentos {atrs} e {erros} destinam-se a tratar o caso em que uma 
  busca dá erro ou não retorna nenhum vídeo. Nesse caso 
  o sistema deve re-apresentar a página de busca
  com as mensagens de erro e os valores preenchidos anteriormente."""
  return html_pag_buscar_videos_IMP.gera(ses, atrs, erros)
