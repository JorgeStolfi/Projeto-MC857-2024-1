#! /usr/bin/python3

# Interfaces usadas por este script:

import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import obj_video
import obj_raiz
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

def testa_comando_fazer_upload_video(rotulo, valido, ses, cmd_args):
  global ok_global

  modulo = comando_fazer_upload_video
  funcao = modulo.processa
  
  ok = True

  id_ses = obj_sessao.obtem_identificador(ses) if ses != None else None
  sys.stderr.write("-"*70 + "\n")
  sys.stderr.write(f"testando {funcao} rotulo = {rotulo} ses = {str(id_ses)} cmd_args = {str(cmd_args)}\n")

  ult_id_antes = obj_raiz.ultimo_identificador("videos", "V")
  pag = funcao(ses, cmd_args)
  ult_id_depois = obj_raiz.ultimo_identificador("videos", "V")
  sys.stderr.write(f"  ultimo id antes = {ult_id_antes} depois = {ult_id_depois}\n")
  
  if ult_id_depois == ult_id_antes:
    sys.stderr.write(f"  comando não criou novo video\n")
    if valido:
      sys.stderr.write(f"  ** deveria ter criado!\n")
      ok = False
    else:
      sys.stderr.write(f"  como esperado\n")
  else:
    id_vid = ult_id_depois
    sys.stderr.write(f"  comando criou novo video, id = {id_vid}\n")
    if not valido:
      sys.stderr.write(f"  ** deveria ter falhado!\n")
      ok = False

    # Verifica os atributos do vídeo criado:
    vid_criado = obj_video.busca_por_identificador(id_vid)
    assert vid_criado != None
    atrs_criado = obj_video.obtem_atributos(vid_criado)
    sys.stderr.write(f"  atributos criados = {str(atrs_criado)}\n")
    for chave in cmd_args.keys():
      if chave == 'id_usuario': 
        val_criado = obj_usuario.obtem_identificador(vid_args['autor'])
      else:
        val_criado = atrs_criado[chave] if vid_criado != None else None
      val_dados = cmd_args[chave]
      if val_criado != val_dados:
        sys.stderr.write(f"  ** atributo '{chave}' não bate: {str(val_criado)}, {str(val_dados)}\n")
        ok = False
   
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  util_testes.escreve_resultado_html(modulo, rotulo, pag, frag, pretty)

  if not ok:
    aviso_prog("teste falhou", True)
    ok_global = False

  sys.stderr.write("-"*70 + "\n")
  return

# ----------------------------------------------------------------------
# Algumas sessões para teste:
ses_admin1 = obj_sessao.busca_por_identificador("S-00000001") # Do administrador.
ses_comum1 = obj_sessao.busca_por_identificador("S-00000003") # De um plebeu.
ses_comum2 = obj_sessao.busca_por_identificador("S-00000004") # De outro plebeu.

# Obtém alguns usuários:
usr_admin1 = obj_sessao.obtem_usuario(ses_admin1)
assert obj_usuario.obtem_atributo(usr_admin1, 'administrador')

usr_comum1 = obj_sessao.obtem_usuario(ses_comum1)
assert not obj_usuario.obtem_atributo(usr_comum1, 'administrador')

usr_comum2 = obj_sessao.obtem_usuario(ses_comum2)
assert not obj_usuario.obtem_atributo(usr_comum2, 'administrador')
assert usr_comum2 != usr_comum1 

# ----------------------------------------------------------------------
# Testa com dados OK:
dados_OK = { \
  'arq': "banana",
  'titulo': "Bananas cibernéticas",
}
testa_comando_fazer_upload_video("OK", True, ses_comum1, dados_OK)

# Testa com arquivo repetido:
dados_Earq = { \
  'autor': usr_comum2,
  'arq': "banana",
  'titulo': "Bananas psicossomáticas",
}
testa_comando_fazer_upload_video("Earq", False, ses_comum2, dados_Earq)

# Testa com usuário de outra sessão:
dados_Eses = { \
  'autor': usr_comum1,
  'arq': "pitmat",
  'titulo': "Pitangas matemáticas",
}
testa_comando_fazer_upload_video("Eses", False, ses_comum2, dados_Eses)

# Testa com usuário não logado:
dados_Elog = { \
  'autor': usr_comum1,
  'arq': "goiorg",
  'titulo': "Goiabas organolépticas",
}
testa_comando_fazer_upload_video("Eses", False, None, dados_Elog)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("Teste falhou")
