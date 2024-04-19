import html_pag_buscar_usuarios_IMP


def gera(ses, atrs, erros):
  """ Retorna uma página contendo o formulário para buscar usuários.
  Os campos do formulário são um subconjuto dos atributos de um objeto
  da classe {obj_usuario.Class}.
  
  O parâmetro {ses} é a sessão de login que solicitou a página.
  Se for {None}, significa que o usuário não estava logado.
  Senão, deve ser um objeto de tipo {obj_sessao.Classe},
  ainda aberto.

  Se {atrs} não for {None}, deve ser um dicionário que define os
  valores iniciais de todos ou alguns campos. 
  
  A página terá um botão de tipo 'submit' com texto "Buscar" que,
  quando acionado, emite uma ação POST com comando 'buscar_usuarios'. 
  Haverá também um botão simples com texto "Cancelar" que emite
  o comando 'pag_principal'.
   
  Apenas administradores podem fazer buscas por certos campos, 
  como 'email'.  Usuários não logados podem ter outras restrições"""
  return html_pag_buscar_usuarios_IMP.gera(ses, atrs, erros)
