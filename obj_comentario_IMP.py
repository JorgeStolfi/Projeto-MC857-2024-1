import obj_raiz
import obj_comentario
import obj_usuario
import obj_video

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql
import util_identificador
import util_valida_campo
import time

from util_erros import ErroAtrib, erro_prog, mostra

from datetime import datetime, timezone
import sys

# Uma instância de {db_obj_tabela} descrevendo a tabela de comentários:
tabela = None

# Definição interna da classe {obj_comentario.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id, atrs):
    obj_raiz.Classe.__init__(self, id, atrs)

# Implementação das funções da interface:

def inicializa_modulo(limpa):
  global tabela

  # Só pode inicializar uma vez:
  if tabela != None: return
  
  nome_tb = "comentarios"           # Nome da tabela na base de dados.
  letra_tb = "C"                    # Prefixo dos identificadores de comentários
  classe = obj_comentario.Classe # Classe dos objetos (linhas da tabela) na memória.

  # Descrição das colunas da tabela na base de dados: 
  # Vide parâmetro {cols} de {db_obj_tabela.cria_tabela}.
  colunas = \
    ( ( 'video',  obj_video.Classe,      'TEXT', False ), # Video ao qual está associado.
      ( 'autor',  obj_usuario.Classe,    'TEXT', False ), # Usuário que postou o comentário.
      ( 'data',   type("foo"),           'TEXT', False ), # Data e hora da postagem.
      ( 'pai',    obj_comentario.Classe, 'TEXT', True  ), # Comentário pai, ou {None}.
      ( 'texto',  type("foo"),           'TEXT', False ), # Texto do comentário.
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(atrs):
  global tabela
  if tabela.debug: mostra(0, f"  > obj_comentario.cria({str(atrs)}) ...")

  # Data de postagem:
  if 'data' in atrs: raise ErroAtrib("data não pode ser especificada")
  data = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
  atrs['data'] = data

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  com = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(com) is obj_comentario.Classe
  if tabela.debug: sys.stderr.write(f"  < {obj_comentario.cria}\n")
  return com

def muda_atributos(com, mods_mem):
  global tabela
  if tabela.debug: sys.stderr.write("  > {obj_comentario.muda_atributos} {str(mods_mem)}:\n")
  assert com != None and isinstance(com, obj_comentario.Classe)
  
  erros = valida_atributos(com, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  if tabela.debug: sys.stderr.write(f"    > com antes = {str(com)}\n")
  obj_raiz.muda_atributos(com, mods_mem, tabela, def_obj_mem)
  if tabela.debug: sys.stderr.write(f"    > com depois = {str(com)}\n")
  
  if tabela.debug: sys.stderr.write(f"  < {obj_comentario.muda_atributos}\n")
  return

def obtem_identificador(com):
  global tabela
  assert com != None and isinstance(com, obj_comentario.Classe)
  return obj_raiz.obtem_identificador(com)

def obtem_atributos(com):
  global tabela
  assert com != None and isinstance(com, obj_comentario.Classe)
  return obj_raiz.obtem_atributos(com)

def obtem_atributo(com, chave):
  global tabela
  return obj_raiz.obtem_atributo(com, chave)

def obtem_objeto(id_com):
  global tabela
  com = obj_raiz.obtem_objeto(id_com, tabela, def_obj_mem)
  assert com == None or type(com) is obj_comentario.Classe
  return com

def busca_por_video(id_vid, sem_pai):
  global tabela
  unico = False
  if tabela.debug: sys.stderr.write("  > {obj_comentario_IMP.busca_por_video}: {id_vid} = " + f"{id_vid}\n");
  assert type(id_vid) is str
  unico = False
  if sem_pai:
    atrs = { 'video': id_vid, 'pai': None }
    lista_ids = obj_raiz.busca_por_campos(atrs, unico, tabela)
  else:
    lista_ids = obj_raiz.busca_por_campo('video', id_vid, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > ids encontrados = {lista_ids}\n");
  return lista_ids

def busca_por_autor(id_usr):
  global tabela
  if tabela.debug: sys.stderr.write("  > {obj_comentario_IMP.busca_por_nome}: {id_usr} = " + f"{id_usr}\n");
  assert type(id_usr) is str
  unico = False
  lista_ids = obj_raiz.busca_por_campo('autor', id_usr, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return lista_ids

def busca_por_pai(id_pai):
  global tabela
  if tabela.debug: sys.stderr.write("  > {obj_comentario_IMP.busca_por_pai}: {id_pai} = " + f"{id_pai}\n");
  assert type(id_pai) is str
  unico = False
  lista_ids = obj_raiz.busca_por_campo('pai', id_pai, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return lista_ids

def busca_por_texto(texto):
  global tabela
  if tabela.debug: sys.stderr.write("  > {obj_comentario_IMP.busca_por_texto}: {texto} = " + f"{texto}\n")
  assert type(texto) is str
  unico = False
  texto += "%" + texto + "%"
  lista_ids = obj_raiz.busca_por_campos({'texto':texto}, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return lista_ids

def busca_por_data(data):
  # !!! BUSCA POR DATA AINDA NÃO IMPLEMENTADA !!!
  lista_ids = []
  return lista_ids
  
def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)
  
def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  lista_atrs = \
    [ 
      ( "C-00000001", "V-00000001", "U-00000001", None,         "Supimpa!\nDeveras!", ),
      ( "C-00000002", "V-00000001", "U-00000002", "C-00000001", "Né não! Acho... Talvez...", ),
      ( "C-00000003", "V-00000002", "U-00000002", None,         "Falta sal.", ),
      ( "C-00000004", "V-00000003", "U-00000003", None,         "Soberbo!", ),
      ( "C-00000005", "V-00000001", "U-00000003", "C-00000002", "É sim!", ),
      ( "C-00000006", "V-00000003", "U-00000004", None,         "Supercílio! " + "k"*60, ),
      ( "C-00000007", "V-00000001", "U-00000004", "C-00000002", "Batata!", ),
      ( "C-00000008", "V-00000001", "U-00000002", None,         "Inefável!", ),
      ( "C-00000009", "V-00000001", "U-00000001", "C-00000005", "Larga mão dessa!\nCoisa feia!\nRespeite os mais bodosos...", ),
    ]
  for id_com, id_vid, id_autor, id_pai, texto in lista_atrs:
    vid = obj_video.obtem_objeto(id_vid)
    autor = obj_usuario.obtem_objeto(id_autor)
    pai = obj_comentario.obtem_objeto(id_pai)
    atrs = { 'video': vid, 'autor': autor, 'pai': pai, 'texto': texto }
    com = cria(atrs)
    assert com != None and type(com) is obj_comentario.Classe
    id_com_atu = obj_comentario.obtem_identificador(com)
    texto_atu = obj_comentario.obtem_atributo(com,'texto')
    if verb: sys.stderr.write("  comentário %s = \"%s\" criado\n" % (id_com_atu, texto_atu))
    assert id_com_atu == id_com # Identificador é o esperado.
    assert texto_atu == texto   # O texto foi guardado corretamente.
  return

def verifica_criacao(com, id_com, atrs):
  return obj_raiz.verifica_criacao(com, obj_comentario.Classe, id_com, atrs, None, tabela, def_obj_mem)

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(com, atrs):
  """Faz validações específicas nos atributos {atrs}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {com} é {None}, supõe que um novo comentário está sendo criado. Se {com}
  não é {None}, deve ser um objeto de tipo {obj_comentario.Classe},
  e supõe que {atrs} sao alterações a aplicar nesse
  comentário. """
  global tabela
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'video' in atrs:
    vid_fin = atrs['video']
    if type(vid_fin) is not obj_video.Classe:
      erros += [ "campo 'video' = \"%s\" deve ser um {obj_video}" % str(vid_fin) ]
  else:
    vid_fin = obj_comentario.obtem_atributo(com, 'video')

  if 'autor' in atrs:
    autor_fin = atrs['autor']
    if type(autor_fin) is not obj_usuario.Classe:
      erros += [ "campo 'autor' = \"%s\" deve ser um objeto usuario" % str(autor_fin) ]
  else:
    autor_fin = obj_comentario.obtem_atributo(com, 'autor')

  if 'data' in atrs:
    data_fin = atrs['data']
    erros += util_valida_campo.data('data', data_fin, False)
  else:
    data_fin = obj_comentario.obtem_atributo(com, 'data')
  
  if 'pai' in atrs:
    pai_fin = atrs['pai'];
    if pai_fin != None and type(pai_fin) is not obj_comentario.Classe:
      erros += [ "campo 'pai' = \"%s\" deve ser {None} ou um {obj_comentario}" % str(pai_fin) ]
  else:
    pai_fin = obj_comentario.obtem_atributo(com, 'pai')
    
  if pai_fin != None:
    vid_pai = obj_comentario.obtem_atributo(pai_fin, 'video')
    if vid_pai != vid_fin: 
      erros.append(f"videos diferentes pai = {str(vid_pai)} com = {str(vid_fin)}")
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in tabela.colunas:
    if chave in atrs:
      nargs += 1
    elif com == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs} = " + str(atrs) + "")

  return erros

def def_obj_mem(com, id_com, atrs_SQL):
  """Se {com} for {None}, cria um novo objeto da classe {obj_comentario.Classe} com
  identificador {id_com} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {com} não é {None}, deve ser um objeto da classe {obj_comentario.Classe}; nesse
  caso a função altera os atributos de {com} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0,"obj_comentario_IMP.def_obj_mem(" + str(com) + ", " + id_com + ", " + str(atrs_SQL) + ") ...")
  if com == None:
    com = cria_obj_mem(id_com, atrs_SQL)
  else:
    assert com.id == id_com
    modifica_obj_mem(com, atrs_SQL)
  if tabela.debug: mostra(2,"com = " + str(com))
  return com
    
def cria_obj_mem(id_com, atrs_SQL):
  """Cria um novo objeto da classe {obj_comentario.Classe} com
  identificador {id_com} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global tabela

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, False, db_tabelas_do_sistema.identificador_para_objeto)
  if tabela.debug: mostra(2,"criando objeto, atrs = " + str(atrs))
  assert type(atrs) is dict
  if len(atrs) != len(tabela.colunas):
    erro_prog("numero de atributos = " + str(len(atrs)) + " devia ser " + str(len(tabela.colunas)))

  com = obj_comentario.Classe(id_com, atrs)
  return com
  
def modifica_obj_mem(com, atrs_mod_SQL):
  """O parâmetro {com} deve ser um objeto da classe {obj_comentario.Classe}; nesse
  caso a função altera os atributos de {com} conforme especificado em
  {atrs_mod_SQL}.  A entrada correspondente da base de dados *NÃO* é alterada.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela

  # Converte atributos para formato na memória. Pode ser subconjunto:
  atrs_mod_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_mod_SQL, tabela.colunas, True, db_tabelas_do_sistema.identificador_para_objeto)
  if tabela.debug: mostra(2,"modificando objeto, atrs_mod_mem = " + str(atrs_mod_mem))
  assert type(atrs_mod_mem) is dict
  if len(atrs_mod_mem) > len(tabela.colunas):
    erro_prog("numero de atributos a alterar = " + str(len(atrs_mod_mem)) + " excessivo")

  # Modifica os atributos:
  for chave, val_mem in atrs_mod_mem.items():
    if not chave in com.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = com.atrs[chave]
    if val_mem != None and val_velho != None and (not type(val_velho) is type(val_mem)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    com.atrs[chave] = val_mem
  return com

def obtem_conversa(raizes):
  global tabela
  if raizes == None: raizes = [] # Simplify.
  assert isinstance(raizes, list) or isinstance(raizes, tuple)
  
  conversa = [].copy()
  
  for id_com in raizes:
    com = obj_comentario.obtem_objeto(id_com)
    if com == None: erro_prog(f"comentario {id_com} não existe")
    arv = obtem_arvore(com)
    conversa.append(arv)
    
  return conversa

def obtem_arvore(com):
  global tabela
  assert com == None or isinstance(com, obj_comentario.Classe)
  if com == None: return None
  id_com = obj_comentario.obtem_identificador(com)
  
  arv = [ id_com ]
  
  lista_ids_filhos = busca_por_pai(id_com)

  if lista_ids_filhos != None:
    subarvs = obtem_conversa(lista_ids_filhos)
    arv += subarvs

  return arv
