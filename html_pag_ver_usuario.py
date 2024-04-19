import html_pag_ver_usuario_IMP

def gera(ses, usr, erros):
  """
  Retorna uma página com formulário para examinar os dados
  do usuário {usr}.
  
  O parâmetro {ses} deve ser {None} (se o usuário que pediu
  está deslogado) ou o objeto {obj_sessao.Classe} de uma sessão aberta.
  
  O parâmetro {usr} não pode ser {None}; deve ser
  um objeto de tipo {obj_usuario.Classe}.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens (strings)
  a incluir na página.
  
  Alguns campos, como 'email', só serão exibidos se o dono da sessão 
  {ses} for administrador ou o próprio usuário {usr}.  O campo 'senha' 
  nunca é exibido.

  Dependendo de quem pediu, a página pode ter botões para alterar os
  dados do usuário, e buscar vídeos, sessões, e comentários do
  usuário.
  """
  return html_pag_ver_usuario_IMP.gera(ses, usr, erros)
