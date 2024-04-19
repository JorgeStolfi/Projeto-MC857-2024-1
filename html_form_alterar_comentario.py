import html_form_alterar_comentario_IMP

def gera(id_com, atrs, ses_admin):
  """
  Retorna um elemento "<form>...</form>" adequado para
  alterar os dados de um comentário {com} cujo identificador é {id_com}.
  
  O parâmetro {id_com} deve ser o identificador "C-{NNNNNNNN}" de um
  comentário que existe. O formulário vai mostrar {id_com} como um campo
  "readonly".
  
  O parâmetro {atrs} deve ser um dicionário que especifica os valores
  iniciais dos campos editáveis do formulário.
  
  Se {ses_admin} for {True}, a função supõe que o formulário vai ser usado por
  um administrador. Se {ses_admin} for {False}, supõe vai ser usado
  por um usuário comum (não administrador) que é o 
  autor do comentário.
  
  Alguns atributos do comentário não podem ser alterados, nem mesmo
  pelo administrador. Esses atributos serão mostrados, mas como 
  "readonly". Se seus valores forem especificados em {atrs},
  eles devem coincidir com os respectivos valores atuais no
  comentário {com}.

  O formulário conterá um botão "Confirmar alterações" ou similar.
  Quando o usuário clicar nesse botão, será emitido um comando POST com
  ação "alterar_comentario". Os argumentos desse POST são todos os
  atributos da classe {obj_comentario.Classe}, com os valores de {atrs}
  a menos de alterações feitas pelo usuário.
  
  O formulário também terá um botão simples "Cancelar", que, 
  quando clicado, emite o comando "pag_principal".
  """
  return html_form_alterar_comentario_IMP.gera(id_com, atrs, ses_admin)
