import html_pag_cadastrar_usuario_IMP

def gera(ses, atrs, erros):
  """
  Retorna uma página com o formulário de cadastramento de
  novo usuario.

  O formuláro contém campos editáveis para as informações que o usuário
  deve preencher.  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais desses campos.

  O parâmetro {ses} é a sessão de login que pediu esta página. Se {ses}
  não for {None} e o dono da mesma for um administrador, o formulário
  terá a opão de cadastrar o novo usuário como administrador também.
  Vide detalhes em {html_bloco_dados_de_usuario.gera}.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens de erro
  a mostrar na página. 
  
  O formulário conterá um botão 'Cadastrar' (de tipo 'submit'). Quando o
  usuário clicar nesse botão, será emitido um comando POST com ação
  {cadastrar_usuario}. Os argumentos desse POST são todos os atributos
  da classe {obj_usuario.Classe}, com os valores de {atrs} que o usuário
  deve ter preenchido. Um argumento adicional 'conf_senha' conterá a
  confirmação de senha.

  O formulário também terá um botão simples 'Cancelar', que, quando
  clicado, emite o comando 'pag_principal'.
  
  Os argumentos {args} e {erros} se destinam a tratar o caso em que uma
  tentativa de cadastrar um novo usuário falha, e é então necessário
  exibir novamente esta página mas com as mensagens de erro e sem perder
  os dados que o usuário já preencheu. Veja-se
  {comando_cadastrar_usuario.processa}.
  """
  return html_pag_cadastrar_usuario_IMP.gera(ses, atrs, erros)
