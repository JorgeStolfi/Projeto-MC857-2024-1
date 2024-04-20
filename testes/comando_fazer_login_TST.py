#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes
from util_erros import erro_prog, aviso_prog, mostra
import comando_fazer_login

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_fazer_login(rot_teste, email, senha, deveria_logar):
  global ok_global
  dados = {
    "email": email,
    "senha": senha
  }
  modulo = comando_fazer_login
  pag, ses = modulo.processa(None, dados)

  if (deveria_logar and ses == None):
    ok_global = False
    aviso_prog("Não gerou a sessão quando deveria para o email " + str(email), True)

  if ((not deveria_logar) and ses != None):
    ok_global = False
    aviso_prog("Gerou gerou a sessão quando não deveria para o email " + str(email), True)
    
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.escreve_resultado_html(modulo, rot_teste, pag, frag, pretty)

# ----------------------------------------------------------------------
# Executa chamadas
testa_comando_fazer_login("OK", "primeiro@gmail.com", "U-00000001", True)
testa_comando_fazer_login("Erro", "nao_existo@gmail.com", "123456789", False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
