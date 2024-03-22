import html_bloco_dados_de_usuario_IMP

def gera(id_usr, atrs, admin):
  """
  Retorna um bloco "<table>... </table>" contendo os dados de um usuário.  
  
  Os campos da tabela serão inicializados com os atributos 
  no dicionário {atrs} (e não com os atributos atuais do usuário).
  
  Alguns campos são editáveis
  e portanto este bloco deve ser incluído em um elemento "<form>...</form>".
  Pode ser usado para entrar dados de um novo usuário ou alterar dados de 
  um usuário existente;
  
  Se o parâmetro booleano {admin} for {True}, a função supõe que o formulário 
  foi solicitado por um administrador.  Nesse caso o formulário mostrará o 
  atributo 'administrador' do usuário como editável.
  
  Se {id_usr} é {None}, retorna uma tabela de campos adequada para cadastrar novo usuário.
  Não haverá um campo para o identifcador, e todos os campos serão editáveis.  
  
  Se {id_usuário} não é {None}, retorma uma tabela de campos adequada
  para alterar os dados do usuário {usr} cujo identificador é
  {id_usr}, que supostamente já existe. O identificador será visível
  se {admin} for {True}. Num POST, será enviado com rótulo 'id_usuario'.
  Todos os campos serão editáveis, exceto o identificador.
  
  Em qualquer caso, o formulário terá um campo adicional 
  para repetição da senha, com rótulo 'conf_senha'.
  """
  return html_bloco_dados_de_usuario_IMP.gera(id_usr, atrs, admin)
