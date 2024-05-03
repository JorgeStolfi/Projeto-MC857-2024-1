import html_linha_resumo_de_usuario_IMP

def gera(usr):
  """
  Devolve uma lista de fragmentos HTML com os valores dos principais
  atributos do objeto {usr} da classe {obj_usuario.Classe}, incluindo o
  identificador {usr_id}. Esta função serve para gerar os elementos de
  uma linha da tabela produzida por {html_bloco_lista_de_usuarios.gera}.
  
  Se {usr} for {None}, o resultado é uma lista com os cabeçalhos das
  colunas da tabela ("Usuário", "Email", "Nome", etc.), em vez dos valores
  dos atributos.
  
  Cada elemento do resultado estará formatado com um estilo adequado.
  Veja {html_elem_item_de_resumo.gera}.
  
  Se {usr} não é {None}, resultado inclui também um botão "Ver" que dispara um comando
  HTTP "ver_usuario".  O argumento desse comando será {{ 'usuario': usr_id }}."""
  return html_linha_resumo_de_usuario_IMP.gera(usr)
