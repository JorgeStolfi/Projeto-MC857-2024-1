import comando_solicitar_pag_buscar_videos
import db_tabelas
import obj_sessao
import obj_video
import db_base_sql
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessões de teste
ses_comum = obj_sessao.busca_por_identificador("S-00000001")

# Obtém um usuário administrador
admin = obj_video.busca_por_identificador("U-00000001")
assert obj_video.obtem_atributo(admin, 'administrador')
ses_admin = obj_sessao.cria(admin, "NOPQRSTUVWX")

def testa_processa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_solicitar_pag_buscar_videos
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa_processa("NL-e0", None, None)
testa_processa("NA-e2", ses_comum, ["banana", "abacate"])
testa_processa("OK-e0", ses_admin, None)
testa_processa("OK-e2", ses_admin, ["Roubar", "Mentir"])
