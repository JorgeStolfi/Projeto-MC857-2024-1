import obj_raiz
import obj_usuario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql
import util_valida_campo

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
      ( 'email',         type("foo"), 'TEXT',    False ), # Endereço de email
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

def obtem_objeto(id_usr):
  global tabela
  usr = obj_raiz.obtem_objeto(id_usr, tabela, def_obj_mem)
  assert usr == None or type(usr) is obj_usuario.Classe
  return usr

def busca_por_email(em):
  global tabela
  unico = True
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.busca_por_email}: email = {em}\n");
  id_usr = obj_raiz.busca_por_campo('email', em, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > id encontrado = {id_usr}\n");
  return id_usr

def busca_por_nome(nome):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.busca_por_nome}: nome = {nome}\n");
  args = { 'nome': nome }
  unico = False
  lista_ids = obj_raiz.busca_por_semelhanca(args, unico, tabela)
  if tabela.debug: sys.stderr.write(f"    > lista de ids encontrada = {','.join(lista_ids)}\n");
  return lista_ids

def busca_por_campos(args, unico):
  global tabela
  return obj_raiz.busca_por_campos(args, unico, tabela)
  
def busca_por_semelhanca(args, unico):
  global tabela
  return obj_raiz.busca_por_semelhanca(args, unico, tabela)
  
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
    id_usr_esp = atrs['id']; del atrs['id']
    usr = cria(atrs)
    assert usr != None and type(usr) is obj_usuario.Classe
    id_usr = obj_usuario.obtem_identificador(usr)
    nome = obj_usuario.obtem_atributo(usr,'nome')
    if verb: sys.stderr.write("  usuário %s = \"%s\" criado\n" % (id_usr, nome))
    assert id_usr == id_usr_esp, "identificador não confere"
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
  return obj_raiz.verifica_criacao(usr, obj_usuario.Classe, id_usr, atrs, None, tabela, def_obj_mem)

def valida_nome(chave, val, nulo_ok, parcial):
  erros = [].copy()
  epref = f"campo '{chave}' = \"{val}\" não é nome válido: "
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ epref + f"deve ser string" ]
  else:
    nmin = 3 if parcial else 10
    nmax = 60
    n = len(val)
    if n < nmin:
      erros += [ epref + f"é muito curto ({n} caracteres, mínimo {nmin})" ]
    elif n > nmax:
      erros += [ epref + f"é muito longo ({n} caracteres, máximo {nmax})" ]

    re_car_validos = r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s.'-]+$"
    if not re.match(re_car_validos, val):
      erros += [ epref + f"tem caracteres não permitidos" ]

    if not parcial and (val[0].isspace() or val[-1].isspace()):
      erros += [ epref + f"branco antes ou depois do nome" ]

    if '  ' in val:
      erros += [ epref + f"tem dois ou mais espaços seguidos" ]

    if not parcial and not val[0].isupper():
      erros += [ epref + f"primeiro caractere '{val[0]}' não é letra maiúscula" ]

    if not parcial and not val[-1].isalpha():
      erros += [ epref + f"o último caractere '{val[-1]}' não é uma letra" ]
    
    re_pto_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][.]" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ])[.]"
    if re.match(re_pto_prev, val):
      erros += [ epref + f"um ponto deve seguir uma letra" ]
      
    re_pto_prox = r"[.][^-\s]" if parcial else r"[.]([^-\s]|$)"
    if re.match(re_pto_prox, val):
      erros += [ epref + f"um ponto deve ser seguido por hífen ou um espaço em branco" ]
    
    re_apo_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ][']" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ])[']"
    if re.match(re_apo_prev, val):
      erros += [ epref + f"um apóstrofe deve seguir uma letra" ]
      
    re_apo_prox = r"['][^A-ZÀ-ÖØ-Þ]" if parcial else r"[']([^A-ZÀ-ÖØ-Þ]|$)"
    if re.match(re_apo_prox, val):
      erros += [ epref + f"um apóstrofe deve ser seguido por uma letra maiúscula" ]
    
    re_hif_prev = r"[^a-zA-ZÀ-ÖØ-öø-ÿ.][-]" if parcial else r"(^|[^a-zA-ZÀ-ÖØ-öø-ÿ.])[-]"
    if re.match(re_hif_prev, val):
      erros += [ epref + f"um hífen deve seguir uma letra ou um ponto" ]
      
    re_hif_prox = r"[-][^A-ZÀ-ÖØ-Þ]" if parcial else r"[-]([^A-ZÀ-ÖØ-Þ]|$)"
    if re.match(re_hif_prox, val):
      erros += [ epref + f"um hífen deve ser seguido por uma letra maiúscula" ]

  return erros

def valida_senha(chave, val, nulo_ok):
  # O padrão {re} para caracter ASCII visível é [!-~], e para
  # letra ou dígito é [A-Za-z0-9].
  erros = [].copy()
  if val == None:
    if not nulo_ok:# !!! Implementar conforme documentação na interface !!!
      erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ f"campo '{chave}' = \"{str(val)}\" não é senha válida: deve ser string" ]
  else:
    if not re.search(r'^[!-~]*$', val):
      erros += [ f"campo '{chave}' não é senha válida: pode conter apenas caracters visíveis ASCII ([!-~])" ]
    nmin = 8  # Comprimento mínimo.
    nmax = 14 # Comprimento máximo.
    n = len(val)
    if n < nmin:
      erros += [ f"campo '{chave}' não é senha válida: muito curto ({n} caracteres, mínimo {nmin})"]
    elif n > nmax:
      erros += [ f"campo '{chave}' não é senha válida: muito longo ({n} caracteres, máximo {nmax})"]
    if not re.search(r'[A-Za-z]', val):
      erros += [ f"campo '{chave}' não é senha válida: deve conter no mínimo uma letra" ]
    if not re.search(r'[0-9]', val):
      erros += [ f"campo '{chave}' não é senha válida: deve conter no mínimo um dígito" ]
    if re.search(r'^[a-zA-Z0-9]*$', val):
      erros += [ f"campo '{chave}' não é senha válida: não pode ser apenas letras e dígitos" ]
  return erros

def valida_email(chave, val, nulo_ok):
  erros = [].copy()
  if val == None:
    if not nulo_ok: erros += [ f"campo '{chave}' não pode ser omitido" ]
  elif type(val) is not str:
    erros += [ f"campo '{chave}' = \"{str(val)}\" não é um email válido: deve ser string" ]
  else:
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao_email, val):
      erros += [ f"campo '{chave}' = '%s' não é um email válido" % ( str(val))]

    #Validar se o campo usuario e campo dominio estão dentro dos padrões de, respectivamente 64 e 255 caracteres
    else:
      partes = val.split('@')
      usuario = partes[0]
      dominio = partes[1]
      if not 1< len(usuario) < 64:
        erros += [ f"campo '{chave}' = \"{str(val)}\" não é um email válido: usuario inválido "]
      if not 1< len(dominio) < 255:
        erros += [ f"campo '{chave}' = \"{str(val)}\" não é um email válido: dominio inválido "]
      
      #validar as partes do dominio
      partes_dominio = dominio.split('.')
      for parte in partes_dominio:
        if not 1 < len(parte) < 64:
          erros += [ f"campo '{chave}' = \"{str(val)}\" não é um email válido: dominio inválido "]
  return erros

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
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'nome' in atrs:
    nome_nulo_ok = False
    nome_parcial = False
    erros += valida_nome('nome', atrs['nome'], nome_nulo_ok, nome_parcial)
  if 'email' in atrs:
    email_nulo_ok = False
    erros += valida_email('Email', atrs['email'], email_nulo_ok)
  if 'administrador' in atrs:
    erros += util_valida_campo.booleano('Administrador', atrs['administrador'], False)
     
  # Pega a senha, se tiver:
  if 'senha' in atrs:
    senha = atrs['senha']
    if senha == '': senha = None
  else:
    senha = None
  
  # Valida a senha:
  senha_nula_ok = (usr != None) # Pode ser nula na criação? !!!
  erros += valida_senha('Senha', senha, senha_nula_ok)

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
  id_usr_dado = usr_dado.id if usr_dado != None else None
  if tabela.debug: sys.stderr.write(f"  > {obj_usuario.verifica_email_em_uso}: email = '{em}' id_usr_dado = '{str(id_usr_dado)}'\n")
  id_usr_atual = busca_por_email(em)
  if tabela.debug: sys.stderr.write(f"    > id_usr_atual = '{str(id_usr_atual)}'\n")
  if id_usr_dado == None and id_usr_atual != None:
    erro = "usuário com 'email' = '" + em + "' já existe: " + id_usr_atual
  elif id_usr_dado != None and id_usr_atual != None and id_usr_atual != id_usr_dado:
    erro = "usuário com 'email' = '" + em + "' não encontrado, devia ser " + id_usr_dado
  else:
    erro = None
  if tabela.debug: sys.stderr.write(f"    > resultado = '{erro}'\n")
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
  global tabela
  if tabela.debug: mostra(0,"obj_usuario.def_obj_mem(" + str(usr) + ", " + id_usr + ", " + str(atrs_SQL) + ") ...")
  if usr == None:
    usr = cria_obj_mem(id_usr, atrs_SQL)
  else:
    assert usr.id == id_usr
    modifica_obj_mem(usr, atrs_SQL)
  if tabela.debug: mostra(2,"usr = " + str(usr))
  return usr
    
def cria_obj_mem(id_usr, atrs_SQL):
  """Cria um novo objeto da classe {obj_usuario.Classe} com
  identificador {id_usr} e atributos {atrs_SQL}, tais como extraidos
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

  usr = obj_usuario.Classe(id_usr, atrs_mem)
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
