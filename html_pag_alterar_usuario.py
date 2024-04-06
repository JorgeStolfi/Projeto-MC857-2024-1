import html_pag_alterar_usuario_IMP

def gera(ses, id_usr, atrs, admin, erros):
  """Retorna uma página com formulário para alterar os dados
  do usuário {usr} cujo identificador é {id_usr}.
  
  O formuláro contém campos editáveis com os atributos
  correntes do usuário, especificados no dicionário {atrs}.
  O valor de {atrs['senha']} não será mostrado, e haverá um
  campo adicional 'conf_senha'.
  
  Se {admin} for {True}, supõe que a página foi pedida por um
  administrador. Nesse caso o formulário vai mostrar um checkbox para
  mudar a categoria do usuário {usr}, para administrador ou usuário comum. A
  página vai mostrar também o campo {id_usr} como "readonly".

  Se {admin} for {False}, supõe que a página foi pedida pelo próprio 
  {usr} que é um usuário comum (não administrador). Nesse caso não
  haverá o checkbox "administrador", e o campo {id_usr} será
  "hidden".

  O formulário conterá um botão 'Alterar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {alterar_usuario}.  Os argumentos desse POST são todos os atributos da classe
  {obj_usuario.Classe}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário, mais o atributo 'conf_senha'.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'pag_principal'."""
  return html_pag_alterar_usuario_IMP.gera(ses, id_usr, atrs, admin, erros)
