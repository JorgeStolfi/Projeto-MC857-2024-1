# Este módulo define a classe de objetos {obj_video.Classe}, que
# representa um vídeo armazenado no website.
#
# Nas funções abaixo, o parâmetro {usr} é um objeto da classe {obj_usuario.Classe}
# que representa o usuário.

# Implementaçao deste módulo:
import obj_video_IMP

class Classe(obj_video_IMP.Classe_IMP):
  """Um objeto desta classe representa um vídeo armazenado no website.
  Os atributos deste objeto, por enquanto, são:

    'autor'    {obj_usuario.Classe} o usuário que fez upload do vídeo.
    'arq'      {str}   nome do arquivo de vídeo.
    'titulo'   {str}   título do vídeo (max 60 caracteres).
    'data'     {str}   data de upload, no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
    'duracao'  {int}   duração do vídeo em millissegundos.
    'largura'  {int}   largura de cada frame, em pixels.
    'altura'   {int}   atura de cada frame, em pixels.

  Outros atributos (categoria, ) poderão ser acrescentados no futuro.

  Além desses atributos, cada vídeo tem um identificador, 
  uma string da forma "V-{NNNNNNNN}" onde {NNNNNNNN} é o índice
  na tabela de vídeos (vide abaixo) formatado em 8 algarismos.

  Cada vídeo pertence a um unico usuário, mas cada usuário
  pode ter vários vídeos.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada vídeo está representado no sistema por (a) um arquivo na pasta "videos",
  com nome "{arq}.mp4"; e (b) por uma
  linha na tabela "videos" da base SQL em disco. Apenas algumas dessas
  linhas estarão representadas também na memória por objetos da classe
  {obj_video.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "V-", convertido para inteiro.  Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do vídeo
  (menos o identificador)."""
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela "videos" na base de dados. Deve
  ser chamada apenas uma vez no ínicio da execução do servidor, depois
  de chamar {db_base_sql.conecta} e {obj_usuario.inicializa_modulo}. Não
  retorna nenhum valor. Se o parâmetro booleano {limpa} for {True},
  apaga todas as linhas da tabela SQL, resetando o contador em 0.
  """
  obj_video_IMP.inicializa_modulo(limpa)

def cria(atrs):
  """Cria um novo objeto da classe {obj_video.Classe}, associada ao usuário {autor},
  com os atributos {atrs}.  Também acrescenta o vídeo à base de dados. 
  Atribui um identificador único ao vídeo, derivado do seu índice na tabela. 
  
  O dicionário {atrs} deve ter apenas os campos 'autor', 'arq', e
  'titulo' como especificados na {Classe} acima. O conteúdo do vídeo já
  deve estar gravado no arquivo "videos/{arq}". Os camos 'duracao',
  'largura' e 'altura' do objeto serão extraídos desse arquivo. O campo
  'data' será a data corrente.
  
  Em caso de sucesso, retorna o objeto criado."""
  return obj_video_IMP.cria(atrs)

def obtem_identificador(vid):
  """Devolve o identificador 'V-{NNNNNNNN}' do vídeo {vid}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_identificador(vid)

def obtem_atributos(vid):
  """Retorna um dicionário Python que é uma cópia dos atributos do
  vídeo {vid}, exceto identificador.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_atributos(vid)

def obtem_atributo(vid, chave):
  """Retorna o atributo do vídeo {vid} com a {chave} dada.
  Equivale a {obtem_atributos(vid)[chave]}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_atributo(vid, chave)

def obtem_usuario(vid):
  """Retorna o objeto da classe {obj_usuario.Classe} correspondente ao usuario que
  fez login na video {vid}.  Equivale a {obj_video.obtem_atributo(vid,'autor')}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_usuario(vid)

def obtem_data_de_upload(vid):
  """Devolve a data de criação do vídeo {vid}.
  Equivale a {obj_video.obtem_atributos(vid,'criacao')}.
  Dá erro se {vid} é {None}."""
  return obj_video_IMP.obtem_data_de_upload(vid)

def obtem_dimensoes_do_arquivo(arq):
  """Localiza um video com nome "{arq}.mp4" no disco,
  e devolve as dimensões deste vídeo.
  Se tal vídeo não existe, devolve {None}.
  """
  return obj_video_IMP.obtem_dimensoes_do_arquivo(arq)

def busca_por_identificador(id_vid):
  """Localiza um video com identificador {id_vid} (uma string da forma
  "V-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_video.Classe}.
  Se {id_vid} é {None} ou tal vídeo não existe, devolve {None}."""
  return obj_video_IMP.busca_por_identificador(id_vid)

def busca_por_campo(campo, val):
  """Localiza todos os vídeos cujo {campo} seja {valor}. Retorna a lista de ids
  desses vídeos."""
  return obj_video_IMP.busca_por_campo(campo, val)  

def busca_por_arquivo(arq):
  """Localiza um video com nome "{arq}.mp4" na tabela de videos,
  e devolve o mesmo na forma de um objeto da classe {obj_video.Classe}.
  Se tal vídeo não existe, devolve {None}."""
  return obj_video_IMP.busca_por_arquivo(arq)

def busca_por_usuario(id_autor):
  """Localiza todos os vídeos do usuário com identificador {id_autor} (uma string da forma
  "U-{NNNNNNNN}").  Retorna uma lista de identificadores desses vídeos.
  Se {id_autor} é {None} ou o usuário não tem nenhum vídeo, devolve uma lista vazia."""
  return obj_video_IMP.busca_por_usuario(id_autor)

def muda_atributos(vid, atrs_mod_mem):
  """Recebe um dicionário Python {atrs_mod_mem} cujas chaves são um subconjunto
  dos nomes de atributos do vídeo (exceto o identificador). Troca os
  valores desses atributos no objeto {vid} da classe {obj_video.Classe}
  pelos valores correspondentes em {atrs_mod_mem}.  Também altera esses
  campos na base de dados. Os valores devem estar no formato de
  atributos na memória."""
  obj_video_IMP.muda_atributos(vid, atrs_mod_mem)

# DEPURAÇÂO

def verifica_criacao(vid, id_vid, atrs):
  """Faz testes de consistência básicos de um objeto {vid} de classe
  {obj_video.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(vid)} devolve
  o identificador esperado {id_vid}, {obtem_atributos(vid)} devolve 
  os atributos esperados {atrs}, e {busca_por_identificador(id_vid)}
  devolve o próprio {vid}.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_video_IMP.verifica_criacao(vid, id_vid, atrs)

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
