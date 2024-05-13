import html_pag_alterar_comentario_IMP

def gera(ses, com, atrs_mod, erros):
  """
  Retorna uma página com formulário para alterar os dados
  do comentário {com}. 
  
  O parâmetro {ses} deve ser um objeto {obj_sessao.Classe}. Não pode ser {None}.
  Determina o cabeçalho da página.
  
  O parâmetro {com} deve ser um objeto do tipo {obj_comentario.Classe}.
  Não pode ser {None}.
 
  O parâmetro {atrs_mod} deve ser um dicionário que especifica os
  valores iniciais para todos os campos editáveis do formulário. Esses
  valores serão usados em substituição aos atributos atuais do
  comentário {com}.  Atributos cujo valor deveria ser um objeto 
  podem estar representados em {atrs_mod} pelos seus identificadores.
  
  Vários atributos do comentário não podem ser alterados, nem mesmo pelo
  administrador. Os valores desses atributos, bem como o indentificador
  do comentário, serão mostrados mas não serão editáveis. Valores
  especificados para eles em {atrs_mod} serão ignorados.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens (strings)
  a incluir na página. 
  
  A página também terá um botão "Salvar" ou equivalente, que, quando
  clicado, emite o comando "alterar_comentario" cujos argumentos serão o
  identificador de {com} (com chave 'comentario') e os valores dos
  atributos editáveis, tais como constam do formulário. A página terá
  também um botão 'Cancelar', que, quando clicado, emite o comando
  'pag_principal'.

  A página terá botôes que permitem buscar as respostas ao comentário {com}
  e examinar o vídeo associado.
  
  Esta função não verifica se o dono da sessão {ses} tem permissão 
  para alterar o comando {com}.  Essa verificação deve ser feita por quem chama.
  """
  return html_pag_alterar_comentario_IMP.gera(ses, com, atrs_mod, erros)
