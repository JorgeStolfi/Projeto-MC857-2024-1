import html_linha_resumo_de_comentario_IMP

def gera(com, para_admin, mostra_autor, mostra_video, mostra_pai, mostra_nota):
  """
  Devolve uma lista de fragmentos HTML com os valores dos principais
  atributos do objeto {com} da classe {obj_comentario.Classe}, incluindo o
  identificador {com_id}. Esta função é usada por {html_bloco_lista_de_comentarios.gera} 
  para gerar os elementos de uma linha da tabela, a ser criada por {html_elem_table.gera}.

  O parâmetro booleano {para_admin} diz se quem pediu estas informações
  é um administrador. Se o atributo 'bloqueado' do comentário for
  {True}, o texto do mesmo só vai ser visível para administradores; para
  os demais só vai aparecer a palavra "[BLOQUEADO]".
  
  Os parâmetros {mostra_autor}, {mostra_video}, {mostra_pai},
  {mostra_nota} determinam se o resumo vai incluir os campos 'autor',
  'video', 'pai', e 'nota', respectivamente.
  
  Se {com} for {None}, o resultado é uma lista com os cabeçalhos das
  colunas da tabela ("Comentário", "Vídeo", etc.), em vez dos valores
  dos atributos.
  
  Cada elemento do resultado estará formatado com um estilo adequado.
  Veja {html_elem_item_de_resumo.gera}.
  
  Se {com} não é {None}, resultado inclui também um campo com um botão
  "Ver" que dispara um comando HTTP "ver_comentario". O argumento desse
  comando será {{ 'comentario': com_id }}.
  
  Se {com} não é {None} e {para_admin} é {true}, a linha terá também um
  botão "Bloquear" ou "Desbloquear" que emite um comando
  "alterar_comentario", com argumentos {{ 'comentario': com_id,
  'bloqueado': B }} onde {B} é a negação do estado atual do atributo
  'bloqueado' do comentário.
  """
  return html_linha_resumo_de_comentario_IMP.gera(com, para_admin, mostra_autor, mostra_video, mostra_pai, mostra_nota)
