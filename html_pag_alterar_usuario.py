import html_pag_alterar_usuario_IMP

def gera(ses, id_usr, atrs, erros):
  """
  Retorna uma página com formulário para alterar os atributos
  de um usuário cadastrado {usr} cujo identificador é {id_usr}. 
  
  O parâmetro {ses} deve ser um objeto {obj_sessao.Classe} de uma sessão
  aberta, diferente de {None}.
  
  O parâmetro {id_usr} pode ser {None} (significando que o usuário {usr}
  a alterar é o dono da sessão {ses}). Senão, deve ser o identificador
  "U-{NNNNNNNN}" do usuário {usr} a alterar. EM qualquer caso, se a
  sessão {ses} não for de administrador, o usuário {usr} deve ser o dono
  da sessão {ses}.
  
  O parâmetro {atrs} deve ser {None} ou um dicionário que especifica 
  valores iniciais para alguns ou todos os campos editáveis do formulário, que
  podem diferir dos valores dos atributos atuais do usuário {usr}.
  Atributos que não aparecem em {atrs} não serão alterados.
  
  Os campos 'senha' e 'conf_senha', se estiverem presentes em {atrs},
  serão igorados. No formulário, estes campos estarão sempre em branco.
  A página vai mostrar também identificador do usuário, como um campo
  "readonly" com chave 'usuario'.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens (strings)
  a incluir na página.
  
  Se a sessão {ses} for de administrador, o formulário vai mostrar um
  checkbox para mudar a categoria do usuário {usr}, para administrador
  ou usuário comum. Se o dono da sessão {ses} é usuário comum (não
  administrador) esse checkbox será "readonly".

  O formulário em si será criado por {html_form_criar_alterar_usuario.gera}.
  Ele incluirá um botão "Confirmar alterações" (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  "alterar_usuario".  Os argumentos desse POST serão todos os atributos da classe
  {obj_usuario.Classe}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário, mais o atributo 'conf_senha'.

  A página resultante terá botôes que permitem buscar as sessãoes abertas, 
  os vídeos, e comentários do usuário {usr}. O formulário também terá
  um botão simples "Cancelar", que, quando clicado, emite o comando
  "pag_principal".
  """
  return html_pag_alterar_usuario_IMP.gera(ses, id_usr, atrs, erros)
