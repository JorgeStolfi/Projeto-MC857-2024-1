import html_form_criar_alterar_usuario_IMP

def gera(id_usr, atrs, ses_admin, texto_bt, comando_bt):
  """
  Retorna um elemento "<form>...</form>" adequado para criar ou 
  alterar os dados de um usuário {usr} cujo identificador é {id_usr}.
  
  O formulário contém campos editáveis com os atributos (possivelmente
  alterados) do usuário, especificados no dicionário {atrs}.  O valor de
  {atrs['senha']} não será mostrado, e haverá um campo adicional
  'conf_senha'.
  
  Se {id_usr} é {None}, a função supõe que o usuário está sendo criado e
  ainda não tem identificador. Se {id_usr} não é {None}, deve ser o
  identificador "U-{NNNNNNNN}" de um usuário que existe. neste casoa a
  função supõe que os dados do usuário estão sendo alterados, e o formulário
  vai mostrar {id_usr} como um campo "readonly".
  
  Se {ses_admin} for {True}, a função supõe que o formulário vai ser
  usado por um administrador. Nesse caso o formulário vai mostrar um
  checkbox para definir/mudar a categoria do usuário {usr}, para
  administrador ou usuário comum.

  Se {ses_admin} for {False}, supõe que o fortmulário vai ser usado por um usuário
  comum (não administrador). Nesse caso não haverá o checkbox
  "administrador". Neste caso, se {id_usr} não for {None}, a função supóe 
  que ele é o dono da sessão que pediu o formulário.

  O formulário conterá um botão (de tipo 'submit') com texto {texto_bt}.
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {comando_bt}.  Os argumentos desse POST são todos os atributos da classe
  {obj_usuario.Classe}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário, mais os atributos 'conf_senha' e 'usuario'.
  
  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'pag_principal'.
  """
  return html_form_criar_alterar_usuario_IMP.gera(id_usr, atrs, ses_admin, texto_bt, comando_bt)
