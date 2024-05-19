#! /usr/bin/python3

import comando_alterar_comentario
import db_tabelas_do_sistema
import obj_comentario
import obj_usuario
import obj_sessao
import obj_video
import db_base_sql
import util_dict
import util_testes
from util_erros import ErroAtrib, aviso_prog

import re
import sys

# Conecta o banco e carrega as informações para o teste
sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True # Vira {False} se algum teste falha.

def testa_processa(rot_teste, res_esp, *args):
  """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, e grava esse resultado
  em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

  global ok_global
  modulo = comando_alterar_comentario
  funcao = modulo.processa
  frag = False # Resultado é só um fragmento de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  ok = util_testes.testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args)
  ok_global = ok_global and ok
  return ok
  
def verifica_atributos(com, atrs_esp):
  """Verifica se os atributos do comentário {com} foram alterados
  conforme o dicionário {atrs_esp}. """
  global ok_global
  
  sys.stderr.write(f"    verificando o efeito:\n")

  ok = True
  atrs_esp = util_dict.para_identificadores(atrs_esp.copy()) # Para não estragar o original.
  
  # Confere e elimina 'comentario' de {atrs_esp}:
  com_id = obj_comentario.obtem_identificador(com)
  atrs_atu = util_dict.para_identificadores(obj_comentario.obtem_atributos(com))
  if 'comentario' in atrs_esp:
    com_id_mod = atrs_esp['comentario'];
    if com_id_mod != obj_comentario.obtem_identificador(com):
      sys.stderr.write(f"    identificador incorreto {com_id} != {com_id_mod}\n")
      ok = False
    atrs_esp.pop('comentario')
    
  # Confere demais campos:
  for chave, val in atrs_atu.items():
    if chave in atrs_esp:
      if atrs_esp[chave] != atrs_atu[chave]:
        xatu = re.sub("\n", r"\\n", str(atrs_atu[chave]))
        xesp = re.sub("\n", r"\\n", str(atrs_esp[chave]))
        sys.stderr.write(f"    valor de '{chave}' NÃO bate «{xatu}» != «{xesp}»\n")
        ok = False
      atrs_esp.pop(chave)

  if atrs_esp != dict():
    sys.stderr.write(f"    campos espúrios em {'{'}atrs_esp{'}'} = {atrs_esp}\n")
    ok = False
    
  if ok: 
    sys.stderr.write(f"    CONFERE!\n")
  else:
    sys.stderr.write(f"    ** teste falhou\n")
  
  sys.stderr.write(f"  {('~'*70)}\n")


  ok_global = ok_global and ok
  return ok

# Obtem sessao de teste
ses = obj_sessao.obtem_objeto("S-00000001")
assert obj_sessao.de_administrador(ses)


# Comentarios existentes para teste(criados por obj_comentario.cria_testes)
# 
# ( "C-00000001", "V-00000001", "U-00000001", None,         "Supimpa!\nDeveras!", ),
# ( "C-00000002", "V-00000001", "U-00000002", "C-00000001", "Né não! Acho... Talvez...", ),
# ( "C-00000003", "V-00000002", "U-00000002", None,         "Falta sal.", ),
# ( "C-00000004", "V-00000003", "U-00000003", None,         "Soberbo!", ),
# ( "C-00000005", "V-00000001", "U-00000003", "C-00000002", "É sim!", ),
# ( "C-00000006", "V-00000003", "U-00000003", None,         "Supercílio! " + "k"*60, ),


# comentario de teste:
com1_id = "C-00000001"
com1 = obj_comentario.obtem_objeto(com1_id)
assert com1 != None

sys.stderr.write("\n")

sys.stderr.write("  tentativa de alteração do campo 'texto' apenas, deve dar certo:\n")
cmd_args_01 = { 'comentario': com1_id,  'texto': "Texto Novo", }
testa_processa("T1", str, ses, cmd_args_01)
verifica_atributos(com1, cmd_args_01) # Deve ter alterado.

sys.stderr.write("  tentativa de alteração do campo 'video', deve falhar:\n")
com1_atrs = obj_comentario.obtem_atributos(com1) # Atributos atuais.
cmd_args_02 = { 'comentario': com1_id, 'video': "V-00000002", 'texto': "Retiro o que disse" }
testa_processa("T2", str, ses, cmd_args_02)
verifica_atributos(com1, com1_atrs) # Não devem ter mudado.

sys.stderr.write("  tentativa de alteração do campo 'autor', deve falhar:\n")
com1_atrs = obj_comentario.obtem_atributos(com1) # Atributos atuais.
cmd_args_03 = { 'comentario': com1_id, 'autor': "U-00000003", 'texto': "Pensando bem..." }
testa_processa("T3", str, ses, cmd_args_03)
verifica_atributos(com1, com1_atrs) # Não devem ter mudado.

sys.stderr.write("  tentativa de alteração com campos imutaveis iguais aos atuais, deve dar certo:\n")
com1_atrs = obj_comentario.obtem_atributos(com1) # Atributos atuais.
cmd_args_04 = { 'comentario': com1_id,  }
cmd_args_04['video'] = obj_video.obtem_identificador(com1_atrs['video']) 
cmd_args_04['autor'] = obj_usuario.obtem_identificador(com1_atrs['autor']) 
cmd_args_04['pai'] = obj_comentario.obtem_identificador(com1_atrs['pai']) if com1_atrs['pai'] != None else None 
cmd_args_04['texto'] = "Ora bolas!"
testa_processa("T4", str, ses, cmd_args_04)
verifica_atributos(com1, cmd_args_04) # Devem ter mudado.

sys.stderr.write("  tentativa de alteração do campo 'nota' apenas, deve dar certo:\n")
cmd_args_05 = { 'comentario': com1_id,  'nota': 2.5, }
testa_processa("T5", str, ses, cmd_args_05)
verifica_atributos(com1, cmd_args_05) # Deve ter alterado.

# Nova sessão para teste de aleração quando usuário não é administrador.
nova_sessao = obj_sessao.obtem_objeto("S-00000002")
sys.stderr.write("  tentativa de alteração do campo 'nota' apenas, sem ser administrador, deve dar errado:\n")
com1_atrs = obj_comentario.obtem_atributos(com1) # Atributos atuais.
cmd_args_06 = { 'comentario': com1_id,  'nota': 2.5, }
try:
  testa_processa("T6", str, ses, cmd_args_06)
except:
  sys.stderr.write("Falha esperada: Usuário não é administrador\n")

verifica_atributos(com1, com1_atrs) # Não deve ter mudado.

sys.stderr.write("  tentativa de alteração do campo 'texto' com o comentário bloqueado, deve falhar:\n")
ses_comum = obj_sessao.obtem_objeto("S-00000005")
obj_comentario.muda_atributos(com1, { 'bloqueado': True } )
com1_atrs = obj_comentario.obtem_atributos(com1)
testa_processa("T5", str, ses_comum, cmd_args_01)
verifica_atributos(com1, com1_atrs) # Não devem ter mudado.

sys.stderr.write("  tentativa de alteração do campo 'texto' com o comentário bloqueado mas com sessão de adm, deve dar certo:\n")
testa_processa("T6", str, ses, cmd_args_01)
verifica_atributos(com1, cmd_args_01) # Deve ter alterado.

if ok_global:
  sys.stderr.write("Teste terminado normalmente\n")
else:
  aviso_prog("Alguns testes falharam.", True)
