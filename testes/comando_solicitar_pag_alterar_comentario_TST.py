#! /usr/bin/python3

import comando_solicitar_pag_alterar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_solicitar_pag_alterar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

ses_admin = obj_sessao.obtem_objeto("S-00000001")
ses_comum = obj_sessao.obtem_objeto("S-00000003")

# Testa erro de sessão inválida
testa_processa(" str, sessaoInvalida",  str, None, {})

# Testa erro de comentário não especificado
testa_processa("comentarioNaoEspecificado",  str, ses_admin, {})

# Testa erro de comentário não existente
id_comentario_nao_existente = 'C-01010101'
testa_processa("comentarioNaoExistente",  str, ses_admin, { 'comentario': id_comentario_nao_existente })

# Testa erro de permissão para alterar comentário
id_comentario_outro_usuario = 'C-00000001'
testa_processa("usuarioSemPermissao",  str, ses_comum, { 'comentario': id_comentario_outro_usuario })

# Teste de gerar página para alterar um comentário
id_comentario_existente = 'C-00000001'
testa_processa("exibePaginaAlterarComentario",  str, ses_admin, { 'comentario': id_comentario_existente })

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)
