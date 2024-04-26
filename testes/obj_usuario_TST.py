#! /usr/bin/python3

import obj_usuario  

import db_base_sql
import util_testes
from util_erros import erro_prog, aviso_prog, mostra

import sys

sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela:\n")
obj_usuario.inicializa_modulo(True)

ok_global = True # Vira {False} se um teste falha.

def testa_valida(rot_teste, funcao, res_esp, *args):
  global ok_global
  modulo = obj_usuario
  html = False   # Resultados string já são HTML?
  frag = False   # Resultados HTML são só fragmentos?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html,frag,pretty, *args)
  ok_global = ok_global and ok
  return ok

funcao = obj_usuario.valida_nome_de_usuario
for xrot, xvalido, val in \
    ( ( "Nulo",               True,  None,                                     ),
      ( "Valido",             True,  "José da Silvã P. O'Hara Costa-Gravas",   ), 
      ( "ApostInvalido",      False, "José' da Silva P. O'Hara Costa-Gravas",  ),
      ( "ApostInválido",      False, "José da Silva P'. O'Hara Costa-Gravas ", ),
      ( "MuitoCurto",         False, "José", ),
      ( "Incerto",            True,  "Ba'Ana", ),
      ( "Valido",             True,  "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "MuitoLongo",         False, "José Josefino Josualdo Josismar Josias Josenildo Josafá Josênio", ),
      ( "HifenInvalido",      False, "José-da Silva P. O'Hara Costa-Gravas",    ),
      ( "BrancoInicial",      False, " José da Silva P. O'Hara Costa-Gravas",   ),
      ( "BrancoFinal",        False, "José da Silva P. O'Hara Costa-Gravas ",   ),
      ( "BrancoDuplo",        False, "José da Silva P.  O'Hara Costa-Gravas",   ),
      ( "PontoInválido",      False, "José da Silva P.O'Hara Costa-Gravas ",    ),
      ( "CaracsInvalidos",    False, "Elon X-φ ≥ 17",                           )
    ):
  for nulo_ok in ( False, True ) if (val == None or xrot == "A") else ( False, ):
    if xvalido or ( val != None and not nulo_ok):
      valido = xvalido and (val != None or nulo_ok)
      rot_teste = "nome_" + xrot + "_nulok" + str(nulo_ok)[0] + ("_ok" if valido else "_bad")
      res_esp = [] if valido else list
      testa_valida(rot_teste, funcao, res_esp,  "padrinho", val, nulo_ok)
      
# ======================================================================

funcao = obj_usuario.valida_senha
testa_valida("senha_Valida_ok",         funcao, [],   'password', "123(meia)4", True) 
testa_valida("senha_MuitoCurta_bad",    funcao, list, 'password', "123",        True) 
testa_valida("senha_MuitoRepetida_bad", funcao, list, 'password', "111111111",  True) 
testa_valida("senha_SoLetras_bad",      funcao, list, 'password', "Segredo",    True) 
testa_valida("senha_MuitoLonga_bad",    funcao, list, 'password', "X"+("a"*60), True) 

testa_valida("senha_None_nulokT_ok",    funcao, [],   'password', None, True)  
testa_valida("senha_None_nulokF_bad",   funcao, list, 'password', None, False)

# ======================================================================

funcao = obj_usuario.valida_email
testa_valida("email_Valido_ok",          funcao, [],    'spam-to', "quem_123@ic.u-camp.br", True) 
testa_valida("email_DuasArrobas_bad",    funcao, list,  'spam-to', "123@456@onde.br",       True) 
testa_valida("email_NenhumaArroba_bad",  funcao, list,  'spam-to', "nenhures",              True) 
testa_valida("email_HostSemPonto_bad",   funcao, list,  'spam-to', "tomate@beringela",      True) 
testa_valida("email_MuitoLonga_bad",     funcao, list,  'spam-to', "X"+("a"*64)+"@gov.br",  True) 

testa_valida("email_None_nulokT_ok",     funcao, [],    'spam-to', None, True) 
testa_valida("email_None_nulokF_bad",    funcao, list,  'spam-to', None, False)

# ======================================================================

def verifica_usuario(rot_teste, usr, ident, atrs):
  """Testes básicos de consistência do objeto {usr} da classe {obj_usuario.Classe}, dados 
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  verificando usuário %s\n" % rot_teste)
  ok = obj_usuario.verifica_criacao(usr, ident, atrs)

  if usr != None and type(usr) is obj_usuario.Classe:   
    # ----------------------------------------------------------------------
    sys.stderr.write("  testando {obj_usuario.busca_por_email()}:\n")
    em1 = atrs['email']
    ident1 = obj_usuario.busca_por_email(em1)
    if ident1 != ident:
      aviso_prog("retornou " + str(ident1) + ", deveria ter retornado " + str(ident),True)
      ok = False 

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write(  "%s\n" % ("-" * 70))
  return
 
def testa_cria_usuario(rot_teste, ident, atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = obj_usuario.cria(atrs)
  verifica_usuario(rot_teste, usr, ident, atrs)
  return usr
 
# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_usuario.cria}:\n")
usr1_atrs = {
  'nome': "José Primeiro", 
  'senha': "U!00000001", 
  'email': "primeiro@gmail.com",
  'administrador': False
}
uindice1 = 1
uident1 = "U-00000001"
usr1 = testa_cria_usuario("usr1", uident1, usr1_atrs)

usr2_atrs = {
  'nome': "João Segundo", 
  'senha': "U!00000002", 
  'email': "segundo@ic.unicamp.br",
  'administrador': False
}
uindice2 = 2
uident2 = "U-00000002"
usr2 = testa_cria_usuario("usr2", uident2, usr2_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_usuario.muda_atributos}:\n")

# Alteração OK
usr1_mods = {
  'nome': "Josegrosso de Souza",
  'senha': "U!12345678"
}
obj_usuario.muda_atributos(usr1, usr1_mods)
usr1_d_atrs = usr1_atrs
for k, v in usr1_mods.items():
  usr1_d_atrs[k] = v
verifica_usuario("usr1_d", usr1, uident1, usr1_d_atrs) 

# Alteração nula:
if type(usr2) is obj_usuario.Classe:
  obj_usuario.muda_atributos(usr2, usr2_atrs) # Não deveria mudar os atributos
  verifica_usuario("usr2", usr2, uident2, usr2_atrs)

# Alteração de dados (menos email):
if type(usr2) is obj_usuario.Classe:
  usr2_m_atrs = usr2_atrs.copy()
  usr2_m_atrs['nome'] = 'Mutatis Mutande'
  usr2_m_atrs['senha'] = 'U!87654321'
  obj_usuario.muda_atributos(usr2, usr2_m_atrs)
  verifica_usuario("usr2_m", usr2, uident2, usr2_m_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
