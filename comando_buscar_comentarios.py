import comando_buscar_comentarios_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o usuário aperta o botão "Buscar" em um
  formulário de busca de comentários (vide
  {html_form_buscar_comentarios.gera}). Ela procura na base de dados os
  comentários cujos atributos casam os dados especificados em
  {cmd_args}.
  
  O resultado será uma página com a lista dos comentários encontrados,
  em forma resumida. Vide {html_bloco_lista_de_comentarios.gera}.
  
  O parâmetro {ses} deve ser {None} ou o objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário que contém os parâmetros
  da busca, que o usuário preencheu no formulário. Devem ser um
  subconjunto dos atributos de um objeto comentário
  ({obj_comentario.Classe}) --- por exemplo, {{'autor': "U-00000007",
  'data': "2024", 'texto': "bananas"}}. O dicionário {cmd_args} pode ter
  também um campo 'comentario' com o ID de um comentário específico, por
  exemplo {{'comentario': "C-00001234"}}.
  
  Note que atributos de {obj_comentario.Classe} cujos valores
  são objetos (como 'autor', 'video', e 'pai') devem ser
  representados em {cmd_args} pelos seus identificadores.
  
  Atributos de {obj_comentario.Classe} que tem valor {None} em
  {cmd_args} (ou estão omitidos) serão ignorados na busca.
  
  No casos dos campos 'comentario', 'video', 'autor', e 'pai', a
  busca será feita pelo valor exato. Nos caso dos campos 'texto' e
  'data', será feita uma busca por valor aproximado.

  Se houver erros nos argumentos, ou a busca não encontrar nenhum
  comentário, devolve o formulário de buscar comentários (veja
  {html_pag_buscar_comentarios.gera}) com os campos {cmd_args}
  preenchidos, mais os avisos de erro.
  """
  return comando_buscar_comentarios_IMP.processa(ses, cmd_args)
