import comando_buscar_videos_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o usuário aperta o botão "Buscar" em
  uma formulário de busca de vídeos (vide
  {html_form_buscar_videos.gera}). Ela procura na base de dados os
  vídeos cujos atributos casam os dados especificados em {cmd_args}. 
  
  O resultado será uma página com a lista dos vídeos encontrados, em
  forma resumida. Vide {html_bloco_lista_de_videos.gera}.
  
  O parâmetro {ses} deve ser {None} (indicando que o leitor não está
  logado), ou o objeto {obj_sessao.Classe} de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário que contém os parâmetros
  da busca, que o usuário preencheu no formulário. Devem ser um
  subconjunto dos atributos de um objeto vídeo ({obj_video.Classe}) ---
  por exemplo, {{'autor': "U-00000007", 'data': "2024", 'titulo':
  "bananas"}}. O dicionário {cmd_args} pode ter também um campo 'video'
  com o ID de um vídeo específico.
  
  Note que atributos de {obj_video.Classe} cujos valores são objetos
  (como 'autor') devem ser representados em {cmd_args} pelos seus
  identificadores.
  
  Atributos de {obj_video.Classe} que tem valor {None} em
  {cmd_args} (ou estão omitidos) serão ignorados na busca.
  
  No casos dos campos 'video', 'arq', e 'autor' de {cmd_args}, a
  busca será feita pelo valor exato. Nos caso dos campos 'titulo' e
  'data', será feita uma busca por valor aproximado.

  Se houver erros nos argumentos, ou a busca não encontrar nenhum vídeo,
  devolve o formulário de buscar vídeos com os campos {cmd_args}
  preenchidos, mais os avisos de erro.
  """
  return comando_buscar_videos_IMP.processa(ses, cmd_args)
