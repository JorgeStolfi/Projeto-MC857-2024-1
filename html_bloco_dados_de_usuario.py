import html_bloco_dados_de_usuario_IMP

def gera(id_usr, atrs, ses_admin, ses_proprio, readonly):
  """
  Retorna um bloco "<table>... </table>" contendo os dados de um usuário {usr}
  cujo identificador é {id_usr}, ou de um usuário a ser criado se {id_usr}
  for {None}.
  
  Pode ser usado para entrar dados de um novo usuário, ou visualizar e
  possivelmente alterar dados de um usuário existente.
  
  Os campos da tabela serão inicializados com os atributos 
  no dicionário {atrs} (e não com os atributos atuais do usuário).
  
  Os parâmetros booleano {ses_admin} e {ses_proprio} devem dizer se o usuário
  que pediu estas informações é administrador ou o próprio {usr},
  respecivamente.  Eles controlam a exibição e edição 
  de certos campos, como especificado abaixo

  O parâmetro booleano {readonly} determina se os dados exibidos serão editáveis.
  
  Se {id_usr} for {None}, retorna uma tabela de campos adequada para
  cadastrar novo usuário. Não haverá um campo para o identificador. O
  atributo 'administrador' será visível e editável se {ses_admin} for
  {True}; caso contrário será invisível, readonly, e inicializado com
  {False}. Todos os demais atributos, inclusive 'senha' e 'email', serão
  editáveis. Neste caso, o parâmetro {ses_proprio} é ignorado.
  
  Se {id_usr} não é {None}, retorma uma tabela de campos adequada para
  visualizar ou alterar os dados do usuário {usr} cujo identificador é
  {id_usr}, que supostamente já existe. Neste caso, a maioria dos
  atributos serão editáves se e somente se {edit = (ses_admin or ses_proprio)}
  for {True}. Especificamente:
  
    * O campo "Usuário" mostrará o {id_usr}, sempre readonly, com 
      chave 'usuario'.
    
    * O atributo 'email' é exibido e editável apenas se {edit} for {True}.
    
    * Haverá um campo editável para o atributo 'senha' se {edit}
      for {True}; caso contrário esse atributo será omitido.
      
    * Os demais atributos, como 'nome', serão sempre exibidos; e serão editáveis
      se {edit} for {True}, ou readonly se {edit} for {False}
    
  Em qualquer caso, se o atributo 'senha' for exibido, será editável,
  e haverá um campo editável adicional para confirmação da mesma, com
  chave 'conf_senha'. Estes campos estarão sempre em branco: seus
  valores em {atrs}, se existirem, são ignorados.  Se {edit}
  for {False}, a senha não será exibida.

  Se houver campos editáveis, este bloco deve ser incluído em um
  elemento "<form>...</form>" que deve incluir um botão de tipo submit.
  No comando POST gerado por esse botão, o identificador {id_usr} será
  incluído nos argumentos do comando com chave 'usuario'.
  """
  return html_bloco_dados_de_usuario_IMP.gera(id_usr, atrs, ses_admin, ses_proprio, readonly)
