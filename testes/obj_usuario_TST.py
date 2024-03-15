#! /usr/bin/python3
import obj_usuario  
import db_tabela_generica
import db_base_sql
import util_testes
import sys
from util_testes import erro_prog, aviso_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela:\n")
obj_usuario.inicializa_modulo(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_usuario(rotulo, usr, ident, atrs):
  """Testes básicos de consistência do objeto {usr} da classe {obj_usuario.Classe}, dados 
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  verificando usuário %s\n" % rotulo)
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
 
def testa_cria_usuario(rotulo, ident, atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = obj_usuario.cria(atrs)
  verifica_usuario(rotulo, usr, ident, atrs)
  return usr
 
# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_usuario.cria}:\n")
usr1_atrs = {
  'nome': "José Primeiro", 
  'senha': "11111111", 
  'email': "primeiro@gmail.com",
  'administrador': False
}
uindice1 = 1
uident1 = "U-00000001"
usr1 = testa_cria_usuario("usr1", uident1, usr1_atrs)

usr2_atrs = {
  'nome': "João Segundo", 
  'senha': "22222222", 
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
  'senha': "10101010"
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
  usr2_m_atrs['senha'] = '10101010'
  obj_usuario.muda_atributos(usr2, usr2_m_atrs)
  verifica_usuario("usr2_m", usr2, uident2, usr2_m_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("- teste falhou")
