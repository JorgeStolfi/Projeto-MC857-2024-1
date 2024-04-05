# Implementação do módulo {usuario} e da classe {obj_usuario.Classe}.

import obj_raiz
import obj_usuario
import obj_sessao

import db_tabela_generica
import db_tabelas
import db_conversao_sql
import util_identificador
import util_valida_campo
from util_testes import ErroAtrib, erro_prog, mostra
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "usuarios"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {obj_usuario.Classe} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "U"
  # Prefixo dos identificadores de usuários

colunas = None
  # Descrição das colunas da tabela na base de dados.
  
usr_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {obj_usuario.Classe}:

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
      ( 'nome',          type("foo"), 'TEXT',    False ), # Nome completo.
      ( 'senha',         type("foo"), 'TEXT',    False ), # Senha de login.
      ( 'email',         type("foo"), 'TEXT',    False ), # Endereço de email
      ( 'administrador', type(False), 'INTEGER', False ), # Define se o usuário é administrador (1=administrador)
    )
  if limpa:
    db_tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    db_tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs_mem):
  global cache, nome_tb, letra_tb, colunas
  if usr_debug: mostra(0,"obj_usuario_IMP.cria({str(atrs_mem)}) ...")

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  usr = obj_raiz.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(usr) is obj_usuario.Classe
  return usr

def muda_atributos(usr, mods_mem):
  global cache, nome_tb, letra_tb, colunas
  if usr_debug: sys.stderr.write("  > {obj_usuario.muda_atributos}:\n")
  
  erros = valida_atributos(usr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  if usr_debug: sys.stderr.write(f"    > usr antes = {str(usr)} mods_mem = {str(mods_mem)}\n")
  obj_raiz.muda_atributos(usr, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  if usr_debug: sys.stderr.write(f"    > usr depois = {str(usr)}\n")
  return

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas
  assert usr != None
  return obj_raiz.obtem_identificador(usr)

def obtem_atributos(usr):
  global cache, nome_tb, letra_tb, colunas
  return obj_raiz.obtem_atributos(usr)

def obtem_atributo(usr, chave):
  global cache, nome_tb, letra_tb, colunas
  return obj_raiz.obtem_atributo(usr,chave)

def busca_por_identificador(id_usr):
  global cache, nome_tb, letra_tb, colunas
  usr = obj_raiz.busca_por_identificador(id_usr, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert usr == None or type(usr) is obj_usuario.Classe
  return usr

def busca_por_email(em):
  global cache, nome_tb, letra_tb, colunas
  unico = True
  if usr_debug: sys.stderr.write(f"  > {obj_usuario_IMP.busca_por_email}: email = {em}\n");
  id_usr = obj_raiz.busca_por_campo('email', em, unico, cache, nome_tb, letra_tb, colunas)
  if usr_debug: sys.stderr.write(f"    > id encontrado = {id_usr}\n");
  return id_usr

def busca_por_nome(nome):
  global cache, nome_tb, letra_tb, colunas
  if usr_debug: sys.stderr.write(f"  > {obj_usuario_IMP.busca_por_nome}: nome = {nome}\n");
  lista_ids = obj_raiz.busca_por_semelhanca(nome_tb, letra_tb, ['nome'], [nome])
  if usr_debug: sys.stderr.write(f"    > lista de ids encontrada = {lista_ids.join(',')}\n");
  sys.stdout.write(",".join(lista_ids))
  return lista_ids

def sessoes_abertas(usr):  
  id_usr = obj_usuario.obtem_identificador(usr)
  lista_ids_ses = obj_sessao.busca_por_usuario(id_usr) # IDs das sessões deste usuário.
  lista_ses = map(lambda id: obj_sessao.busca_por_identificador(id), lista_ids_ses) # Pega objetos.
  # Filtra apenas as Sessoes que estao abertas
  lista_ses_abertas = list(filter(lambda ses: obj_sessao.aberta(ses), lista_ses))
  return lista_ses_abertas
  
def cria_testes(verb):
  global cache, nome_tb, letra_tb, colunas
  inicializa_modulo(True)
  lista_atrs = \
    [ 
      { # U-00000001
        'nome': "José Primeiro", 
        'senha': "11111111", 
        'email': "primeiro@gmail.com",
        'administrador': True,
      },
      { # U-00000002
        'nome': "João Segundo", 
        'senha': "22222222", 
        'email': "segundo@gmail.com",
        'administrador' : False,
      },
      { # U-00000003
        'nome': "Juca Terceiro", 
        'senha': "33333333", 
        'email': "terceiro@gmail.com",
        'administrador' : False,
      },
      { # U-00000004
        'nome': "Jurandir Quarto", 
        'senha': "44444444", 
        'email': "quarto@gmail.com",
        'administrador' : False,
      },
      { # U-00000005
        'nome': "Josenildo Quinto", 
        'senha': "55555555", 
        'email': "quinto@ic.unicamp.br",
        'administrador' : False,
      },
      { # U-00000006
        'nome': "Julio Sexto", 
        'senha': "66666666", 
        'email': "sexto@ic.unicamp.br",
        'administrador' : False,
      },
      { # U-00000007
        'nome': "Jeferson Setimo", 
        'senha': "77777777", 
        'email': "setimo@ic.unicamp.br",
        'administrador' : False,
      },
      { # U-00000008
        'nome': "Joaquim Oitavo", 
        'senha': "88888888", 
        'email': "oitavo@ic.unicamp.br",
        'administrador' : True,
      },
      { # U-00000009
        'nome': "Jonas Nono", 
        'senha': "99999999", 
        'email': "nono@ic.unicamp.br",
        'administrador' : False,
      },

    ]
  for atrs in lista_atrs:
    usr = cria(atrs)
    assert usr != None and type(usr) is obj_usuario.Classe
    id_usr = obj_usuario.obtem_identificador(usr)
    nome = obj_usuario.obtem_atributo(usr,'nome')
    if verb: sys.stderr.write("  usuário %s = \"%s\" criado\n" % (id_usr, nome))
  return

def confere_e_elimina_conf_senha(args):

  senha = (args['senha'] if 'senha' in args else None)
  if senha != None and senha != '':
    # Senha está sendo alterada/definida.  Precisa confirmar senha:
    if 'conf_senha' not in args:
      raise ErroAtrib([ "campo 'Confirmar Senha' 'e obrigatório", ])
    else:
      if senha != args['conf_senha']:
        raise ErroAtrib([ "senhas não batem", ])
   
  # Remove o campo 'conf_senha', não mais necessários
  if 'conf_senha' in args: del args['conf_senha']
  return

def verifica_criacao(usr, id_usr, atrs):
  return obj_raiz.verifica_criacao(usr, obj_usuario.Classe, id_usr, atrs, None, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def liga_diagnosticos(val):
  global usr_debug
  usr_debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(usr, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {usr} é {None}, supõe que um novo usuário está sendo criado. Se {usr}
  não é {None}, deve ser um objeto de tipo {obj_usuario.Classe},
  e supõe que {atrs_mem} sao alterações a aplicar nesse
  usuário. 
  
  Em qualquer caso, não pode haver na base nenhum usuário
  com mesmo email."""
  global cache, nome_tb, letra_tb, colunas
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'nome' in atrs_mem:
    erros += util_valida_campo.nome_de_usuario('nome', atrs_mem['nome'], False)
  if 'email' in atrs_mem:
    erros += util_valida_campo.email('Email', atrs_mem['email'], False)
  if 'administrador' in atrs_mem:
    erros += util_valida_campo.booleano('Administrador', atrs_mem['administrador'], False)
     
  # Pega a senha, se tiver:
  if 'senha' in atrs_mem:
    senha = atrs_mem['senha']
    if senha == '': senha = None
  else:
    senha = None
  
  # Valida a senha:
  erros += util_valida_campo.senha('Senha', senha, (usr != None))

  # Acrescenta 'administrador' se não está presente, converte para booleano se está:
  if 'administrador' not in atrs_mem:
    atrs_mem['administrador'] = False
  elif type(atrs_mem['administrador']) is not bool:
    atrs_mem['administrador'] = True
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs_mem} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs_mem:
      nargs += 1
    elif usr == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs_mem):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs_mem} = " + str(atrs_mem) + "")
    
  # Verifica unicidade de email:
  erro_email_dup = verifica_email_em_uso(atrs_mem['email'], usr) if 'email' in atrs_mem else None
  if erro_email_dup != None: erros.append(erro_email_dup)

  return erros

def verifica_email_em_uso(em, usr_dado):
  """Verifica se existe algum usuário com o email {em}.
  Se {usr_dado} for {None}, não deve existir.
  Se {usr_dado} for diferente de {None}, deve 
  existir e ser esse usuário.
  
  Em caso de erro devolve uma mensagem informando a 
  repetição. Senão, retorna {None}."""
  id_usr_dado = usr_dado.id if usr_dado != None else None
  if usr_debug: sys.stderr.write(f"  > {obj_usuario.verifica_email_em_uso}: email = '{em}' id_usr_dado = '{str(id_usr_dado)}'\n")
  id_usr_atual = busca_por_email(em)
  if usr_debug: sys.stderr.write(f"    > id_usr_atual = '{str(id_usr_atual)}'\n")
  if id_usr_dado == None and id_usr_atual != None:
    erro = "usuário com 'email' = '" + em + "' já existe: " + id_usr_atual
  elif id_usr_dado != None and id_usr_atual != None and id_usr_atual != id_usr_dado:
    erro = "usuário com 'email' = '" + em + "' não encontrado, devia ser " + id_usr_dado
  else:
    erro = None
  if usr_debug: sys.stderr.write(f"    > resultado = '{erro}'\n")
  return erro

def def_obj_mem(usr, id_usr, atrs_SQL):
  """Se {usr} for {None}, cria um novo objeto da classe {obj_usuario.Classe} com
  identificador {id_usr} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {usr} não é {None}, deve ser um objeto da classe {obj_usuario.Classe}; nesse
  caso a função altera os atributos de {usr} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas
  if usr_debug: mostra(0,"obj_usuario_IMP.def_obj_mem(" + str(usr) + ", " + id_usr + ", " + str(atrs_SQL) + ") ...")
  if usr == None:
    usr = cria_obj_mem(id_usr, atrs_SQL)
  else:
    assert usr.id == id_usr
    modifica_obj_mem(usr, atrs_SQL)
  if usr_debug: mostra(2,"usr = " + str(usr))
  return usr
    
def cria_obj_mem(id_usr, atrs_SQL):
  """Cria um novo objeto da classe {obj_usuario.Classe} com
  identificador {id_usr} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global cache, nome_tb, letra_tb, colunas

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, db_tabelas.identificador_para_objeto)
  if usr_debug: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))
    
  # Paranóia: verifica de novo a unicidade do email:
  erro_email_dup = verifica_email_em_uso(atrs_mem['email'], None) if 'email' in atrs_mem else None
  if erro_email_dup != None: erro_prog(erro_email_dup)

  usr = obj_usuario.Classe(id_usr, atrs_mem)
  return usr
  
def modifica_obj_mem(usr, atrs_mod_SQL):
  """O parâmetro {usr} deve ser um objeto da classe {obj_usuario.Classe}; nesse
  caso a função altera os atributos de {usr} conforme especificado em
  {atrs_mod_SQL}.  A entrada correspondente da base de dados *NÃO* é alterada.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas

  # Converte atributos para formato na memória. Pode ser subconjunto:
  atrs_mod_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_mod_SQL, colunas, True, db_tabelas.identificador_para_objeto)
  if usr_debug: mostra(2,"modificando objeto, atrs_mod_mem = " + str(atrs_mod_mem))
  assert type(atrs_mod_mem) is dict
  if len(atrs_mod_mem) > len(colunas):
    erro_prog("numero de atributos a alterar = " + str(len(atrs_mod_mem)) + " excessivo")

  # Paranóia: verifica de novo a unicidade de email:
  erro_email_dup = verifica_email_em_uso(atrs_mod_mem['email'], usr) if 'email' in atrs_mod_mem else None
  if erro_email_dup != None: erro_prog(erro_email_dup)

  # Modifica os atributos:
  for chave, val_mem in atrs_mod_mem.items():
    if not chave in usr.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = usr.atrs[chave]
    if val_mem != None and val_velho != None and (not type(val_velho) is type(val_mem)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    usr.atrs[chave] = val_mem
  return usr
