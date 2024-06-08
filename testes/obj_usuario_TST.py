#! /usr/bin/python3

import obj_usuario  
import obj_video

import db_base_sql
import util_testes
from util_erros import erro_prog, aviso_prog, mostra

import sys

sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

sys.stderr.write("  Inicializando módulo {usuario}, limpando tabela:\n")
obj_usuario.inicializa_modulo(True)

ok_global = True # Vira {False} se um teste falha.

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
  'vnota': 2.00,
  'administrador': False
}
uindice1 = 1
uident1 = "U-00000001"
usr1 = testa_cria_usuario("usr1", uident1, usr1_atrs)

usr2_atrs = {
  'nome': "João Segundo", 
  'senha': "U!00000002", 
  'email': "segundo@ic.unicamp.br",
  'vnota': 2.00,
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
  'senha': "U!12345678",
  'vnota': 3.00,
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
  usr2_m_atrs['vnota'] = 1.00
  obj_usuario.muda_atributos(usr2, usr2_m_atrs)
  verifica_usuario("usr2_m", usr2, uident2, usr2_m_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_usuario.recalcula_vnota}:\n")
# Limpa os dados dos testes anteriores e inicializa os valores padrão no bd
db_base_sql.executa_comando_DELETE("usuarios", "email = 'primeiro@gmail.com'")
db_base_sql.executa_comando_DELETE("usuarios", "email = 'segundo@ic.unicamp.br'")
obj_usuario.cria_testes(True)
obj_video.cria_testes(True)

# Para os testes usuaremos os 3 primeiros usuários
usr1_id = "U-00000001"
sys.stderr.write("  %s\n" % ("-" * 70))
sys.stderr.write("  recalculando vnota de usuário %s\n" % usr1_id)
nota1 = obj_usuario.recalcula_vnota(usr1_id)
sys.stderr.write("  nota recalculada = %s\n" % nota1)

usr2_id = "U-00000002"
sys.stderr.write("  %s\n" % ("-" * 70))
sys.stderr.write("  recalculando vnota de usuário %s\n" % usr2_id)
nota2 = obj_usuario.recalcula_vnota(usr2_id)
sys.stderr.write("  nota recalculada = %s\n" % nota2)

usr3_id = "U-00000003"
sys.stderr.write("  %s\n" % ("-" * 70))
sys.stderr.write("  recalculando vnota de usuário %s\n" % usr3_id)
nota3 = obj_usuario.recalcula_vnota(usr3_id)
sys.stderr.write("  nota recalculada = %s\n" % nota3)
sys.stderr.write("  %s\n" % ("-" * 70))

# Define uma lista com pares (nota, nota_esperada)
notas = [(nota1, 2.35), (nota2, 2.9), (nota3, 2.0)]

for nota, nota_esperada in notas:
  # Valida se a nota gerada é igual a nota esperada
  if nota != nota_esperada:
    ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
