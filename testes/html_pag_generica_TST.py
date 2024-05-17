#! /usr/bin/python3

import html_pag_generica
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.
 
def testa_gera(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""
  
  global ok_global
  modulo = html_pag_generica
  funcao = modulo.gera
  frag = False  # Resultado é só um fragmento de página?
  pretty = True  # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
# Sessão de administrador para teste:
sesA_id = "S-00000001"
sesA = obj_sessao.obtem_objeto(sesA_id)
assert sesA != None
assert obj_sessao.de_administrador(sesA)

# Sessão de usuário comum para teste:
sesC_id = "S-00000003"
sesC = obj_sessao.obtem_objeto(sesC_id)
assert sesC != None
assert not obj_sessao.de_administrador(sesC)

for xses, ses in ("N", None), ("A", sesA), ("C", sesC):
  for xerr, erros in ("N", None), ("E", ""), ("V", []), ("L", ["Vergonha!", "Onde se viu!"]):
    conteudo = "<ul><li>UM</li><li>DOIS</li></ul>"
    rot_teste = f"ses{xses}_err{xerr}"
    testa_gera(rot_teste, str, ses, conteudo, erros)

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
