import html_form_postar_alterar_comentario_IMP

def gera(com_id, atrs, ed_nota):
  """
  Retorna um elemento "<form>...</form>" adequado para
  postar um novo comentário ou alterar os dados de um comentário existente.
  
  O parâmetro {com_id} deve ser {None} ou o identificador "C-{NNNNNNNN}"
  de um comentário que existe. No primeiro caso, o procedimento entende
  que se trata da postagem de um novo comentário. No segundo caso, o
  procedimento entende que se trata da edição do comentário {com} cujo
  identificador é {com_id}.
  
  O parâmetro booleano {ed_nota} diz se o atributo {nota} deve ser
  editável.
  
  O formulário terá campos editáveis com os atributos do comentário. O
  parâmetro {atrs} deve ser um dicionário que especifica valores
  iniciais para um subconjuto (possivelmente vazio) dos atributos de um
  comentário (vide {obj_comentario.Classe}). Os valores especificados em
  {atrs} serão mostrados no formulário em vez dos valores correntes dos
  atributos de {com}. Atributos cujo valor deveria ser um objeto podem
  estar representados em {atrs} pelos seus identificadores.
  
  O dicionário {atrs} deve sempre especificar os campos 'autor' e 'video',
  e opcionalmente 'pai'.  Como a 'data' só é definida quando o comentário
  é incluido na base de dados, esse atributo deve estar em {args}
  se e somente se {com_id} não é {None}.  Todos este atributos não
  podem ser alterados, e não serão editáveis no formulário.
  
  O formulário conterá um botão de tipo submit com texto "Salvar alterações"
  ou "Postar comentário", conforme o caso.  Quando clicado, 
  esse botão emitirá um comando POST com ação "alterar comentário" ou 
  "postar comentário", conforme o caso, cujos argumentos serão {com_id}
  com chave 'comentário' mais os valores dos atributos editáveis
  obtidos de {atrs} mais as alterações feitas pelo usuário.
  """
  return html_form_postar_alterar_comentario_IMP.gera(com_id, atrs, ed_nota)
