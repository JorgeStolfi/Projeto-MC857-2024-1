import obj_comentario_IMP

class Classe(obj_comentario_IMP.Classe_IMP):
  """
  Um objeto desta classe representa um comentário associado
  a um video.  É uma subclasse de {Objeto}.
  
  O identificador de um comentário é uma string da forma
  "C-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela (vide abaixo)
  formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  contém os seguintes campos:

    'video'          (obr) objeto da classe {obj_video.Classe}.
    'autor'          (obr) objeto da classe {obj_usuario.Classe}.
    'data'           (obr) data de postagem, formato "yyyy-mm-dd hh:mm:ss UTC".
    'pai'            (fac) objeto da classe {obj_comentario.Classe}.
    'texto'          (obr) string do comentário.
   
  Atributos marcados (obr) não podem ser {None}, 
  os marcados (fac) podem ser {None}.
    
  Outros atributos, como {votos} ou {removido}, poderão ser
  acrescentados no futuro. Todos os campos podem ser alterados, exceto o
  índice (e portanto o identificador).
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada comentário no sistema é representado por uma linha na tabela
  "comentarios" da base SQL em disco. Apenas algumas dessas linhas são
  representadas também na memória por objetos da classe
  {obj_comentario.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do comentário.
  """
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela "comentarios" na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {db_base_sql.conecta}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  obj_comentario_IMP.inicializa_modulo(limpa)

def cria(atrs):
  """Cria um novo objeto da classe {obj_comentario.Classe}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de comentários da base de dados.
  Atribui um identificador único ao comentário, derivado do seu índice na tabela.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return obj_comentario_IMP.cria(atrs)

def muda_atributos(com, atrs_mod_mem):
  """Modifica alguns atributos do objeto {com} da classe {obj_comentario.Classe},
  registrando as alterações na base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do comentário (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.
  
  Esta função é só um boneco por enquanto pois os atributos 
  de um objeto comentário não podem ser alterados depois que o mesmo
  foi criado.  No futuro pode haver campos alteráveis, como {censurado}
  ou contador de "likes".
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_comentario_IMP.muda_atributos(com, atrs_mod_mem)

def obtem_identificador(com):
  """Devolve o identificador 'C-{NNNNNNNN}' do comentario."""
  return obj_comentario_IMP.obtem_identificador(com)

def obtem_atributos(com):
  """Retorna um dicionário Python que é uma cópia dos atributos do comentário,
  exceto identificador."""
  return obj_comentario_IMP.obtem_atributos(com)

def obtem_atributo(com, chave):
  """Retorna o atributo do comentário {com} com a {chave} dada. 
  Equivale a {obtem_atributos(com)[chave]}"""
  return obj_comentario_IMP.obtem_atributo(com, chave)

def busca_por_identificador(id_com):
  """Localiza um comentario com identificador {id_com} (uma string da forma
  "C-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_comentario.Classe}.
  Se {id_com} é {None} ou tal comentário não existe, devolve {None}."""
  return obj_comentario_IMP.busca_por_identificador(id_com)

def busca_por_video(id_vid):
  """Localiza comentários associados ao video com identificador {id_vid}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o usuário não postou nenhum comentário."""
  return obj_comentario_IMP.busca_por_video(id_vid)

def busca_por_autor(id_usr):
  """Localiza comentários postados pelo usuário com identifiador {id_usr}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o usuário não postou nenhum comentário."""
  return obj_comentario_IMP.busca_por_autor(id_usr)

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(com, id_com, atrs):
  """Faz testes de consistência básicos de um objeto {com} de classe 
  {obj_comentario.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(com)} devolve
  o identificador esperado {id_com}, {obtem_atributos(com)} devolve 
  os atributos esperados {atrs}, e {busca_por_identificador(id_com)}
  devolve o próprio {com}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_comentario_IMP.verifica_criacao(com, id_com, atrs)

def cria_testes(verb):
  """Limpa a tabela de comentários com {inicializa(True)}, e cria pelo menos três comentários
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {db_base_sql.conecta}.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado.""" 
  obj_comentario_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  obj_comentario_IMP.liga_diagnosticos(val)
