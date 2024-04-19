import comando_buscar_sessoes_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o usuário aperta o botão "Buscar" em
  um formulário de busca de sessões (vide
  {html_form_buscar_sessoes.gera}). Ela procura na base de dados os
  sessões cujos atributos casam os dados especificados em
  {cmd_args}. 
  
  O resultado será uma página com a lista dos sessões encontrados,
  em forma resumida. Vide {html_bloco_lista_de_sessoes.gera}.
  
  O parâmetro {ses} deve ser {None} ou o objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário que contém os parâmetros
  da busca, que o usuário preencheu no formulário. Devem ser um
  subconjunto dos atributos de um objeto sessão
  ({obj_sessao.Classe}) --- por exemplo, {{'usuario': "U-00000007",
  'criada': "2024"}}. O dicionário {cmd_args} pode ter
  também um campo 'sessao' com o ID de um sessão específico, por
  exemplo {{'sessao': "S-00001234"}}.
  
  Note que atributos de {obj_sessao.Classe} cujos valores
  são objetos (como 'usuario') devem ser
  representados em {cmd_args} pelos seus identificadores.
  
  Atributos de {obj_sessao.Classe} que tem valor {None} em
  {cmd_args} (ou estão omitidos) serão ignorados na busca.
  
  No casos dos campos 'sessao', 'usuario', e 'aberta', a
  busca será feita pelo valor exato. Nos caso do campo
  'data', será feita uma busca por valor aproximado.

  Se houver erros nos argumentos, ou a busca não encontrar nenhum sessão,
  devolve o formulário de buscar sessões (veja {html_pag_buscar_sessoes.gera})
  com os campos {cmd_args} preenchidos, mais os avisos de erro.
  """
  return comando_buscar_sessoes_IMP.processa(ses, cmd_args)
