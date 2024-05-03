#! /usr/bin/python3

import obj_comentario

import db_base_sql 
import obj_usuario
import obj_video
import util_testes
from util_erros import erro_prog, mostra, aviso_prog

import sys

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("  Inicializando módulos {usuario} e {video}, limpando tabelas:\n")
obj_usuario.cria_testes(True)
obj_video.cria_testes(True)

sys.stderr.write("  Inicializando módulo {comentario}, limpando tabela, criando comentários para teste:\n")
obj_comentario.inicializa_modulo(True)
obj_comentario.cria_testes(True)

ok_global = True # Vira {False} se um teste falha.

def verifica_comentario(rot_teste, com, ident, atrs_esp):
  """Testes básicos de consistência do objeto {com} da classe {obj_comentario.Classe}, dados
  {ident} e os atributos {atrs_esp} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  teste %s, comentário %s\n" % (rot_teste, ident))
  ok = obj_comentario.verifica_criacao(com, ident, atrs_esp)
  
  if com == None:
    aviso_prog("objeto é {None}, devia ser {%s}" % ident)
  else:
    if type(com) is not obj_comentario.Classe:
      aviso_prog("objeto não é {obj_comentario.Classe}")

    sys.stderr.write("  testando {obj_comentario.obtem_identificador(com)}:\n")
    ident_fun = obj_comentario.obtem_identificador(com)
    if ident_fun != ident:
      aviso_prog("retornou " + str(ident_fun) + ", deveria ter retornado " + str(ident),True)
      ok = False

    sys.stderr.write("  testando {obj_comentario.obtem_atributos(com)}:\n")
    atrs_fun = obj_comentario.obtem_atributos(com)
    if atrs_fun != atrs_esp:
      aviso_prog("retornou " + str(atrs_fun) + ", deveria ter retornado " + str(atrs_esp),True)
      ok = False

    for chave in 'video', 'autor', 'data', 'pai', 'texto':
      sys.stderr.write("  testando {obj_comentario.obtem_atributo(com,%s)}:\n" % chave)
      val_fun = obj_comentario.obtem_atributo(com, chave)
      val_esp = atrs_fun[chave]
      if val_fun != val_esp:
        aviso_prog("retornou " + str(val_fun) + ", deveria ter retornado " + str(val_esp),True)
        ok = False

  sys.stderr.write("  testando {obj_comentario.busca_por_dentificador(%s)}:\n" % ident)
  com_esp = com
  com_fun = obj_comentario.obtem_objeto(ident)
  if com_fun != com_esp:
    aviso_prog("retornou " + str(com_fun) + ", deveria ter retornado " + str(com_esp),True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("  Obtendo alguns comentários para teste:\n")

com1 = obj_comentario.obtem_objeto("C-00000001")
com2 = obj_comentario.obtem_objeto("C-00000002")
com3 = obj_comentario.obtem_objeto("C-00000003")
com4 = obj_comentario.obtem_objeto("C-00000004")
com5 = obj_comentario.obtem_objeto("C-00000005")
com6 = obj_comentario.obtem_objeto("C-00000006")

sys.stderr.write("  Obtendo alguns vídeos para teste:\n")

vid1 = obj_video.obtem_objeto("V-00000001")
vid2 = obj_video.obtem_objeto("V-00000002")
vid3 = obj_video.obtem_objeto("V-00000003")

sys.stderr.write("  Obtendo alguns usuários para teste:\n")

usr1 = obj_usuario.obtem_objeto("U-00000001")
usr2 = obj_usuario.obtem_objeto("U-00000002")
usr3 = obj_usuario.obtem_objeto("U-00000003")

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.cria} sem pai:\n")
vid_cr0 = obj_video.obtem_objeto("V-00000003")
usr_cr0 = obj_usuario.obtem_objeto("U-00000005")
pai_cr0 = None
atrs_cr0 = { 'video': vid_cr0, 'autor': usr_cr0, 'pai': pai_cr0, 'texto': "Que coisa!" }
cmt_cr0 = obj_comentario.cria(atrs_cr0)
indice_cr0 = 7 # Depende de {obj_comentario.cria_testes}.
ident_cr0 = f"C-{indice_cr0:08d}"
verifica_comentario("cr0", cmt_cr0, ident_cr0, atrs_cr0)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.cria} com pai:\n")
vid_cr1 = vid_cr0
usr_cr1 = obj_usuario.obtem_objeto("U-00000002")
pai_cr1 = cmt_cr0
atrs_cr1 = { 'video': vid_cr1, 'autor': usr_cr1, 'pai': pai_cr1, 'texto': "Não diga!" }
cmt_cr1 = obj_comentario.cria(atrs_cr1)
indice_cr1 = indice_cr0 + 1
ident_cr1 = f"C-{indice_cr1:08d}"
verifica_comentario("cr1", cmt_cr1, ident_cr1, atrs_cr1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.busca_por_video()}:\n")

def testa_busca_simples(rot_teste, chave, val, idents_esp):
  """Testes de consistência das funções de busca que devolvem listas de identificadores, dados
  a chave de busca {chave}, o valor de busca {val}, e a lista de identificadores {idents_esp} esperados."""
  sys.stderr.write("  testando {obj_comentario.busca_por_%s(\"%s\")}:\n" % (chave, val))

  ok = True
  if chave == 'video':
    idents_fun = obj_comentario.busca_por_video(val)
  elif chave == 'autor':
    idents_fun = obj_comentario.busca_por_autor(val)
  else:
    assert False, "** função inexistente"

  if sorted(idents_fun) != sorted(idents_esp):
    aviso_prog("retornou " + str(idents_fun) + ", deveria ter retornado " + str(idents_esp),True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# Depende de {obj_comentario.cria_testes}.
id_vid_bv1 = "V-00000001"
testa_busca_simples("bv1", 'video', id_vid_bv1, ( "C-00000001", "C-00000002", "C-00000005", ))

id_vid_bv2 = "V-00000003"
testa_busca_simples("bv2", 'video', id_vid_bv2, ( "C-00000004", "C-00000006", ident_cr0, ident_cr1, ))

id_vid_bv3 = "V-00000004"
testa_busca_simples("bv3", 'video', id_vid_bv3, ())

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.busca_por_autor()}:\n")

id_usr_bu1 = "U-00000003"
testa_busca_simples("bu1", 'autor', id_usr_bu1, ( "C-00000004", "C-00000005", "C-00000006", ))

id_usr_bu2 = "U-00000005"
testa_busca_simples("bu2", 'autor', id_usr_bu2, ( ident_cr0, ))

id_usr_bu3 = "U-00000004"
testa_busca_simples("bu3", 'autor', id_usr_bu3, ( ))

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.obtem_arvore()}:\n")

def testa_obtem_arvore(vid, com):
  """"Testa o metodo obtem arvores, que dado um comentario retorna a arvore de comentarios
  relacionados"""
  vid_id = obj_video.obtem_identificador(vid) if vid != None else None
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  sys.stderr.write("  testando {obj_comentario.obtem_arvore}: {vid} = %s {com} = %s\n" % (vid_id, com_id))
  obj_comentario.liga_diagnosticos(True)

  arvore = obj_comentario.obtem_arvore(vid, com, 10)
  # Deve retornar arvore dos comentarios do video vid a partir do comentario com
  sys.stderr.write("    {obj_comentario.obtem_arvore} retornou " + str(arvore))
  sys.stderr.write("\n")
  imprime_arvore_tuplas(arvore, 4)
  obj_comentario.liga_diagnosticos(False)
  return

def imprime_arvore_tuplas(arv, ind):
  """
  Tenta imprimir a tupla para teste
  <Não funcionando> 
  """
  if arv == None:
    sys.stderr.write("Vazio")
  elif isinstance(arv, str):
    sys.stderr.write("%*s%s\n" % (ind, "", arv))
  elif isinstance(arv, obj_comentario.Classe):
    id = obj_comentario.obtem_identificador(arv)
    sys.stderr.write("%*s%s\n" % (ind, "", id))
  else:
    assert isinstance(arv, list) or isinstance(arv, tuple), "tipo de nó errado"
    obj_raiz = arv[0]
    assert obj_raiz == None or isinstance(obj_raiz, str) or isinstance(obj_raiz, obj_comentario.Classe), "info de nó errado"
    imprime_arvore_tuplas(obj_raiz, ind)
    for subarv in arv[1:]:
      imprime_arvore_tuplas(subarv, ind+2)

testa_obtem_arvore(vid_cr0, None)
testa_obtem_arvore(vid_cr0, cmt_cr0)

testa_obtem_arvore(vid_cr1, None)
testa_obtem_arvore(vid_cr1, cmt_cr1)

for vid in vid1, vid2, vid3:
  testa_obtem_arvore(vid, None)

for com in com1, com2, com3, com4, com5, com6:
  vid = obj_comentario.obtem_atributo(com, 'video')
  testa_obtem_arvore(vid, com)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_comentario.busca_por_campos()}:\n")

def testa_busca_por_campos(rot_teste, args_bus, idents_esp):
  """Testes de consistência da função {busca_por_campos} dado o dicionário {args_bus}
  com as chaves e valores dos campos de busca {chave}, o valor de busca {val},
  e a lista de identificadores {idents_esp} esperados."""
  sys.stderr.write(f"  testando {'{'}obj_comentario.busca_por_campos({str(args_bus)}){'}'}:\n" % )

  ok = True
  
  idents_fun = obj_comentario.busca_por_campos(args_bus)

  if sorted(idents_fun) != sorted(idents_esp):
    sys.stderr.write(f"  retornou {str(idents_fun)}, deveria ter retornado {str(idents_esp)}\n")
    ok = False

  if not ok:
    sys.stderr.write("  ** teste falhou\n")
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# Todos os comentários de teste na base:
coms_todos = [ \
    "C-00000001", "C-00000002", "C-00000003",
    "C-00000004", "C-00000005", "C-00000006",
    "C-00000007", "C-00000008", "C-00000009",
  ]

# Teste passando um id de comentario existente:
args_bus_01 = {"comentario": "C-00000001"}
res_esp_01 = [ "C-00000001", ]
testa_busca_por_campos("comE", res_esp_01, ses, args_bus_01)

# Teste passando um id de comentario inexistente:
args_bus_02 = {"comentario": "C-23000001"}
res_esp_02 = [ ]
testa_busca_por_campos("comN", res_esp_02, ses, args_bus_02)

# Teste sem estar logado:
args_bus_03 = {"video": "V-00000003"}
res_esp_03 = ["C-00000004", "C-00000006", ]
testa_busca_por_campos("logF-vid3", res_esp_03, None, args_bus_03)

# Teste passando um id de video existente:
args_bus_04 = {"video": "V-00000003"}
res_esp_04 = ["C-00000004", "C-00000006", ]
testa_busca_por_campos("vidE", res_esp_04, ses, args_bus_04)

# Teste passando um id de video inexistente:
args_bus_05 = {"video": "V-23000001"}
res_esp_05 = []
testa_busca_por_campos("vidN", res_esp_05, ses, args_bus_05)

# Teste passando um id de autor existente:
args_bus_06 = {"autor": "U-00000001"}
res_esp_06 = [ "C-00000001", "C-00000009", ]
testa_busca_por_campos("autE", res_esp_06, ses, args_bus_06)

# Teste passando um id de autor inexistente:
args_bus_07 = {"autor": "U-23000001"}
res_esp_07 = [ ]
testa_busca_por_campos("autN", res_esp_07, ses, args_bus_07)

# Teste passando um id de comentario pai existente:
args_bus_08 = {"pai": "C-00000001"}
res_esp_08 = [ "C-00000002", ]
testa_busca_por_campos("paiE", res_esp_08, ses, args_bus_08)

# Teste passando um id de comentario existente mas sem filhos:
args_bus_09 = {"pai": "C-00000003"}
res_esp_09 = [ ]
testa_busca_por_campos("paiS", res_esp_09, ses, args_bus_09)

# Teste passando um id de comentario pai inexistente:
args_bus_10 = {"pai": "C-23000001"}
res_esp_10 = [ ]
testa_busca_por_campos("Teste comentario pai inexistente", res_esp_10, ses, args_bus_10)

# Teste passando uma data exata que existe:
com3 = obj_comentario.obtem_objeto("C-00000003");
dat3 = obj_comentario.obtem_atributo(com3, 'data')
args_bus_11 = {"data": dat3}
res_esp_11 = list
testa_busca_por_campos("datP", res_esp_11, ses, args_bus_11)

# Teste passando uma data exata que não existe:
args_bus_12 = {"data": "2024-01-01 08:00:00 UTC"},
res_esp_12 = [ ]
testa_busca_por_campos("datP", res_esp_12, ses, args_bus_12)

# Teste passando data corrente ano+mes:
mes3 = dat3[0:7] # Ano e mes.
args_bus_13 = {"data": mes3}
res_esp_13 = coms_todos
testa_busca_por_campos("mesP", res_esp_13, ses, args_bus_13)

# Teste passando o ano corrente:
args_bus_14 = {"data": "2024"}
res_esp_14 = coms_todos
testa_busca_por_campos("anoP", res_esp_14, ses, args_bus_14)

# Teste passando um texto parcial que existe
args_bus_15 = {"texto": "sobe"}
res_esp_15 = [ "C-00000004" ]
testa_busca_por_campos("texE", res_esp_15, ses, args_bus_15)

# Teste passando um texto que não aparece em nenhum comentário:
args_bus_16 = {"texto": "Superhomem"}
res_esp_16 = [ ]
testa_busca_por_campos("texN", res_esp_16, ses, args_bus_16)

# Teste passando vários parâmetros com resposta única (supõe lógica "E"):
args_bus_17 = {"texto": "talvez", "pai": "C-00000001", "autor": "U-00000002"}
res_esp_17 = [ "C-00000002", ]
testa_busca_por_campos("mulU", res_esp_17, ses, args_bus_17)

# Teste passando vários parâmetros com múltiplas respostas (supõe lógica "E"):
args_bus_18 = {"autor": "U-00000002", "video": "V-00000001"}
res_esp_18 = [ "C-00000002", "C-00000008", ]
testa_busca_por_campos("mulM", res_esp_18, ses, args_bus_18)

# Teste passando vários parâmetros sem resposta (supõe lógica "E"):
args_bus_19 = {"autor": "U-00000002", "video": "V-00000004"}
res_esp_19 = [ ]
testa_busca_por_campos("mulV", res_esp_19, ses, args_bus_19)


# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
