# Implementação do módulo {comentario} e da classe {obj_comentario.Classe}.

import obj_raiz
import obj_usuario
import obj_video
import obj_sessao
import obj_comentario

import db_tabela_generica
import db_tabelas
import db_conversao_sql
import util_identificador
import util_valida_campo
from util_testes import ErroAtrib, erro_prog, mostra
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "comentarios"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {obj_comentario.Classe} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "C"
  # Prefixo dos identificadores de comentários

colunas = None
  
com_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {obj_comentario.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id, atrs):
    global cache, nome_tb, letra_tb, colunas
    obj_raiz.Classe.__init__(self, id, atrs)

# Implementação das funções:

def inicializa_modulo(limpa):
  global cache, nome_tb, letra_tb, colunas
  # Descrição das colunas da tabela na base de dados: 
  # Vide parâmetro {cols} de {db_tabela_generica.cria_tabela}.
  colunas = \
    (
      ( 'video',         obj_video.Classe,      'TEXT',    False ), # Video ao qual está associado.
      ( 'autor',         obj_usuario.Classe,    'TEXT',    False ), # Usuário que postou o comentário.
      ( 'data',          type("foo"),           'TEXT',    False ), # Data e hora da postagem.
      ( 'pai',           obj_comentario.Classe, 'TEXT',    True  ), # Comentário pai, ou {None}.
      ( 'texto',         type("foo"),           'TEXT',    False ), # Texto do comentário.
    )
  if limpa:
    db_tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    db_tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs_mem):
  global cache, nome_tb, letra_tb, colunas
  if com_debug: mostra(0,"obj_comentario_IMP.cria({str(atrs_mem)}) ...")

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  com = obj_raiz.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(com) is obj_comentario.Classe
  return com

def muda_atributos(com, mods_mem):
  global cache, nome_tb, letra_tb, colunas
  if com_debug: sys.stderr.write("  > {obj_comentario.muda_atributos}:\n")
  
  erros = valida_atributos(com, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  if com_debug: sys.stderr.write(f"    > com antes = {str(com)} mods_mem = {str(mods_mem)}\n")
  obj_raiz.muda_atributos(com, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  if com_debug: sys.stderr.write(f"    > com depois = {str(com)}\n")
  return

def obtem_identificador(com):
  global cache, nome_tb, letra_tb, colunas
  assert com != None
  return obj_raiz.obtem_identificador(com)

def obtem_atributos(com):
  global cache, nome_tb, letra_tb, colunas
  return obj_raiz.obtem_atributos(com)

def obtem_atributo(com, chave):
  global cache, nome_tb, letra_tb, colunas
  return obj_raiz.obtem_atributo(com,chave)

def busca_por_identificador(id_com):
  global cache, nome_tb, letra_tb, colunas
  com = obj_raiz.busca_por_identificador(id_com, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert com == None or type(com) is obj_comentario.Classe
  return com

def busca_por_video(id_vid):
  global cache, nome_tb, letra_tb, colunas
  unico = False
  if com_debug: sys.stderr.write(f"  > {obj_comentario_IMP.busca_por_video}: id_vid = {id_vid}\n");
  assert type(id_vid) is str
  id_com = obj_raiz.busca_por_campo('video', id_vid, unico, cache, nome_tb, letra_tb, colunas)
  if com_debug: sys.stderr.write(f"    > id encontrado = {id_com}\n");
  return id_com

def busca_por_autor(id_usr):
  global cache, nome_tb, letra_tb, colunas
  unico = False
  if com_debug: sys.stderr.write(f"  > {obj_comentario_IMP.busca_por_nome}: id_usr = {id_usr}\n");
  assert type(id_usr) is str
  lista_ids = obj_raiz.busca_por_campo('autor', id_usr, unico, cache, nome_tb, letra_tb, colunas)
  if com_debug: sys.stderr.write(f"    > lista de ids encontrada = {','.join(lista_ids)}\n");
  return lista_ids
  
def cria_testes(verb):
  global cache, nome_tb, letra_tb, colunas
  inicializa_modulo(True)
  lista_atrs = \
    [ 
      ( "C-00000001", "V-00000001", "U-00000001", "2024-04-05 08:00:00 UTC", None,         "Supimpa!", ),
      ( "C-00000002", "V-00000001", "U-00000002", "2024-04-05 08:10:00 UTC", "C-00000001", "Né não!", ),
      ( "C-00000003", "V-00000002", "U-00000002", "2024-04-05 08:20:00 UTC", None,         "Falta sal.", ),
      ( "C-00000004", "V-00000003", "U-00000003", "2024-04-05 08:30:00 UTC", None,         "Soberbo!", ),
      ( "C-00000005", "V-00000001", "U-00000003", "2024-04-05 08:40:00 UTC", "C-00000002", "É sim!", ),
      ( "C-00000006", "V-00000003", "U-00000003", "2024-04-05 08:50:00 UTC", None,         "Supercílio!", ),
    ]
  for id_com, id_vid, id_autor, data, id_pai, texto in lista_atrs:
    vid = obj_video.busca_por_identificador(id_vid)
    autor = obj_usuario.busca_por_identificador(id_autor)
    pai = obj_comentario.busca_por_identificador(id_pai)
    atrs = { 'video': vid, 'autor': autor, 'data': data, 'pai': pai, 'texto': texto }
    com = cria(atrs)
    assert com != None and type(com) is obj_comentario.Classe
    id_com_atu = obj_comentario.obtem_identificador(com)
    texto_atu = obj_comentario.obtem_atributo(com,'texto')
    if verb: sys.stderr.write("  comentário %s = \"%s\" criado\n" % (id_com_atu, texto_atu))
    assert id_com_atu == id_com # Identificador é o esperado.
    assert texto_atu == texto   # O texto foi guardado corretamente.
  return

def verifica_criacao(com, id_com, atrs):
  return obj_raiz.verifica_criacao(com, obj_comentario.Classe, id_com, atrs, None, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def liga_diagnosticos(val):
  global com_debug
  com_debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(com, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {com} é {None}, supõe que um novo comentário está sendo criado. Se {com}
  não é {None}, deve ser um objeto de tipo {obj_comentario.Classe},
  e supõe que {atrs_mem} sao alterações a aplicar nesse
  comentário. 
  
  O comentário pai, se existir, deve ter data estritamente menor que 
  a data de {com}."""
  global cache, nome_tb, letra_tb, colunas
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'video' in atrs_mem:
    vid_fin = atrs_mem['video']
    if type(vid_fin) is not obj_video.Classe:
      erros += [ "campo 'video' = \"%s\" deve ser um {obj_video}" % str(vid_fin) ]
  else:
    vid_fin = obj_comentario.obtem_atributo(com, 'video')

  if 'autor' in atrs_mem:
    autor_fin = atrs_mem['autor']
    if type(autor_fin) is not obj_usuario.Classe:
      erros += [ "campo 'autor' = \"%s\" deve ser um objeto usuario" % str(autor_fin) ]
  else:
    autor_fin = obj_comentario.obtem_atributo(com, 'autor')

  if 'data' in atrs_mem:
    data_fin = atrs_mem['data']
    erros += util_valida_campo.data('data', data_fin, False)
  else:
    data_fin = obj_comentario.obtem_atributo(com, 'data')
  
  if 'pai' in atrs_mem:
    pai_fin = atrs_mem['pai'];
    if pai_fin != None and type(pai_fin) is not obj_comentario.Classe:
      erros += [ "campo 'pai' = \"%s\" deve ser {None} ou um {obj_comentario}" % str(pai_fin) ]
  else:
    pai_fin = obj_comentario.obtem_atributo(com, 'pai')
    
  if pai_fin != None:
    vid_pai = obj_comentario.obtem_atributo(pai_fin, 'video')
    if vid_pai != vid_fin: 
      erros.append(f"videos diferentes pai = {str(vid_pai)} com = {str(vid_fin)}")
      
    data_pai = obj_comentario.obtem_atributo(pai_fin, 'data')
    if data_pai >= data_fin: 
      erros.append(f"comentarios fora de ordem cronológica {data_pai} {data_fin}")
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs_mem} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs_mem:
      nargs += 1
    elif com == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs_mem):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs_mem} = " + str(atrs_mem) + "")

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
  global cache, nome_tb, letra_tb, colunas
  if com_debug: mostra(0,"obj_comentario_IMP.def_obj_mem(" + str(com) + ", " + id_com + ", " + str(atrs_SQL) + ") ...")
  if com == None:
    com = cria_obj_mem(id_com, atrs_SQL)
  else:
    assert com.id == id_com
    modifica_obj_mem(com, atrs_SQL)
  if com_debug: mostra(2,"com = " + str(com))
  return com
    
def cria_obj_mem(id_com, atrs_SQL):
  """Cria um novo objeto da classe {obj_comentario.Classe} com
  identificador {id_com} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global cache, nome_tb, letra_tb, colunas

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, db_tabelas.identificador_para_objeto)
  if com_debug: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))

  com = obj_comentario.Classe(id_com, atrs_mem)
  return com
  
def modifica_obj_mem(com, atrs_mod_SQL):
  """O parâmetro {com} deve ser um objeto da classe {obj_comentario.Classe}; nesse
  caso a função altera os atributos de {com} conforme especificado em
  {atrs_mod_SQL}.  A entrada correspondente da base de dados *NÃO* é alterada.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas

  # Converte atributos para formato na memória. Pode ser subconjunto:
  atrs_mod_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_mod_SQL, colunas, True, db_tabelas.identificador_para_objeto)
  if com_debug: mostra(2,"modificando objeto, atrs_mod_mem = " + str(atrs_mod_mem))
  assert type(atrs_mod_mem) is dict
  if len(atrs_mod_mem) > len(colunas):
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
