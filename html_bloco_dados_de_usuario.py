import html_bloco_dados_de_usuario_IMP

def gera(usr_id, atrs, editavel, para_admin, para_proprio):
  """
  Retorna um fragmento HTML que exibe dados do usuário {usr}
  cujo identificador é {usr_id}, ou de um usuário a ser criado se {usr_id}
  for {None}.
  
  Esta função pode ser usada para entrar dados de um novo usuário, ou
  visualizar e possivelmente alterar dados de um usuário existente.
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Nome", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente. Alguns atributos podem ser editáveis, portanto este
  bloco deve ser incluído em um elemento "<form>...</form>". Veja
  {html_elem_form.gera}.
  
  O parâmetro {usr_id} deve ser {None} ou o identificador (um string no
  formato "U-{NNNNNNNN}") de um usuário existente.
  
  O parâmetro {atrs} deve ser {None} ou um {dict}.  Os valores iniciais
  dos campos do formulário serão obtidos de {atrs}, se constarem ali,
  ou do usuário {usr} caso contrário.
  
  Os parâmetros booleano {editavel}, {para_admin} e {para_proprio}
  especificam quais campos do formulário serão visíveis e/ou editáveis,
  como detalhado abaixo. Se {para_admin} for {True}, a função entende que
  o usuário que pediu o formulário é administrador. Se {para_proprio} for
  {True}, entende que o formulário foi pedido pelo próprio {usr}.
  
  Se {editavel} é {False}, nenhum campo será editável.  Se for {True},
  os campos editáveis dependerão de {para_admin} e {para_proprio}.
  
  Os campos da tabela serão inicializados com os atributos 
  no dicionário {atrs} (e não com os atributos atuais do usuário).
  
  Se {usr_id} é {None}, retorna uma tabela de campos adequada para
  cadastrar novo usuário. O parâmetro {editavel} deve ser {True} neste
  caso. Não haverá um campo para o identificador. O atributo
  'administrador' será visível e editável se {para_admin} for {True};
  caso contrário será invisível, readonly, e inicializado com {False}.
  Todos os demais atributos, inclusive 'senha' e 'email', serão
  editáveis. Neste caso, o parâmetro {para_proprio} é ignorado.
  
  Se {usr_id} não é {None}, retorma uma tabela de campos adequada para
  visualizar ou alterar os dados do usuário {usr} cujo identificador é
  {usr_id}, que supostamente já existe. Neste caso, alguns campos
  serão editáves se e somente se {editavel} for {True}. Especificamente:
  
    * haverá um campo "Usuário", sempre readonly, que mostra
    {usr_id}, com chave 'usuario'.
    
    * O atributo 'email' é exibido apenas se {para_admin or para_proprio}
    for {True}, e será editável apenas se {editavel} for {True}.
    
    * O atributo 'administrador' é exibido, e será e será editável
    apenas se {editavel} e {para_admin} forem ambos {True}.
    
    * Haverá um campo editável para o atributo 'senha' se {editavel}
    for {True}; caso contrário esse atributo será omitido, independentemente
    de {para_admin} e {para_proprio}.

    * O atributo 'vnota' é exibido e será editável 
    apenas se {editavel} e {para_admin} forem ambos {True}.
      
    * Os demais atributos, como 'nome', serão sempre exibidos; e serão editáveis
    se {editavel} for {True}.
    
  Em qualquer caso, se o atributo 'senha' for exibido, ele será editável,
  e haverá um campo editável adicional para confirmação da mesma, com
  chave 'conf_senha'. Estes campos estarão sempre em branco: seus
  valores em {atrs}, se existirem, são ignorados.  Se {edit}
  for {False}, a senha não será exibida.

  Se houver campos editáveis, este bloco deve ser incluído em um
  elemento "<form>...</form>" que deve incluir um botão de tipo submit.
  No comando POST gerado por esse botão, o identificador {usr_id} será
  incluído nos argumentos do comando com chave 'usuario'.
  """
  return html_bloco_dados_de_usuario_IMP.gera(usr_id, atrs, editavel, para_admin, para_proprio)
