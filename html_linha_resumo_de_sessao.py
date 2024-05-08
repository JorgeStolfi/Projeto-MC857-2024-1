import html_linha_resumo_de_sessao_IMP

def gera(ses, bt_ver, bt_fechar, mostrar_usr):
  """
  Retorna uma lista de fragmentos HTML com os valores dos principais
  atributos do objeto {ses} da classe {obj_sessao.Classe}, incluindo o
  identificador {ses_id}. Esta função serve para gerar os elementos de
  uma linha da tabela produzida por {html_bloco_lista_de_sessoes.gera}.
  
  Se {ses} for {None}, o resultado é uma lista com os cabeçalhos das
  colunas da tabela ("Sessão", "Usuário", etc.), em vez dos valores
  dos atributos.
  
  Cada elemento do resultado estará formatado com um estilo adequado.
  Veja {html_elem_item_de_resumo.gera}.
  
  Se o booleano {bt_ver} é {True}, resultado inclui também um botão
  "Ver" que dispara um comando HTTP "ver_sessao". Se o booleano
  {bt_fechar} é {True}, o resultado inclui também um botão "Fechar" que
  dispara um comando HTTP "fechar_sessao". O argumento desses comandos
  será {{ 'sessao': ses_id }}. Estes botões não aparecem se {ses} é
  {None} (linha de cabeçalhos).
  """
  return html_linha_resumo_de_sessao_IMP.gera(ses, bt_ver, bt_fechar, mostrar_usr)
