import obj_vista_IMP

class Classe(obj_vista_IMP.Classe_IMP):
  """
  Um objeto desta classe representa uma ocasião em que um usuário assistiu um vídeo.
  É uma subclasse de {obj_raiz.Classe}.
  
  O identificador de uma vista (vide {obtem_indentificador} abaixo) é
  uma string da forma "A-{NNNNNNNN}" onde {NNNNNNNN} é o índice na
  tabela de vistas, formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  (vide {obtem_atributos} abaixo) contém os seguintes campos:

    'usuario'  {obj_usuario.Classe} O usuário que assistiu.
    'video'    {obj_video.Classe}   Vodeo que foi assistido.
    'data'     {str}                Data e hora (ISO, UTC) em que assistiu.

  Outros atributos poderão ser acrescentados no futuro.
  
  Nenhum destes atributos pode ser {None}.
  
  A data deve estar no formato ISO, "yyyy-mm-dd HH:MM:SS UTC".
  Por enquanto todas as datas são referentes ao fuso universal "UTC".

  Uma nova vista é criada "aberta" quando o usuario pede para assistir um vídeo.
  Vistas continuam registradas na tabela mesmo depois de fechadas,
  para fins de depuração, estatísticas, atendimento a usuários, etc..
  
  Vistas por usuários não logados não geram objetos {obj_vista.Classe} e não
  são registradas na base de dados, só contadas no
  atributo 'vistas' do vídeo.
  (Entretanto, o servidor HTTP do site -- separado deste sistema --
  provavelmente estará registrando todos os acessos num log.)
  
  Em todas as funções abaixo, o parâmetro {vis} deve ser {None}
  ou um objeto desta classe.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada vista é representada por uma
  linha na tabela "sessoes" da base SQL em disco. Apenas algumas dessas
  linhas são representadas também na memória por objetos da classe
  {obj_vista.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "A-", convertido para inteiro. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos da sessão
  (menos o identificador).
  """
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela "vistas" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor,
  depois de chamar {db_base_sql.conecta}. Não retorna nenhum valor.
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  obj_vista_IMP.inicializa_modulo(limpa)

def cria(usuario, video):
  """Cria um novo objeto da classe {obj_vista.Classe}, com os atributos dados.
  A data será a data corrente.  O identificador do novo objeto será derivado do seu
  índice na tabela.
  
  Em caso de sucesso, retorna o objeto. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro.
  """
  return obj_vista_IMP.cria(dono, cookie, criacao)

def obtem_identificador(vis):
  """Devolve o identificador 'A-{NNNNNNNN}' da vista {vis}.
  Dá erro se {vis} é {None}."""
  return obj_vista_IMP.obtem_identificador(vis)

def obtem_atributos(vis):
  """Retorna um dicionário Python que é uma cópia dos atributos da
  vista {vis}, exceto identificador. Dá erro se {vis} é {None}."""
  return obj_vista_IMP.obtem_atributos(vis)

def obtem_atributo(vis, chave):
  """Retorna o atributo da vista {vis} com a {chave} dada.
  Equivale a {obtem_atributos(vis)[chave]}.
  Dá erro se {vis} é {None}."""
  return obj_vista_IMP.obtem_atributo(vis, chave)

def obtem_objeto(ses_id):
  """Localiza uma sessao com identificador {ses_id} (uma string da forma
  "A-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {obj_vista.Classe}.
  Se {ses_id} é {None} ou tal vista não existe, devolve {None}."""
  return obj_vista_IMP.obtem_objeto(ses_id)

def busca_por_campo(campo, val):
  """Localiza todas as vistas cujo atributo {campo} seja {valor}. Retorna a lista de ids
  dessas vistas.  Equivale a {busca_por_campos({ chave: val }, unico = False)}."""
  return obj_vista_IMP.busca_por_campo(campo, val)  

def busca_por_campos(atrs, unico):
  """
  Busca vistas que satisfazem uma combinação de valores em vários
  campos, definidos pelo dicionário {atrs}. Especificamente, para todo
  par {ch: val} em {atrs}, exige que o valor do atributo {ch} do objeto
  case com {val}. Cada valor {val} pode ser um padrão SQL ou um
  intervalo; veja {obj_raiz.busca_por_campos} para maiores detalhes.
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_vista_IMP.busca_por_campos(atrs, unico)  

def ultimo_identificador():
  """Devolve o identificador da última vista inserida na tabela.
  Se ainda não houver nenhuma vista, devolve "A-00000000"."""
  return obj_vista_IMP.ultimo_identificador()

# DEPURAÇÂO

def verifica_criacao(vis, ses_id, atrs):
  """Faz testes de consistência básicos de um objeto {vis} de classe {obj_vista.Classe}.
  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(vis)} devolve
  o identificador esperado {ses_id}, {obtem_atributos(vis)} devolve 
  os atributos esperados {atrs}, e {obtem_objeto(ses_id)}
  devolve o próprio {vis}.
  
  Os atributos {atrs} NÃO devem incluir a data 'criacao'.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_vista_IMP.verifica_criacao(vis, ses_id, atrs)

def cria_testes(verb):
  """Limpa a tabela de vistas com {inicializa(True)}, e cria três vistas
  para fins de teste, incluindo-as na tabela.  As vistas estarão
  inicialmente abertas.  Não devolve nenhum resultado.

  Deve ser chamada apenas uma vez no ínicio da execução do programa,
  depois de chamar {db_base_sql.conecta}.Supõe que a tabela de usuários
  já foi inicializada e tem pelo menos três entradas.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado."""
  obj_vista_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas
  funções deste módulo."""
  obj_vista_IMP.liga_diagnosticos(val)
