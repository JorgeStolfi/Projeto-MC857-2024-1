import obj_sessao_IMP

class Classe(obj_sessao_IMP.Classe_IMP):
  """
  Um objeto desta classe representa uma sessao de acesso ao servidor
  por um usuário que fez login, e armazena seus atributos na memória,
  espelhando a linha correspondente da tabela "sessoes" da base de dados
  do sistema. É uma subclasse de {obj_raiz.Classe}.
  
  O identificador de uma sessão (vide {obtem_indentificador} abaixo) é
  uma string da forma "S-{NNNNNNNN}" onde {NNNNNNNN} é o índice na
  tabela de sessãoes, formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  (vide {obtem_atributos} abaixo) contém os seguintes campos:

    'dono'     {obj_usuario.Classe} O usuário cujo login criou a sessão.
    'aberta'   {bool}               Estado da sessao.
    'cookie'   {str}                Cookie da sessao.
    'criacao'  {str}                Data da criação da sessão.

  Outros atributos (IP, etc.) poderão ser acrescentados no futuro.
  
  Nenhum destes atributos pode ser {None}.
  
  A data de criação deve estar no formato ISO, "yyyy-mm-dd HH:MM:SS UTC".
  Por enquanto todas as datas são referentes ao fuso universal "UTC".

  Cada sessao pertence a um unico usuário, mas cada usuário
  pode ter várias sessoes abertas ao mesmo tempo. A sessao é criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout.
  Sessões continuam registradas na tabela mesmo depois de fechadas,
  para fins de depuração, estatísticas, atendimento a usuários, etc..
  
  Não é necessario fazer login para fazer certos acessos ao sistema,
  como fazer buscas e assistir vídeos.  Estes acessos não são
  registrados na base de dados, e não geram objetos {obj_sessao.Classe}.
  (Entretanto, o servidor HTTP do site -- separado deste sistema --
  provavelmente estará registrando todos os acessos num log.)
  
  Em todas as funções abaixo, o parâmetro {ses} deve ser {None}
  ou um objeto desta classe.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada sessão do sistema -- aberta ou fechada -- é representada por uma
  linha na tabela "sessoes" da base SQL em disco. Apenas algumas dessas
  linhas são representadas também na memória por objetos da classe
  {obj_sessao.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "S-", convertido para inteiro. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos da sessão
  (menos o identificador).
  """
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela "sessoes" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor,
  depois de chamar {db_base_sql.conecta}. Não retorna nenhum valor.
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  obj_sessao_IMP.inicializa_modulo(limpa)

def cria(dono, cookie, criacao):
  """
  Cria um novo objeto da classe {obj_sessao.Classe}, associada ao
  usuário {dono}, inicialmente aberta, com o cookie inicial {cookie}.
  Também acrescenta a sessão à base de dados.
  
  Se o parâmetro {criacao} é a data de criação da sessão (atributo 'criacao').
  Se for {None} será usada a data corrente no momento da chamada
  desta função. Senão, deve ser uma data em formato ISO com fuso horário
  "UTC".
  
  O identificador do novo objeto será derivado do seu
  índice na tabela.
  
  Em caso de sucesso, retorna o objeto. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro.
  """
  return obj_sessao_IMP.cria(dono, cookie, criacao)

def muda_atributos(ses, atrs_mod):
  """Modifica alguns atributos do objeto {ses} da classe
  {obj_sessao.Classe}, registrando as alterações na base de dados.
  Dá erro se {ses} é {None}.

  O parâmetro {atrs_mod} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos da sessão (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {atrs_mod}.  Os valores devem estar no formato de
  atributos na memória.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_sessao_IMP.muda_atributos(ses, atrs_mod)

def obtem_identificador(ses):
  """Devolve o identificador 'S-{NNNNNNNN}' da sessão {ses}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_identificador(ses)

def obtem_atributos(ses):
  """Retorna um dicionário Python que é uma cópia dos atributos da
  sessão {ses}, exceto identificador. Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_atributos(ses)

def obtem_atributo(ses, chave):
  """Retorna o atributo da sessão {ses} com a {chave} dada.
  Equivale a {obtem_atributos(ses)[chave]}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_atributo(ses, chave)

def obtem_dono(ses):
  """Retorna o objeto da classe {obj_usuario.Classe} correspondente ao usuario que
  fez login na sessao {ses}.  Equivale a {obj_sessao.obtem_atributo(ses,'dono')}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_dono(ses)

def aberta(ses):
  """Retorna o estado da sessão {ses}: {True} se a sessao ainda esta aberta,
  {False} se o usuário deu logout.  Equivale a {obj_sessao.obtem_atributo(ses,'aberta')}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.aberta(ses)

def obtem_cookie(ses):
  """Devolve o cookie da sessão {ses}.
  Equivale a {obj_sessao.obtem_atributos(ses,'cookie')}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_cookie(ses)

def obtem_data_de_criacao(ses):
  """Devolve a data de criação da sessão {ses}.
  Equivale a {obj_sessao.obtem_atributos(ses,'criacao')}.
  Dá erro se {ses} é {None}."""
  return obj_sessao_IMP.obtem_data_de_criacao(ses)

def de_administrador(ses):
  """Retorna {True} se a sessão {ses} não é {None}, está aberta, e
  o usuário da mesma é um administrador.  Caso contrário (em particular, se {ses} é {None})
  devolve {False}."""
  return obj_sessao_IMP.de_administrador(ses)

def obtem_objeto(ses_id):
  """Localiza uma sessao com identificador {ses_id} (uma string da forma
  "S-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {obj_sessao.Classe}.
  Se {ses_id} é {None} ou tal sessão não existe, devolve {None}."""
  return obj_sessao_IMP.obtem_objeto(ses_id)

def busca_por_dono(dono, soh_abertas):
  """Localiza todas as sessões do usuário com identificador {dono}.  
  Retorna uma lista de identificadores dessas sessões.  
  Se {dono} é {None} ou não existem tais sessões, devolve uma lista vazia.
  
  Se {soh_abertas} é {False}, retorna todas as sessões do {dono},
  abertas ou fechadas. Neste caso, equivale a {busca_por_campos({ 'dono': dono }, unico=False)}.
  
  Se {soh_abertas} é {True}, considera apenas as sessões abertas.
  Neste caso, equivale a {busca_por_campos({ 'dono': dono, 'aberta': True }, unico=False)}."""
  return obj_sessao_IMP.busca_por_dono(dono, soh_abertas)

def busca_por_campo(campo, val):
  """Localiza todas as sessões cujo atributo {campo} seja {valor}. Retorna a lista de ids
  dessas sessões.  Equivale a {busca_por_campos({ chave: val }, unico = False)}."""
  return obj_sessao_IMP.busca_por_campo(campo, val)  

def busca_por_campos(atrs, unico):
  """
  Busca sessões que satisfazem uma combinação de valores em vários
  campos, definidos pelo dicionário {atrs}. Especificamente, para todo
  par {ch: val} em {atrs}, exige que o valor do atributo {ch} do objeto
  case com {val}. Cada valor {val} pode ser um padrão SQL ou um
  intervalo; veja {obj_raiz.busca_por_campos} para maiores detalhes.
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_sessao_IMP.busca_por_campos(atrs, unico)  

def fecha(ses):
  """Registra o logout do usuário na sessão {ses}, mudando o atributo 'aberta'
  permanentemente para {False}. Também altera esse campo na base de dados.
  A sessão não pode ser {None} e deve estar aberta.  Não retorna nenum resultado."""
  obj_sessao_IMP.fecha(ses)

def ultimo_identificador():
  """Devolve o identificador da última sessão inserida na tabela.
  Se ainda não houver nenhuma sessão, devolve "S-00000000"."""
  return obj_sessao_IMP.ultimo_identificador()

# DEPURAÇÂO

def verifica_criacao(ses, ses_id, atrs):
  """Faz testes de consistência básicos de um objeto {ses} de classe {obj_sessao.Classe}.
  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(ses)} devolve
  o identificador esperado {ses_id}, {obtem_atributos(ses)} devolve 
  os atributos esperados {atrs}, e {obtem_objeto(ses_id)}
  devolve o próprio {ses}.
  
  Os atributos {atrs} NÃO devem incluir a data 'criacao'.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_sessao_IMP.verifica_criacao(ses, ses_id, atrs)

def cria_testes(verb):
  """Limpa a tabela de sessoes com {inicializa(True)}, e cria três sessões
  para fins de teste, incluindo-as na tabela.  As sessões estarão
  inicialmente abertas.  Não devolve nenhum resultado.

  Deve ser chamada apenas uma vez no ínicio da execução do programa,
  depois de chamar {db_base_sql.conecta}.Supõe que a tabela de usuários
  já foi inicializada e tem pelo menos três entradas.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado."""
  obj_sessao_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas
  funções deste módulo."""
  obj_sessao_IMP.liga_diagnosticos(val)
