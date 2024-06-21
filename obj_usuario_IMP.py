import obj_raiz
import obj_usuario
import obj_video

import util_nome_de_usuario
import util_senha
import util_email
import util_booleano
import util_nota

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql

from util_erros import ErroAtrib, erro_prog, mostra

import sys
import re

# Uma instância de {db_obj_tabela} descrevendo a tabela de usuários:
tabela = None

# Definição interna da classe {obj_usuario.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id, atrs):
    obj_raiz.Classe.__init__(self, id, atrs)

# Implementação das funções da interface:

def inicializa_modulo(limpa):
  global tabela

  # Só pode inicializar uma vez:
  if tabela != None: return

  nome_tb = "usuarios"        # Nome da tabela na base de dados.
  letra_tb = "U"              # Prefixo dos identificadores de usuários
  classe = obj_usuario.Classe # Classe dos objetos (linhas da tabela) na memória.

  # Descrição das colunas da tabela na base de dados:
  # Vide parâmetro {cols} de {db_obj_tabela.cria_tabela}.
  colunas = \
    ( ( 'nome',          type("foo"), 'TEXT',    False ), # Nome completo.
      ( 'senha',         type("foo"), 'TEXT',    False ), # Senha de login.
      ( 'email',         type("foo"), 'TEXT',    False ), # Endereço de email.
      ( 'vnota',         type(418.8), 'FLOAT',   False ), # Nota média dos vídeos.
      ( 'cnota',         type(418.8), 'FLOAT',   False ), # Nota média dos comentários.
      ( 'administrador', type(False), 'INTEGER', False ), # Define se o usuário é administrador (1=administrador)
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(atrs):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.cria}({str(atrs)})\n")

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  usr = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(usr) is obj_usuario.Classe
  if tabela.debug: sys.stderr.write(f"  < {obj_usuario.cria}\n")
  return usr

def muda_atributos(usr, mods_mem):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.muda_atributos} {str(mods_mem)}\n")
  assert usr != None and isinstance(usr, obj_usuario.Classe)
  
  erros = valida_atributos(usr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  if tabela.debug: sys.stderr.write(f"    usr antes = {str(usr)}\n")
  obj_raiz.muda_atributos(usr, mods_mem, tabela, def_obj_mem)
  if tabela.debug: sys.stderr.write(f"    usr depois = {str(usr)}\n")
  
  if tabela.debug: sys.stderr.write(f"  < {obj_usuario.muda_atributos}\n")
  return

def obtem_identificador(usr):
  global tabela
  assert usr != None and isinstance(usr, obj_usuario.Classe)
  return obj_raiz.obtem_identificador(usr)

def obtem_atributos(usr):
  global tabela
  assert usr != None and isinstance(usr, obj_usuario.Classe)
  return obj_raiz.obtem_atributos(usr)

def obtem_atributo(usr, chave):
  global tabela
  return obj_raiz.obtem_atributo(usr,chave)

def eh_administrador(usr):
  global tabela
  return obj_raiz.obtem_atributo(usr, 'administrador')

def obtem_objeto(usr_id):
  global tabela
  usr = obj_raiz.obtem_objeto(usr_id, tabela, def_obj_mem)
  assert usr == None or type(usr) is obj_usuario.Classe
  return usr

def busca_por_email(em):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.busca_por_email}: email = {em}\n");
  usr_id = obj_raiz.busca_por_campo('email', em, unico = True, tabela = tabela)
  if tabela.debug: sys.stderr.write(f"    > id encontrado = {usr_id}\n");
  return usr_id

def busca_por_nome(nome):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.busca_por_nome}: nome = {nome}\n");
  lista_ids = busca_por_campos({ 'nome': nome }, unico = False)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {','.join(lista_ids)}\n");
  return lista_ids

def busca_por_campos(args, unico):
  global tabela
  args = obj_raiz.converte_campo_em_padrao(args, 'nome');
  return obj_raiz.busca_por_campos(args, unico, tabela)
  
def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  lista_atrs = \
    [ 
      { 'id': "U-00000001",
        'nome': "José Primeiro", 
        'senha': "U-00000001", 
        'email': "primeiro@gmail.com",
        'administrador': True,
      },
      { 'id': "U-00000002",
        'nome': "João Segundo", 
        'senha': "U-00000002", 
        'email': "segundo@gmail.com",
        'administrador' : False,
      },
      { 'id': "U-00000003",
        'nome': "Juca Terceiro", 
        'senha': "U-00000003", 
        'email': "terceiro@gmail.com",
        'administrador' : False,
      },
      { 'id': "U-00000004",
        'nome': "Jurandir Quarto", 
        'senha': "U-00000004", 
        'email': "quarto@gmail.com",
        'administrador' : False,
      },
      { 'id': "U-00000005",
        'nome': "Josenildo Quinto", 
        'senha': "U-00000005", 
        'email': "quinto@ic.unicamp.br",
        'administrador' : False,
      },
      { 'id': "U-00000006",
        'nome': "Julio Sexto", 
        'senha': "U-00000006", 
        'email': "sexto@ic.unicamp.br",
        'administrador' : False,
      },
      { 'id': "U-00000007",
        'nome': "Jeferson Sétimo", 
        'senha': "U-00000007", 
        'email': "setimo@ic.unicamp.br",
        'administrador' : False,
      },
      { 'id': "U-00000008",
        'nome': "Joaquim Oitavo", 
        'senha': "U-00000008", 
        'email': "oitavo@ic.unicamp.br",
        'administrador' : True,
      },
      { 'id': "U-00000009",
        'nome': "Jonas Nono", 
        'senha': "U-00000009", 
        'email': "nono@ic.unicamp.br",
        'administrador' : False,
      },
    ]
  for atrs in lista_atrs:
    # Atribui umas notas variadas para testes de busca:
    if atrs['id'] == 'U-00000009':
      atrs['vnota'] = 3.00
      atrs['cnota'] = 1.00
    elif atrs['id'] == 'U-00000001':
      atrs['vnota'] = 2.80 
      atrs['cnota'] = 4.00
    else:
      atrs['vnota'] = 2.00
      atrs['cnota'] = 2.00
    usr_id_esp = atrs['id']; del atrs['id']
    usr = cria(atrs)
    assert usr != None and type(usr) is obj_usuario.Classe
    usr_id = obj_usuario.obtem_identificador(usr)
    nome = obj_usuario.obtem_atributo(usr,'nome')
    if verb: sys.stderr.write("  usuário %s = \"%s\" criado\n" % (usr_id, nome))
    assert usr_id == usr_id_esp, "identificador não confere"
  return

def confere_e_elimina_conf_senha(args):

  erros = []

  # Confere os campos 'senha' e 'conf_senha', elimina este último:
  if 'senha' in args or 'conf_senha' in args:
    senha = args.get('senha')
    conf_senha = args.get('conf_senha')
    if senha == '': senha = None
    if conf_senha == '': conf_senha = None
    if senha != None or conf_senha != None:
      # As duas tem que estar presentes e coincidir:
      if senha == None: 
        erros.append("A nova senha não foi especificada")
      elif conf_senha == None: 
        erros.append("A senha não foi confirmada")
      elif senha != conf_senha:
        erros.append("As senhas não batem")
  args.pop('conf_senha', None)
  return erros

def verifica_criacao(usr, usr_id, atrs):
  return obj_raiz.verifica_criacao(usr, obj_usuario.Classe, usr_id, atrs, None, tabela, def_obj_mem)

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(usr, atrs):
  """Faz validações específicas nos atributos {atrs}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {usr} é {None}, supõe que um novo usuário está sendo criado. Se {usr}
  não é {None}, deve ser um objeto de tipo {obj_usuario.Classe},
  e supõe que {atrs} sao alterações a aplicar nesse
  usuário. 
  
  Em qualquer caso, não pode haver na base nenhum usuário
  com mesmo email."""
  global tabela
  
  erros = [];
  
  # Validade dos campos fornecidos:
  nulo_ok = False
  if 'nome' in atrs:
    erros += util_nome_de_usuario.valida('nome', atrs['nome'], nulo_ok)
  if 'email' in atrs:
    erros += util_email.valida('Email', atrs['email'], nulo_ok)
  if 'vnota' in atrs:
    erros += util_nota.valida('Nota vídeos', atrs['vnota'], nulo_ok)
  if 'cnota' in atrs:
    erros += util_nota.valida('Nota comentários', atrs['cnota'], nulo_ok)
  if 'administrador' in atrs:
    erros += util_booleano.valida('Administrador', atrs['administrador'], nulo_ok)
     
  # Pega a senha, se tiver:
  if 'senha' in atrs:
    senha = atrs['senha']
    if senha == '': senha = None
  else:
    senha = None
  
  # Valida a senha:
  senha_nula_ok = (usr != None) # Pode ser nula na criação? !!!
  erros += util_senha.valida('Senha', senha, senha_nula_ok)

  # Acrescenta 'administrador' se não está presente, converte para booleano se está:
  if 'administrador' not in atrs:
    atrs['administrador'] = False
  elif type(atrs['administrador']) is not bool:
    atrs['administrador'] = True
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in tabela.colunas:
    if chave in atrs:
      nargs += 1
    elif usr == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs} = " + str(atrs) + "")
    
  # Verifica unicidade de email:
  erro_email_dup = verifica_email_em_uso(atrs['email'], usr) if 'email' in atrs else None
  if erro_email_dup != None: erros.append(erro_email_dup)

  return erros

def verifica_email_em_uso(em, usr_dado):
  """Verifica se existe algum usuário com o email {em}.
  Se {usr_dado} for {None}, não deve existir.
  Se {usr_dado} for diferente de {None}, deve 
  existir e ser esse usuário.
  
  Em caso de erro devolve uma mensagem informando a 
  repetição. Senão, retorna {None}."""
  usr_id_dado = usr_dado.id if usr_dado != None else None
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.verifica_email_em_uso}: email = '{em}' usr_id_dado = '{str(usr_id_dado)}'\n")
  usr_id_atual = busca_por_email(em)
  if tabela.debug: sys.stderr.write(f"    > usr_id_atual = '{str(usr_id_atual)}'\n")
  if usr_id_dado == None and usr_id_atual != None:
    erro = "usuário com 'email' = '" + em + "' já existe: " + usr_id_atual
  elif usr_id_dado != None and usr_id_atual != None and usr_id_atual != usr_id_dado:
    erro = "usuário com 'email' = '" + em + "' não encontrado, devia ser " + usr_id_dado
  else:
    erro = None
  if tabela.debug: sys.stderr.write(f"    > resultado = '{erro}'\n")
  return erro

def def_obj_mem(usr, usr_id, atrs_SQL):
  """Se {usr} for {None}, cria um novo objeto da classe {obj_usuario.Classe} com
  identificador {usr_id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {usr} não é {None}, deve ser um objeto da classe {obj_usuario.Classe}; nesse
  caso a função altera os atributos de {usr} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0,"obj_usuario.def_obj_mem(" + str(usr) + ", " + usr_id + ", " + str(atrs_SQL) + ") ...")
  if usr == None:
    usr = cria_obj_mem(usr_id, atrs_SQL)
  else:
    assert usr.id == usr_id
    modifica_obj_mem(usr, atrs_SQL)
  if tabela.debug: mostra(2,"usr = " + str(usr))
  return usr
    
def cria_obj_mem(usr_id, atrs_SQL):
  """Cria um novo objeto da classe {obj_usuario.Classe} com
  identificador {usr_id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global tabela

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, False, db_tabelas_do_sistema.identificador_para_objeto)
  if tabela.debug: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(tabela.colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(tabela.colunas)))
    
  # Paranóia: verifica de novo a unicidade do email:
  erro_email_dup = verifica_email_em_uso(atrs_mem['email'], None) if 'email' in atrs_mem else None
  if erro_email_dup != None: erro_prog(erro_email_dup)

  usr = obj_usuario.Classe(usr_id, atrs_mem)
  return usr
  
def modifica_obj_mem(usr, atrs_mod_SQL):
  """O parâmetro {usr} deve ser um objeto da classe {obj_usuario.Classe}; nesse
  caso a função altera os atributos de {usr} conforme especificado em
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

def recalcula_vnota(usr_id):
  assert usr_id != None

  videos = obj_video.busca_por_autor(usr_id)
  usr = obtem_objeto(usr_id)
  # Numerador e denominador da média
  numerador = 2
  denominador = 1

  for video in videos:
    video_obj = obj_video.obtem_objeto(video)
    nota = obj_video.obtem_atributo(video_obj, 'nota')
    visualizacoes = obj_video.obtem_atributo(video_obj, 'vistas')
    numerador += nota * visualizacoes
    denominador += visualizacoes
  
  mods = {
    'vnota': round(numerador / denominador, 2)
  }

  muda_atributos(usr, mods)
  return mods['vnota']

def recalcula_cnota(usr_id):
  assert usr_id != None

  comentarios = obj_comentario.busca_por_autor(usr_id)
  usr = obtem_objeto(usr_id)
  # Numerador e denominador da média
  numerador = 2
  denominador = 1

  for comentario in comentarios:
    comentario_obj = obj_comentario.obtem_objeto(comentario)
    nota = obj_comentario.obtem_atributo(comentario_obj, 'nota')
    numerador += nota
    denominador += 1
  
  mods = {
    'cnota': round(numerador / denominador, 2)
  }

  muda_atributos(usr, mods)
  return mods['cnota']
