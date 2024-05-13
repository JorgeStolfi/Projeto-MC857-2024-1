import html_form_cadastrar_usuario_IMP

def gera(atrs, para_admin):
  """
  Retorna um formulário HTML (um elemento "<form>...</form>") adequado para
  cadastrar um novo usuário no sistema.  O formulário terá campos editáveis 
  para o usuário espcificar os atributos do novo usuário.
  
  O parâmetro {atrs} deve ser {None} ou um dicionário com 
  valores iniciais (defaults) para alguns ou todos esses atributos.
  
  Se o parâmetro booleano {para_admin} for {True}, a função supõe que o formulário 
  foi pedido por um administrador. Nesse caso o formulário vai mostrar um
  checkbox editável para definir a categoria do novo usuário (administrador 
  ou usuário comum).

  Se {para_admin} for {False}, supõe que o formulário vai ser usado por
  um usuário comum (não administrador). Nesse caso não haverá o checkbox
  "administrador".
  
  O valor de {atrs['senha']}, se existir, não será mostrado, e haverá um
  campo adicional 'conf_senha'.

  O formulário terá um botão (de tipo 'submit') com texto "Cadastrar" ou
  equivalente. Quando o usuário clicar nesse botão, será emitido um
  comando POST com ação {cadastrar_usuario}. Os argumentos desse POST
  são todos os atributos da classe {obj_usuario.Classe}, com os valores
  que estiverem no formulário nesse momento, incluindo 'conf_senha'.
  """
  return html_form_cadastrar_usuario_IMP.gera(atrs, para_admin)
