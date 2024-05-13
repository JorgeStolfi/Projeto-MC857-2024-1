import html_form_alterar_usuario_IMP

def gera(usr_id, atrs, para_admin):
  """
  Retorna um elemento "<form>...</form>" adequado para
  alterar os dados de um usuário {usr} cujo identificador é {usr_id}.
  
  O parâmetro {usr_id} não pode ser {None}, e deve ser o identificador
  "U-{NNNNNNNN}" do usuário {usr}, que deve existir. O formulário vai
  mostrar {usr_id} como um campo "readonly".
  
  O formulário terá campos editáveis com os atributos do usuário. O
  parâmetro {atrs} deve ser um dicionário com um subconjuto
  (possivelmente vazio) das chaves desses atributos. Os valores
  especificados em {atrs} serão mostrados no formulário em vez dos
  valores correntes dos atributos de {usr}. O valor do atributo 'senha'
  não será mostrado, e haverá um campo editável adicional 'conf_senha'.
  
  Se {para_admin} for {True}, a função supõe que o formulário vai ser
  usado por um administrador. Nesse caso o formulário vai mostrar um
  checkbox editável para definir/mudar a categoria do usuário {usr}, para
  administrador ou usuário comum.

  Se {para_admin} for {False}, supõe que o formulário vai ser usado pelo
  próprio {usr} que é um usuário comum. comum (não administrador). Nesse
  caso não haverá o checkbox "administrador".
  
  Alguns atributos do usuário não podem ser alterados, nem mesmo
  pelo administrador. Esses atributos serão mostrados, mas como 
  "readonly". Se seus valores forem especificados em {atrs},
  eles devem coincidir vid os respectivos valores atuais 
  no usuário {usr}.

  O formulário conterá um botão (de tipo 'submit') com texto "Alterar",
  "Confirmar alterações" ou similar. Quando o usuário clicar nesse
  botão, será emitido um comando POST com ação "alterar usuario". Os
  argumentos desse POST são todos os atributos da classe
  {obj_usuario.Classe}, possivelmente substituidos pelos valores em
  {atrs} e edições feitas pelo dono da sessão, mais os argumentos
  'conf_senha' e 'usuario'.
  """
  return html_form_alterar_usuario_IMP.gera(usr_id, atrs, para_admin)
