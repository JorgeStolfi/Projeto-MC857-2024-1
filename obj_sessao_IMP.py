import obj_raiz
import obj_sessao
import obj_usuario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql
import util_identificador
import util_valida_campo 

from util_erros import ErroAtrib, erro_prog, mostra

from datetime import datetime, timezone
import sys

# Uma instância de {db_obj_tabela} descrevendo a tabela de sessões:
tabela = None

# Definição interna da classe {obj_sessao.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id, atrs):
    obj_raiz.Classe.__init__(self, id, atrs)

# Implementação das funções da interface:

def inicializa_modulo(limpa):
  global tabela

  # Só pode inicializar uma vez:
  if tabela != None: return

  nome_tb = "sessoes"        # Nome da tabela na base de dados.
  letra_tb = "S"             # Prefixo dos identificadores de sessões
  classe = obj_sessao.Classe # Classe dos objetos (linhas da tabela) na memória.

  # Descrição das colunas da tabela na base de dados: 
  # Vide parâmetro {cols} de {db_obj_tabela.cria_tabela}.
  colunas = \
    (
      ( 'usr',     obj_usuario.Classe, 'TEXT',    False ), # Objeto/id do usuário logado na sessão.
      ( 'criacao', type("foo"),        'TEXT',    False ), # Momento de criação da sessão.
      ( 'aberta',  type(False),        'INTEGER', False ), # Estado da sessao (1 = aberta).
      ( 'cookie',  type("foo"),        'TEXT',    False ), # Cookie da sessao.
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(usr, cookie):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_sessao.cria}({str(usr)},{str(cookie)})\n")

  criacao = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
  atrs = {
    'usr': usr,
    'criacao': criacao,
    'aberta': True,
    'cookie': cookie
  }

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  ses = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(ses) is obj_sessao.Classe
  if tabela.debug: sys.stderr.write(f"  < {obj_sessao.cria}\n")
  return ses

def muda_atributos(ses, mods_mem):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_sessao.muda_atributos} {str(mods_mem)}\n")
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  
  erros = valida_atributos(ses, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  if tabela.debug: sys.stderr.write(f"    ses antes = {str(ses)}\n")
  obj_raiz.muda_atributos(ses, mods_mem, tabela, def_obj_mem)
  if tabela.debug: sys.stderr.write(f"    ses depois = {str(ses)}\n")

  if tabela.debug: sys.stderr.write(f"  < {obj_sessao.muda_atributos}\n")
  return

def obtem_identificador(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_identificador(ses)

def obtem_atributos(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributos(ses)

def obtem_atributo(ses, chave):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributo(ses, chave)

def obtem_usuario(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributo(ses, 'usr')

def obtem_data_de_criacao(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributo(ses, 'criacao')

def aberta(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributo(ses, 'aberta')

def obtem_cookie(ses):
  global tabela
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  return obj_raiz.obtem_atributo(ses,'cookie')

def de_administrador(ses):
  global tabela
  if ses == None: return False
  assert isinstance(ses, obj_sessao.Classe)
  if not aberta(ses): return False
  usr = obtem_usuario(ses)
  return obj_usuario.obtem_atributo(usr, 'administrador')

def busca_por_identificador(id_ses):
  global tabela
  if id_ses == None: return None
  ses = obj_raiz.busca_por_identificador(id_ses, tabela, def_obj_mem)
  return ses

def busca_por_usuario(usr, soh_abertas):
  global tabela
  if usr == None: return [].copy()
  id_usr = obj_usuario.obtem_identificador(usr)
  lista_ids_ses = obj_raiz.busca_por_campo('usr', id_usr, False, tabela) # IDs das sessões deste usuário.
  if soh_abertas:
    lista_ses = list(map(lambda id: busca_por_identificador(id), lista_ids_ses)) # Pega objetos.
    lista_ses_abertas = list(filter(lambda ses: aberta(ses), lista_ses))
    lista_ids_ses = list(map(lambda ses: obtem_identificador(ses), lista_ses_abertas))
  return lista_ids_ses

def busca_por_campo(chave, val):
  global tabela
  lista_ids = obj_raiz.busca_por_campo(chave, val, False, tabela)
  return lista_ids

def fecha(ses):
  global tabela
  if (ses is not None) and (obj_sessao.obtem_atributo(ses,'aberta')):
    mods_mem = { 'aberta': False }
    muda_atributos(ses, mods_mem)
  
def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  # Dados de cada sessão:
  lista_ucs = \
    [
      ( "S-00000001", "U-00000001", "ABCDEFGHIJK", True  ),
      ( "S-00000002", "U-00000001", "BCDEFGHIJKL", True  ),
      ( "S-00000003", "U-00000002", "CDEFGHIJKLM", False ),
      ( "S-00000004", "U-00000003", "DEFGHIJKLMN", False ),
      ( "S-00000005", "U-00000005", "EFGHIJKLMNO", False ),
      ( "S-00000006", "U-00000008", "FGHIJKLMNOP", True  ),
    ]
  for id_ses_esp, id_usr, cookie, admin_esp in lista_ucs:
    usr = obj_usuario.busca_por_identificador(id_usr)
    assert usr != None and type(usr) is obj_usuario.Classe
    ses = cria(usr, cookie)
    id_ses = obj_sessao.obtem_identificador(ses)
    if verb: sys.stderr.write("  sessão %s de %s criada\n" % (id_ses, id_usr))
    # Paranóia:
    assert id_ses == id_ses_esp
    usr_cri = obj_sessao.obtem_usuario(ses)
    assert usr_cri != None and usr_cri == usr
    assert de_administrador(ses) == admin_esp
  return

def verifica_criacao(ses, id_ses, atrs):
  # A data de criacao não deve estar em {atrs}:
  return obj_raiz.verifica_criacao(ses, obj_sessao.Classe, id_ses, atrs, ('criacao',), tabela, def_obj_mem)

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(ses, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {ses} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {ses} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global tabela
  erros = [].copy();
  # !!! Implementar !!!
  return erros

def def_obj_mem(obj, id_ses, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {obj_sessao.Classe} com
  identificador {id_ses} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {obj_sessao.Classe}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0, "obj_sessao_IMP.def_obj_mem(" + str(obj) + ", " + id_ses + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, False, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = obj_sessao.Classe(id_ses, atrs_mem)
  else:
    assert obj.id == id_ses
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, True, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "modificando objeto, atrs_mem = " + str(atrs_mem))
    assert type(atrs_mem) is dict
    if len(atrs_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in atrs_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      if chave == 'usr' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if tabela.debug: mostra(2, "obj = " + str(obj))
  return obj
