import html_pag_buscar_comentarios_IMP


def gera(ses, atrs, erros):
  """ Retorna uma página contendo o formulário para buscar comentários.
  Os campos do formulário são um subconjuto dos atributos de um objeto 
  da classe {obj_comentario.Class}.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos.
  
  A página terá um botão de tipo 'submit' com texto "Buscar" que,
  quando acionado, emite uma ação POST com comando 'buscar_comentarios'. 
  Haverá também um botão simples com texto "Cancelar" que emite
  o comando 'pag_principal'."""
  return html_pag_buscar_comentarios_IMP.gera(ses, atrs, erros)
