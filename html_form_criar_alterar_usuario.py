import html_form_criar_alterar_usuario_IMP

def gera(id_usr, atrs, admin, texto_bt, comando_bt):
  """Retorna um elemento "<form>...</form>" adequado para criar ou alterar os dados
  de um usuário {usr} cujo identificador é {id_usr}.
  
  O formulário contém campos editáveis com os atributos
  (possivelmente alterados) do usuário, especificados no dicionário {atrs}.
  O valor de {atrs['senha']} não será mostrado, e haverá um
  campo adicional 'conf_senha'.
  
  Se {id_usr} é {None}, supõe que o usuário está sendo criado 
  e ainda não tem identificador.  Se {id_usr} não é {None},
  supõe que os dados do usuário estão sendo alterados, e 
  a página vai mostrar o campo {id_usr} como "readonly"
  e rótulo (para POST) 'id_usuario'.
  
  Se {admin} for {True}, supõe que a página foi pedida por um
  administrador. Nesse caso o formulário vai mostrar um checkbox para
  mudar a categoria do usuário {usr}, para administrador ou 
  usuário comum.

  Se {admin} for {False}, supõe que a página foi pedida pelo próprio 
  {usr} que é um usuário comum (não administrador). Nesse caso não
  haverá o checkbox "administrador".

  O formulário conterá um botão (de tipo 'submit') com texto {texto_bt}.
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {comando_bt}.  Os argumentos desse POST são todos os atributos da classe
  {obj_usuario.Classe}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário, mais os atributos 'conf_senha' e 'id_usuario'.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_criar_alterar_usuario_IMP.gera(id_usr, atrs, admin, texto_bt, comando_bt)
