import html_linha_resumo_de_sessao_IMP

def gera(ses, bt_ver, bt_fechar):
  """Retorna uma lista de fragmentos HTML que descreve dados principais de uma
  sessão: identificador da sessão, usuário dono da sessão, um booleano
  indicando se a sessão está aberta ou não, o cookie da sessão
  a data de criação da sessão, e opcionalmente botões para atuar na sessão
  como especificado por {bt_ver} e {bt_fechar}

  O resultado é uma tupla com fragmentos separados para cada um desses
  campos, que pode ser usada como uma linha do argumento de {html_elem_table.gera}.

  Se {bt_ver} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Ver". Quando clicado, esse botão emitirá o comando
  HTTP "ver_sessao" com o identificador da sessão como argumento 
  com chave 'sessao'.

  Se {bt_fechar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Fechar". Quando clicado, esse botão emitirá o comando
  HTTP "fechar_sessao" com o identificador da sessão como argumento com chave
  'sessao'."""
  return html_linha_resumo_de_sessao_IMP.gera(ses, bt_ver, bt_fechar)
