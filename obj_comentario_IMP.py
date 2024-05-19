import obj_raiz
import obj_comentario
import obj_usuario
import obj_video

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql

import util_identificador
import util_data
import util_inteiro
import util_booleano
import util_texto_de_comentario

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
    ( ( 'video',     obj_video.Classe,      'TEXT',    False ), # Video ao qual está associado.
      ( 'autor',     obj_usuario.Classe,    'TEXT',    False ), # Usuário que postou o comentário.
      ( 'pai',       obj_comentario.Classe, 'TEXT',    True  ), # Comentário pai, ou {None}.
      ( 'texto',     type("foo"),           'TEXT',    False ), # Texto do comentário.
      ( 'voto',      type(418),             'INTEGER', False ), # Opinião sobre vídeo ou pai.
      ( 'nota',      type(3.14),            'FLOAT',   False ), # Opinião sobre vídeo ou pai.
      ( 'bloqueado', type(False),           'INTEGER', False ), # O comentário foi bloqueado.
      ( 'data',      type("foo"),           'TEXT',    False ), # Data e hora da postagem.
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(atrs):
  global tabela
  if tabela.debug: mostra(0, f"  > obj_comentario.cria({str(atrs)}) ...")

  # Data de postagem:
  if not 'data' in atrs or atrs['data'] == None:
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

def obtem_objeto(com_id):
  global tabela
  com = obj_raiz.obtem_objeto(com_id, tabela, def_obj_mem)
  assert com == None or type(com) is obj_comentario.Classe
  return com

def obtem_atributos(com):
  global tabela
  assert com != None and isinstance(com, obj_comentario.Classe)
  return obj_raiz.obtem_atributos(com)

def obtem_atributo(com, chave):
  global tabela
  return obj_raiz.obtem_atributo(com, chave)

def obtem_autor(com):
  global tabela
  return obj_raiz.obtem_atributo(com, 'autor')

def busca_por_video(vid_id, sem_pai):
  global tabela
  unico = False
  if tabela.debug: sys.stderr.write("  > {obj_comentario_IMP.busca_por_video}: {vid_id} = " + f"{vid_id}\n");
  assert type(vid_id) is str
  unico = False
  if sem_pai:
    atrs = { 'video': vid_id, 'pai': None }
    lista_ids = obj_raiz.busca_por_campos(atrs, unico, tabela)
  else:
    lista_ids = obj_raiz.busca_por_campo('video', vid_id, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > ids encontrados = {lista_ids}\n");
  return lista_ids

def busca_por_campo(chave, val):
  global tabela
  lista_ids = obj_raiz.busca_por_campo(chave, val, False, tabela)
  return lista_ids

def busca_por_campos(args, unico):
  global tabela
  res = obj_raiz.busca_por_campos(args, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return res

def busca_por_autor(usr_id):
  global tabela
  if tabela.debug: sys.stderr.write("  > obj_comentario_IMP.busca_por_autor(" + f"{usr_id}" + ")\n");
  assert type(usr_id) is str
  unico = False
  lista_ids = obj_raiz.busca_por_campo('autor', usr_id, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return lista_ids

def busca_por_pai(pai_id):
  global tabela
  if tabela.debug: sys.stderr.write("  > obj_comentario_IMP.busca_por_pai(" + f"{pai_id}" + ")\n");
  assert type(pai_id) is str
  unico = False
  lista_ids = obj_raiz.busca_por_campo('pai', pai_id, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {str(lista_ids)}\n");
  return lista_ids

def busca_por_texto(frase):
  global tabela
  if tabela.debug: sys.stderr.write("  > obj_comentario_IMP.busca_por_texto(" + f"{frase}" + ")\n")
  assert type(frase) is str
  unico = False
  lista_ids = obj_raiz.busca_por_campos({ 'texto': "~%" + frase + "%" }, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > ids encontrados = {str(lista_ids)}\n");
  return lista_ids

def busca_por_data(data_ini, data_fin):
  global tabela
  if tabela.debug: sys.stderr.write("  > obj_comentario_IMP.busca_por_data(" + f"{data_ini}, {data_fin}" + ")\n");
  args_busca = { 'data': ( data_ini, data_fin, ) }
  unico = False
  lista_ids = obj_raiz.busca_por_campos(args_busca, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > ids encontrados = {str(lista_ids)}\n");
  return lista_ids
  
def recalcula_nota(com):#################################################
  global tabela
  notaOriginal = obj_comentario.obtem_atributo(com, "nota")
  votoOriginal = obj_comentario.obtem_atributo(com, "voto")
  ##sys.stderr.write("!!! função {obj_comentario.recalcula_nota} ainda não foi implementada !!!\n")
  ##nota = 2.0
  nota = (2.0*4.0 + votoOriginal*notaOriginal**2)/(4.0+notaOriginal**2)
  return nota

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
      ( "C-00000009", "V-00000001", "U-00000001", "C-00000005", "Larga mão dessa!\nCoisa feia!\nRespeite os mais bodosos. Se não tem coisa melhor a fazer, vá ver se estou na esquina...", ),
      ( "C-00000010", "V-00000001", "U-00000004", "C-00000002", "Interessante...\nPorém, na Bessarábia os elefantes dos sátrapas eram tatuados com hieróglifos, não com emojis.\nÉ fake!", ),
      ( "C-00000011", "V-00000001", "U-00000002", "C-00000005", "Levante deste camastralho!!!", ),
      ( "C-00000012", "V-00000001", "U-00000005", "C-00000005", "Boa tarde! Sou a viúva do Príncipe Ngwande de Timbuktu e preciso de sua ajuda.", ),
      ( "C-00000013", "V-00000001", "U-00000005", "C-00000005", "Boa tarde! Sou a viúva do Príncipe Ngwande de Timbuktu e preciso de sua ajuda.", ),
      ( "C-00000014", "V-00000001", "U-00000005", "C-00000005", "Boa tarde! Sou a viúva do Príncipe Ngwande de Timbuktu e preciso de sua ajuda.", ),
      ( "C-00000015", "V-00000001", "U-00000005", "C-00000005", "Boa tarde! Sou a viúva do Príncipe Ngwande de Timbuktu e preciso de sua ajuda.", ),
      ( "C-00000016", "V-00000001", "U-00000005", "C-00000005", "Boa tarde! Sou a viúva do Príncipe Ngwande de Timbuktu e preciso de sua ajuda.", ),
    ]
  for com_id_esp, vid_id, autor_id, pai_id, texto in lista_atrs:
    vid = obj_video.obtem_objeto(vid_id)
    autor = obj_usuario.obtem_objeto(autor_id)
    pai = obj_comentario.obtem_objeto(pai_id)
    dia = com_id_esp[-2:]
    data = "2024-01-" + dia + " 08:33:25 UTC"
    bloqueado = False
    voto = ((7 + int(vid_id[-3:]))**2//11) % 5
    nota = (((7 + int(vid_id[-3:]))**2//11) % 401) / 100.0
    atrs = { 
        'video': vid, 
        'autor': autor, 
        'pai': pai, 
        'data': data,
        'texto': texto,
        'voto': voto,
        'nota': nota,
        'bloqueado': bloqueado,
      }
    com = cria(atrs)
    assert com != None and type(com) is obj_comentario.Classe
    com_id_atu = obj_comentario.obtem_identificador(com)
    texto_atu = obj_comentario.obtem_atributo(com,'texto')
    if verb: sys.stderr.write("  comentário %s = \"%s\" criado\n" % (com_id_atu, texto_atu))
    assert com_id_atu == com_id_esp # Identificador é o esperado.
    assert texto_atu == texto   # O texto foi guardado corretamente.
  return

def verifica_criacao(com, com_id, atrs):
  return obj_raiz.verifica_criacao(com, obj_comentario.Classe, com_id, atrs, None, tabela, def_obj_mem)

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
  
  erros = [];
  
  # Validade dos campos fornecidos:
  if 'video' in atrs:
    vid_fin = atrs['video']
    if type(vid_fin) is not obj_video.Classe:
      erros += [ f"O campo 'video' = \"{vid_fin}\" deve ser um objeto vídeo" ]
  elif com != None:
    vid_fin = obj_comentario.obtem_atributo(com, 'video')

  if 'autor' in atrs:
    autor_fin = atrs['autor']
    if type(autor_fin) is not obj_usuario.Classe:
      erros += [ f"O campo 'autor' = \"{autor_fin}\" deve ser um objeto usuário" ]
  elif com != None:
    autor_fin = obj_comentario.obtem_atributo(com, 'autor')

  if 'data' in atrs:
    data_fin = atrs['data']
    erros += util_data.valida('data', data_fin, False)
  elif com != None:
    data_fin = obj_comentario.obtem_atributo(com, 'data')
  
  if 'pai' in atrs:
    pai_fin = atrs['pai'];
    if pai_fin != None and type(pai_fin) is not obj_comentario.Classe:
      erros.append( f"O campo 'pai' = \"{pai_fin}\" deve ser {None} ou um objeto comentario" )
  elif com != None:
    pai_fin = obj_comentario.obtem_atributo(com, 'pai')
  
  if pai_fin != None:
    vid_pai = obj_comentario.obtem_atributo(pai_fin, 'video')
    if vid_pai != vid_fin: 
      erros.append(f"O video do pai = \"{vid_pai}\" não é o mesmo deste comentário = \"{vid_fin}\"")
    
  if 'voto' in atrs:
    voto_fin = atrs['voto']
    if not type(voto_fin) is int or voto_fin < 0 or voto_fin > 4:
      erros.append(f"O campo 'voto' = \"{voto_fin}\" deve ser inteiro em {'{0..4}'}")
  elif com != None:
    voto_fin = obj_comentario.obtem_atributo(com, 'voto')
    
  if 'nota' in atrs:
    nota_fin = atrs['nota']
    nota_min = 0.0
    nota_max = 4.0
    if not isinstance(nota_fin, float):
      erros.append(f"O atributo 'nota' = \"{nota_fin}\" não é um {'{float}'}")
    elif nota_fin < nota_min or nota_fin > nota_max:
      erros.append(f"O atributo 'nota' = \"{nota_fin}\" está fora da faixa [{nota_min:.0f} _ {nota_max:.0f}]")
  elif com != None:
    nota_fin = obj_comentario.obtem_atributo(com, 'nota')
     
  if 'bloqueado' in atrs:
    bloqueado_fin = atrs['bloqueado']
    erros += util_booleano.valida('bloqueado', bloqueado_fin, False)
  elif com != None:
    bloqueado_fin = obj_comentario.obtem_atributo(com, 'bloqueado')
     
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in tabela.colunas:
    if chave in atrs:
      nargs += 1
    elif com == None:
      erros.append(f"O campo '{chave}' é obrigatório")

  if nargs < len(atrs):
    # Não deveria ocorrer:
    erro_prog(f"Atributos espúrios em \"{atrs}\"")

  return erros

def def_obj_mem(com, com_id, atrs_SQL):
  """Se {com} for {None}, cria um novo objeto da classe {obj_comentario.Classe} com
  identificador {com_id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {com} não é {None}, deve ser um objeto da classe {obj_comentario.Classe}; nesse
  caso a função altera os atributos de {com} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0,"obj_comentario_IMP.def_obj_mem(" + str(com) + ", " + com_id + ", " + str(atrs_SQL) + ") ...")
  if com == None:
    com = cria_obj_mem(com_id, atrs_SQL)
  else:
    assert com.id == com_id
    modifica_obj_mem(com, atrs_SQL)
  if tabela.debug: mostra(2,"com = " + str(com))
  return com
    
def cria_obj_mem(com_id, atrs_SQL):
  """Cria um novo objeto da classe {obj_comentario.Classe} com
  identificador {com_id} e atributos {atrs_SQL}, tais como extraidos
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

  com = obj_comentario.Classe(com_id, atrs)
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

def obtem_conversa(raizes, max_coms, max_nivel):
  """
  O parâmetro {max_coms} delimita o maximo de comentários a serem retornados na conversa, sem contabilizar as raizes,
  enquanto {max_nivel} delimita até qual nivel da arvore os comentários serão retornados.
  """
  global tabela
  if raizes == None: raizes = [] # Simplify.
  assert isinstance(raizes, list) or isinstance(raizes, tuple)
  conversa = []

  coms_faltando = max_coms
  
  for com_id in raizes:
    if coms_faltando <= 0:
      conversa.append([com_id])
      # Para de procurar mais comentarios, mas adiciona o resto das raizes caso existam
      continue
    com = obj_comentario.obtem_objeto(com_id)
    if com == None: erro_prog(f"comentario {com_id} não existe")
    arv, resto = obtem_arvore(com, coms_faltando, max_nivel - 1)
    coms_faltando = resto
    conversa.append(arv)

  return conversa

def obtem_conversa_com_resto(raizes, max_coms, max_nivel):
  """
  Retorna a quantidade de comentarios que ainda podem ser buscados, junto da conversa.
  """
  global tabela
  if raizes == None: raizes = [] # Simplify.
  assert isinstance(raizes, list) or isinstance(raizes, tuple)
  conversa = []

  coms_faltando = max_coms
  
  for com_id in raizes:
    if coms_faltando <= 0: 
      conversa.append([com_id])
      break
    com = obj_comentario.obtem_objeto(com_id)
    if com == None: erro_prog(f"comentario {com_id} não existe")
    arv, resto = obtem_arvore(com, coms_faltando, max_nivel - 1)
    coms_faltando = resto
    conversa.append(arv)

  return conversa, coms_faltando

def obtem_arvore(com, max_coms, max_nivel):
  global tabela
  assert com == None or isinstance(com, obj_comentario.Classe)
  if com == None: return None
  com_id = obj_comentario.obtem_identificador(com)
  
  arv = [ com_id ]

  if max_nivel < 0:
    return arv, max_coms
  
  lista_ids_filhos = busca_por_pai(com_id)

  coms_faltando = max_coms

  if lista_ids_filhos != None:
    for id_filho in lista_ids_filhos:
      # Para execução se alcançou o limite de comentarios
      if coms_faltando <= 0: break
      subarvs, resto = obtem_conversa_com_resto([id_filho], coms_faltando - 1, max_nivel)
      coms_faltando = resto
      arv += subarvs

  return arv, coms_faltando
