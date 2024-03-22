import obj_raiz
import obj_sessao
import obj_usuario

import db_tabela_generica
import db_tabelas
import db_conversao_sql
import util_identificador
import util_valida_campo; from util_valida_campo import ErroAtrib
from util_testes import erro_prog, mostra
import sys

from datetime import datetime, timezone

# VARIÁVEIS GLOBAIS DO MÓDULO

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {obj_sessao.Classe} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "sessoes"
  # Nome da tabela na base de dados.

letra_tb = "S"
  # Prefixo comum dos identificadores de sessao.

colunas = None
  # Descrição das colunas da tabela na base de dados.

ses_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {obj_usuario.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id, atrs):
    global cache, nome_tb, letra_tb, colunas
    obj_raiz.Classe.__init__(self, id, atrs)


# Implementações:

def inicializa_modulo(limpa):
  global cache, nome_tb, letra_tb, colunas
  colunas = \
    (
      ( "usr",          obj_usuario.Classe,     'TEXT',    False ),  # Objeto/id do usuário logado na sessão.
      ( "criacao",      type("foo"),            'TEXT',    False ),  # Momento de criação da sessão.
      ( "aberta",       type(False),            'INTEGER', False ),  # Estado da sessao (1 = aberta).
      ( "cookie",       type("foo"),            'TEXT',    False ),  # Cookie da sessao.
    )
  if limpa:
    db_tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    db_tabela_generica.cria_tabela(nome_tb, colunas)

def cria(usr, cookie):
  global cache, nome_tb, letra_tb, colunas

  atrs_cria = {
    'usr': usr,
    'criacao': datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %z"),
    'aberta': True,
    'cookie': cookie
  }

  erros = valida_atributos(None, atrs_cria)
  if len(erros) != 0: raise ErroAtrib(erros)

  ses = obj_raiz.cria(atrs_cria, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(ses) is obj_sessao.Classe
  return ses

def obtem_identificador(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_identificador(ses)

def obtem_atributos(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributos(ses)

def obtem_atributo(ses, chave):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributo(ses, chave)

def obtem_usuario(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributo(ses, 'usr')

def obtem_data_de_criacao(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributo(ses, 'criacao')

def aberta(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributo(ses, 'aberta')

def obtem_cookie(ses):
  global cache, nome_tb, letra_tb, colunas
  assert (ses != None) and type(ses) is obj_sessao.Classe
  return obj_raiz.obtem_atributo(ses,'cookie')

def eh_administrador(ses):
  global cache, nome_tb, letra_tb, colunas
  if  ses == None or not aberta(ses): return False
  usr = obtem_usuario(ses)
  return obj_usuario.obtem_atributo(usr, 'administrador')

def busca_por_identificador(id_ses):
  global cache, nome_tb, letra_tb, colunas
  if id_ses == None: return None
  ses = obj_raiz.busca_por_identificador(id_ses, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return ses

def busca_por_usuario(id_usr):
  global cache, nome_tb, letra_tb, colunas
  if id_usr == None: return [].copy()
  ses = obj_raiz.busca_por_campo("usr", id_usr, False, cache, nome_tb, letra_tb, colunas)
  return ses

def busca_por_campo(chave, val):
  global cache, nome_tb, letra_tb, colunas
  lista_ids = obj_raiz.busca_por_campo(chave, val, False, cache, nome_tb, letra_tb, colunas)
  return lista_ids

def muda_atributos(ses, atrs_mod_mem):
  global cache, nome_tb, letra_tb, colunas

  erros = valida_atributos(ses, atrs_mod_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  obj_raiz.muda_atributos(ses, atrs_mod_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def fecha(ses):
  global cache, nome_tb, letra_tb, colunas
  if (ses is not None) and (obj_sessao.obtem_atributo(ses,'aberta')):
    atrs_mod_mem = { 'aberta': False }
    muda_atributos(ses, atrs_mod_mem)

def cria_testes(verb):
  global cache, nome_tb, letra_tb, colunas
  inicializa_modulo(True)
  # Identificador de usuários e cookie de cada sessão:
  lista_ucs = \
    [
      ( "U-00000001", "ABCDEFGHIJK" ), # S-00000001
      ( "U-00000001", "BCDEFGHIJKL" ), # S-00000002
      ( "U-00000002", "CDEFGHIJKLM" ), # S-00000003
      ( "U-00000003", "DEFGHIJKLMN" ), # S-00000004
    ]
  for id_usr, cookie in lista_ucs:
    usr = obj_usuario.busca_por_identificador(id_usr)
    assert usr != None and type(usr) is obj_usuario.Classe
    ses = cria(usr, cookie)
    assert ses != None and type(ses) is obj_sessao.Classe
    id_ses = obj_sessao.obtem_identificador(ses)
    usr = obj_sessao.obtem_usuario(ses)
    id_usr = obj_usuario.obtem_identificador(usr) if usr != None else "ninguém"
    if verb: sys.stderr.write("  sessão %s de %s criada\n" % (id_ses, id_usr))
  return

def verifica_criacao(ses, id_ses, atrs):
  # A data de criacao não deve estar em {atrs}:
  return obj_raiz.verifica_criacao(ses, obj_sessao.Classe, id_ses, atrs, ('criacao',), cache, nome_tb, letra_tb, colunas, def_obj_mem)

def liga_diagnosticos(val):
  global ses_debug
  ses_debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(ses, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {ses} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {ses} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global cache, nome_tb, letra_tb, colunas
  erros = [].copy();
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
  global cache, nome_tb, letra_tb, colunas
  if ses_debug: mostra(0, "obj_sessao_IMP.def_obj_mem(" + str(obj) + ", " + id_ses + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, db_tabelas.identificador_para_objeto)
    if ses_debug: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = obj_sessao.Classe(id_ses, atrs_mem)
  else:
    assert obj.id == id_ses
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, db_tabelas.identificador_para_objeto)
    if ses_debug: mostra(2, "modificando objeto, atrs_mem = " + str(atrs_mem))
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
  if ses_debug: mostra(2, "obj = " + str(obj))
  return obj
