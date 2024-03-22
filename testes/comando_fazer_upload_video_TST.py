#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes; from util_testes import erro_prog, aviso_prog, mostra
import comando_fazer_upload_video

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_fazer_upload_video(rotulo, dados):
  global ok_global
  modulo = comando_fazer_upload_video
  pag = modulo.processa(None, dados)
   
  frag = False     # Resultado não é fragmento, é página completa.
  pretty = False   # Não tente deixar o HTML legível.
  util_testes.escreve_resultado_html(modulo, rotulo, pag, frag, pretty)

  vid_criado_id = obj_video.busca_por_email(dados["arq"])
  vid_criado_obj = obj_video.busca_por_identificador(vid_criado_id)
  vid_criado_atrs = obj_video.obtem_atributos(vid_criado_obj) if vid_criado_obj != None else None
  sys.stderr.write(f"  video criado = {vid_criado_id} atrs = {vid_criado_atrs}\n")
  
  for chave in dados.keys():
    if chave == 'id_usr': 
      val_criado = obj_usuario.obtem_identificador(val_criado_args['usr'])
    else:
      val_criado = vid_criado_atrs[chave]
    val_dados = dados[chave]
    if val_criado != val_dados:
      ok_global = False
      aviso_prog(f"atributo '{chave}' não bate: {str(val_criado)}, {str(val_dados)}", True)
 
# Obtém um usuário comum (não administrador):
usr1 = obj_usuario.busca_por_identificador("U-00000003")
assert not obj_usuario.objtem_atributo(usr1, 'administrador')

# ----------------------------------------------------------------------
# Testa com dados OK:
dados_ok = { \
  'usr': usr1,
  'arq': "banana",
  'titulo': "Bananas ciberbnéticas",
}
testa_comando_fazer_upload_video("OK", dados_ok, True)

# Testa com arquivo repetido:
dados_erro = { \
  'usr': usr1,
  'fruta': "banana",
  'titulo': "Bananas ciberbnéticas",
}
testa_comando_fazer_upload_video("Erro", dados_erro, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("- teste falhou")
