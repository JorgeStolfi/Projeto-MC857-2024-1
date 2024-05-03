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

def testa_funcao_validadora(rot_teste, funcao, res_esp, *args):
  global ok_global
  modulo = obj_usuario
  html = False   # Resultados string já são HTML?
  frag = False   # Resultados HTML são só fragmentos?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao(rot_teste, modulo, funcao, res_esp, html,frag,pretty, *args)
  ok_global = ok_global and ok
  return ok

funcao = obj_usuario.valida_nome
# {xvalid} = válido em qualquer caso (depende de {nulo_ok}).
# {xvalparc} = válido se {parcial = True} (depende de {nulo_ok}).
for xrot, xvalid, xvalparc, val in \
    ( # Válidos como parciais e completos:
      ( "Nulo",               True,   True,   None, ),
      ( "Valido1",            True,   True,   "José da Silvã P. O'Hara Costa-Gravas",   ), 
      ( "Valido2",            True,   True,   "P.-Louis Sant'Ana", ),
      ( "Valido3",            True,   True,   "Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghi Abcdefghij", ),
      ( "Valido4",            True,   True,   "Abcdefghij", ),
      # Válidos só como parciais:
      ( "MuitoCurtoFull9",    False,  True,   "José Josias",   ),
      ( "BrancoInicial",      False,  True,   " José da Silva P. O'Hara Costa-Gravas",   ),
      ( "BrancoFinal",        False,  True,   "José da Silva P. O'Hara Costa-Gravas ",   ),
      # Inválidos mesmo somo parciais: 
      ( "MuitoCurtoParc2",    False,  False,  "Jo",             ),
      ( "CaracsInvalidos",    False,  False,  "Elon X-φ ≥ 17",  ),
      ( "BrancoDuplo",        False,  False,  "José da Silva P.  O'Hara Costa-Gravas",   ),
      ( "MuitoLongo",         False,  False,  "José Josefino Josualdo Josismar Josias Josenildo Josafá Josênio", ),
      ( "ApostInvalido1",     False,  False,  "José' da Silva P. O'Hara Costa-Gravas",   ),
      ( "ApostInvalido2",     False,  False,  "José da Silva P'. O'Hara Costa-Gravas",   ),
      ( "HifenInvalido1",     False,  False,  "José-da Silva P-. O'Hara Costa-Gravas",   ),
      ( "HifenInvalido2",     False,  False,  "José-da Silva O'Hara Costa-Gravas",       ),
      ( "PontoInvalido2",     False,  False,  "José da Silva P.O'Hara Costa-Gravas ",    ),
      ( "ApostInicial",       False,  True,   "'Hara Costa-Gravas",  ),
      ( "ApostFinal",         False,  True,   "José da Silva O'",    ),
      ( "Hifeninicial",       False,  True,   "José-da Silva P. O'Hara Costa-Gravas",    ),
      ( "HifenFinal",         False,  True,   "Costa-",      ),
      ( "PontoInicial",       False,  True,   ".-Louis",     ),
      ( "PontoFinal",         False,  True,   "José da S.",  ),
    ):
  for nulo_ok in ( False, True ):
    for parcial in ( False, True ):
      if val == None:
        valido = nulo_ok
      elif parcial:
        valido = xvalparc
      else:
        valido = xvalid
      # Exclui casos repetitivos: 
      if (not nulo_ok) or (nulo_ok and (val == None or xrot == "Valido1")):
        rot_teste = "nome_" + xrot + "_nulok" + str(nulo_ok)[0] + "_parcial" + str(parcial)[0] + ("_ok" if valido else "_bad")
        res_esp = [] if valido else list
        testa_funcao_validadora(rot_teste, funcao, res_esp,  "padrinho", val, nulo_ok, parcial)
      
# ======================================================================

funcao = obj_usuario.valida_senha
testa_funcao_validadora("Valida_ok",         funcao, [],   'password', "123(meia)4", True) 
testa_funcao_validadora("MuitoCurta_bad",    funcao, list, 'password', "123",        True) 
testa_funcao_validadora("MuitoRepetida_bad", funcao, list, 'password', "111111111",  True) 
testa_funcao_validadora("SoLetras_bad",      funcao, list, 'password', "Segredo",    True) 
testa_funcao_validadora("MuitoLonga_bad",    funcao, list, 'password', "X"+("a"*60), True) 

testa_funcao_validadora("None_nulokT_ok",    funcao, [],   'password', None, True)  
testa_funcao_validadora("None_nulokF_bad",   funcao, list, 'password', None, False)

# ======================================================================

funcao = obj_usuario.valida_email
testa_funcao_validadora("Valido_ok",          funcao, [],    'spam-to', "quem_123@ic.u-camp.br", True) 
testa_funcao_validadora("DuasArrobas_bad",    funcao, list,  'spam-to', "123@456@onde.br",       True) 
testa_funcao_validadora("NenhumaArroba_bad",  funcao, list,  'spam-to', "nenhures",              True) 
testa_funcao_validadora("HostSemPonto_bad",   funcao, list,  'spam-to', "tomate@beringela",      True) 
testa_funcao_validadora("MuitoLonga_bad",     funcao, list,  'spam-to', "X"+("a"*64)+"@gov.br",  True) 

testa_funcao_validadora("None_nulokT_ok",     funcao, [],    'spam-to', None, True) 
testa_funcao_validadora("None_nulokF_bad",    funcao, list,  'spam-to', None, False)

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
