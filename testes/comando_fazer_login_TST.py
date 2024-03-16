#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes; from util_testes import erro_prog, aviso_prog, mostra
import comando_fazer_login

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_fazer_login(rotulo, email, senha, deveria_logar):
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
    aviso_prog("Gerou a sessão quando não deveria para o email " + str(email) + " com senha " + str(senha), True)
    
  frag = False     # Resultado não é fragmento, é página completa.
  pretty = False   # Não tente deixar o HTML legível.
  util_testes.escreve_resultado_html(modulo, rotulo, pag, frag, pretty)

# ----------------------------------------------------------------------
# Executa chamadas
testa_comando_fazer_login("OK", "primeiro@gmail.com", "11111111", True)
testa_comando_fazer_login("Erro_Email", "nao_existo@gmail.com", "123456789", False)
testa_comando_fazer_login("Erro_Senha", "primeiro@gmail.com", "123456789", False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro na geração da sessão\n")
else:
  erro_prog("- teste falhou")
