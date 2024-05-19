#! /usr/bin/python3

import db_base_sql
import comando_ver_conversa
import db_tabelas_do_sistema
import obj_sessao
import obj_comentario
import util_testes
from util_erros import erro_prog, aviso_prog, mostra

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
  
  global ok_global
  modulo = comando_ver_conversa
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem uma sessao de um usuario que é de administrador:
ses_A1 = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses_A1)

# Obtem uma sessao de um usuario comum:
ses_C1 = obj_sessao.obtem_objeto("S-00000003")
assert not obj_sessao.de_administrador(ses_C1)

# Usuário não logado
testa_processa("nao_logado", str, None, {'comentario': 'C-00000001', 'max_coms': 100, 'max_nivels': 100})

# Usuário logado comum com id válido
testa_processa("comum_valido", str, ses_C1, {'comentario': 'C-00000001', 'max_coms': 100, 'max_nivels': 100})

# Usuário logado admin com id válido
testa_processa("admin_valido", str, ses_A1, {'video': 'V-00000001', 'max_coms': 100, 'max_nivels': 100})

# Sem nenhum id
testa_processa("sem_id", str, ses_A1, {})

# Com ambos id de vídeo e comentário
testa_processa("com_dois_ids", str, ses_A1, {'comentario': 'C-00000001', 'video': 'V-00000002', 'max_coms': 100, 'max_nivels': 100})

# Com id de vídeo inválido
testa_processa("id_video_invalido", str, ses_A1, {'video': 'V-02222222', 'max_coms': 100, 'max_nivels': 100})

# Com id de comentário inválido
testa_processa("id_comentario_invalido", str, ses_A1, {'comentario': 'C-01111111', 'max_coms': 100, 'max_nivels': 100})

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
