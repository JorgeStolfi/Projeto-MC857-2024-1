import obj_video_IMP

class Classe(obj_video_IMP.Classe_IMP):
  """
  Um objeto desta classe representa um vídeo armazenado no website e
  armazena seus atributos na memória, espelhando a linha correspondente
  da tabela "videos" da base de dados do sistema. Ele é criado
  quando alguém faz upload de um arquivo vídeo.
  
  O identificador de um vídeo (vide {obtem_indentificador} é uma string
  da forma "V-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela de
  vídeos, formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  (vide {obtem_atributos} abaixo) contém os seguintes campos:

    'autor'    {obj_usuario.Classe} O usuário que fez upload do vídeo.
    'titulo'   {str}   Título do vídeo (max 60 caracteres).
    'data'     {str}   Data de upload, no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
    'duracao'  {int}   Duração do vídeo em millissegundos.
    'largura'  {int}   Largura de cada frame, em pixels.
    'altura'   {int}   Atura de cada frame, em pixels.
    'nota'     {float} Nota média do vídeo (0 a 4).

  Outros atributos (categoria, legendas, etc) poderão ser acrescentados
  no futuro.
   
  Nenhum destes atributos pode ser {None}.
  
  A data de upload deve estar no formato ISO, "yyyy-mm-dd HH:MM:SS UTC".
  Por enquanto todas as datas são referentes ao fuso universal "UTC".

  Cada vídeo pertence a um unico usuário (autor), mas cada usuário
  pode ter vários vídeos.
  
  Em todas as funções abaixo, o parâmetro {vid} deve ser {None}
  ou um objeto desta classe.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada vídeo está representado no sistema por (a) um arquivo na pasta
  "videos", com nome "{video_id}.mp4"; e (b) por uma linha na tabela "videos"
  da base SQL em disco. Apenas algumas dessas linhas estarão
  representadas também na memória por objetos da classe
  {obj_video.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "V-", convertido para inteiro.  Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do vídeo
  (menos o identificador).
  """
  pass

def inicializa_modulo(limpa):
  """
  Inicializa o modulo, criando a tabela "videos" na base de dados. Deve
  ser chamada apenas uma vez no ínicio da execução do servidor, depois
  de chamar {db_base_sql.conecta} e {obj_usuario.inicializa_modulo}. Não
  retorna nenhum valor. Se o parâmetro booleano {limpa} for {True},
  apaga todas as linhas da tabela SQL, resetando o contador em 0.
  """
  obj_video_IMP.inicializa_modulo(limpa)

def cria(atrs):
  """
  Cria um novo objeto da classe {obj_video.Classe}, associada ao
  usuário {autor}, com os atributos {atrs}. Também acrescenta o vídeo à
  base de dados.
  
  O dicionário {atrs} deve ter apenas os campos 'autor' e
  'titulo' como especificados na {Classe} acima.
  
  O conteúdo do vídeo deve estar no atributo {atrs} com chave
  'conteudo'. Esse conteúdo será gravado no arquivo
  "videos/{vid_id}.mp4", onde {vid_id} é o identificador do objeto video
  a ser criado. Se a chave 'conteúdo' não existir em {atrs}, supõe que o
  arquivo já está gravado com esse nome.
  
  Os campos 'duracao', 'largura' e 'altura' do objeto serão extraídos desse arquivo. 
  O campo 'data' será a data corrente no momento da chamada desta função.
  O campo 'nota' será inicializado com -1.
  O identificador do novo objeto será derivado do seu índice na tabela.
  
  Em caso de sucesso, retorna o objeto criado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro.
  """
  return obj_video_IMP.cria(atrs)

def muda_atributos(vid, atrs_mod):
  """
  Modifica alguns atributos do objeto {vid} da classe
  {obj_video.Classe}, registrando as alterações na base de dados.
  Dá erro se {vid} é {None}.
  
  Recebe um dicionário Python {atrs_mod} cujas chaves são um subconjunto
  dos nomes de atributos do vídeo, exceto o identificador
  e as dimensões ('duracao', 'largura', 'altura'). 
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {atrs_mod}.  Os valores devem estar no formato de
  atributos na memória.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_video_IMP.muda_atributos(vid, atrs_mod)

def obtem_identificador(vid):
  """Devolve o identificador 'V-{NNNNNNNN}' do vídeo {vid}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_identificador(vid)

def obtem_objeto(vid_id):
  """Localiza um video com identificador {vid_id} (uma string da forma
  "V-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_video.Classe}.
  Se {vid_id} é {None} ou tal vídeo não existe, devolve {None}."""
  return obj_video_IMP.obtem_objeto(vid_id)

def obtem_atributos(vid):
  """Retorna um dicionário Python que é uma cópia dos atributos do
  vídeo {vid}, exceto identificador. Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_atributos(vid)

def obtem_atributo(vid, chave):
  """Retorna o atributo do vídeo {vid} com a {chave} dada.
  Equivale a {obtem_atributos(vid)[chave]}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_atributo(vid, chave)

def obtem_autor(vid):
  """Retorna o objeto da classe {obj_usuario.Classe} correspondente ao autor do
  vídeo {vid}.  Equivale a {obj_video.obtem_atributo(vid,'autor')}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_autor(vid)

def obtem_data_de_upload(vid):
  """Devolve a data de criação do vídeo {vid}.
  Equivale a {obj_video.obtem_atributos(vid,'criacao')}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_data_de_upload(vid)

def busca_por_campo(campo, val):
  """Localiza todos os vídeos cujo {campo} seja {valor}. Retorna a lista de ids
  desses vídeos."""
  return obj_video_IMP.busca_por_campo(campo, val)  

def busca_por_campos(args, unico):
  """Procura vídeos com atributos {args}, na memória ou na base de dados.
  
  Especificamente, para todo par {ch: val} em {args}, exige que o valor
  do atributo {ch} do objeto seja {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_video_IMP.busca_por_campos(args, unico)

def busca_por_autor(autor_id):
  """Localiza todos os vídeos do usuário com identificador {autor_id} (uma string da forma
  "U-{NNNNNNNN}").  Retorna uma lista de identificadores desses vídeos.
  Se {autor_id} é {None} ou o usuário não tem nenhum vídeo, devolve uma lista vazia."""
  return obj_video_IMP.busca_por_autor(autor_id)

def ultimo_identificador():
  """Devolve o identificador do último vídeo inserido na tabela.
  Se ainda não houver nenhum vídeo, devolve "V-00000000"."""
  return obj_video_IMP.ultimo_identificador()

# DEPURAÇÂO

def verifica_criacao(vid, vid_id, atrs):
  """Faz testes de consistência básicos de um objeto {vid} de classe
  {obj_video.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(vid)} devolve
  o identificador esperado {vid_id}, {obtem_atributos(vid)} devolve 
  os atributos esperados {atrs}, e {obtem_objeto(vid_id)}
  devolve o próprio {vid}.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_video_IMP.verifica_criacao(vid, vid_id, atrs)
 
def cria_testes(verb):
  """Limpa a tabela de vídeos com {inicializa(True)}, e cria alguns vídeos
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.

  Esta função deve ser chamada apenas uma vez no ínicio da execução do programa,
  depois de chamar {db_base_sql.conecta} e {obj_usuario.cria_testes}.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado."""
  obj_video_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas
  funções deste módulo."""
  obj_video_IMP.liga_diagnosticos(val)
