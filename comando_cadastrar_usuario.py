# Este módulo processa o acionamento por um novo usuário do botão "Cadastrar" dentro
# do formulário com os dados para cadastramento, que devem estar preenchidos.

import comando_cadastrar_usuario_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Cadastrar"
  em um formulário para cadastrar um novo usuário, após ter preenchido
  os campos do mesmo.
  
  Os dados do novo usuário devem estar definidos no dicionário {args}.
  Deve haver um campo 'senha' com valor não nulo e um campo 'conf_senha'
  com o mesmo valor.
  
  Se os dados forem aceitáveis, a função cria o novo usuário {usr},
  acrescentando-o à base de dado; e retorna um formulário 
  para o usuário fazer login (com campos para email e senha,
  e um botão "Entrar").
  
  Se os dados não forem aceitáveis, a função devolve o
  mesmo formulário de cadastrar usuário, com os mesmos
  dados nos campos preenchidos, com uma ou mais mensagens de erro
  adequadas."""
  return comando_cadastrar_usuario_IMP.processa(ses, args)
