#! /usr/bin/python3

import comando_alterar_video
import db_tabelas_do_sistema
import obj_video
import obj_sessao
import db_base_sql
import util_testes
from util_erros import erro_prog, aviso_prog

import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, compara com {res_esp}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_alterar_video
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok

# Obtem sessao de teste
ses = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses)

# Video 
vid_id = 'V-00000001'

# Teste para validar o erro de sessão inválida
testa_processa("SessaoInvalida", str, None, { 'video': vid_id })

# Teste para validar um video inválido
testa_processa("VideoInvalido", str, ses, { 'video': None })

# Teste para validar mensagem de alteração não autorizada
ses_nao_admin = obj_sessao.obtem_objeto("S-00000003")
testa_processa("NaoAutorizado", str, ses_nao_admin, { 'video': vid_id })

# Teste para validar erro ao alterar vídeo
testa_processa("ErroAoAlterar", str, ses, { 'video': vid_id, 'titulo': '' })

# Teste para alterar um vídeo com sucesso
video_attrs = obj_video.obtem_atributos(obj_video.obtem_objeto(vid_id))
novo_titulo = 'Novo Titulo'
data_do_video = video_attrs['data']
autor_do_video = video_attrs['autor']

testa_processa("AlteraComSucesso", str, ses, { 'video': vid_id, 'titulo': novo_titulo, 'data': data_do_video, 'autor': autor_do_video })
video_atributos_atualizados = obj_video.obtem_atributos(obj_video.obtem_objeto(vid_id))

titulo_atualizou = video_atributos_atualizados['titulo'] == novo_titulo
assert titulo_atualizou
ok_global = ok_global and titulo_atualizou


if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)
