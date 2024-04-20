import html_bloco_dados_de_usuario_IMP

def gera(id_usr, atrs, ses_admin, auto):
  """
  Retorna um bloco "<table>... </table>" contendo os dados de um usuário {usr}
  cujo identificador é {id_usr}, ou de um usuário a ser criado se {id_usr}
  for {None}.
  
  Pode ser usado paraentrar dados de um novo usuário, ou visualizar e
  possivelmente alterar dados de um usuário existente.
  
  Os campos da tabela serão inicializados com os atributos 
  no dicionário {atrs} (e não com os atributos atuais do usuário).
  
  O parâmetro booleano {ses_admin} deve ser {True} sse o usuário que pediu
  estes dados é administrador. O parâmetro booleano {auto} diz se o
  usuário que pediu os dados é o próprio {usr}.
  
  Se {id_usr} for {None}, retorna uma tabela de campos adequada para
  cadastrar novo usuário. Não haverá um campo para o identificador.
  
  Se {id_usr} não é {None}, retorma uma tabela de campos adequada para
  visualizar ou alterar os dados do usuário {usr} cujo identificador é
  {id_usr}, que supostamente já existe.
  
  Se {id_usr} for {None} ou {ses_admin} for {True} ou {auto} for {True}, a
  maioria dos campos serão visíveis e editáveis. Além do campo de senha,
  haverá um campo adicional para confirmação da mesma, com rótulo
  'conf_senha'. O atributo 'administrador' do usuário será visível,
  mas será editável só se {ses_admin} for True.
  
  Se  {id_usr} não é {None} e {ses_admin} e {auto} são ambos {False},
  apenas os campos públicos serão visíveis, e nenhum deles será editável.

  Se houver campos editáveis, este bloco deve ser incluído em um
  elemento "<form>...</form>" que deve incluir um botão de tipo submit.
  No comando POST gerado por esse botão, o identificador {id_usr} será
  incluído nos argumentos do comando com rótulo 'usuario'.
  """
  return html_bloco_dados_de_usuario_IMP.gera(id_usr, atrs, ses_admin, auto)
