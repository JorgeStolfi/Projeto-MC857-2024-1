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
com7 = obj_comentario.obtem_objeto("C-00000007")
com8 = obj_comentario.obtem_objeto("C-00000008")
com9 = obj_comentario.obtem_objeto("C-00000009")

sys.stderr.write("  Obtendo alguns vídeos para teste:\n")

vid1 = obj_video.obtem_objeto("V-00000001")
vid2 = obj_video.obtem_objeto("V-00000002")
vid3 = obj_video.obtem_objeto("V-00000003")

sys.stderr.write("  Obtendo alguns usuários para teste:\n")

usr1 = obj_usuario.obtem_objeto("U-00000001")
usr2 = obj_usuario.obtem_objeto("U-00000002")
usr3 = obj_usuario.obtem_objeto("U-00000003")

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.cria} sem pai:\n")
cr0_vid = obj_video.obtem_objeto("V-00000003")
cr0_usr = obj_usuario.obtem_objeto("U-00000005")
cr0_pai = None
cr0_atrs = { 'video': cr0_vid, 'autor': cr0_usr, 'pai': cr0_pai, 'texto': "Que coisa!" }
cr0_indice = int(obj_comentario.ultimo_identificador()[2:]) + 1 # Índice esperado.
cr0_id = f"C-{cr0_indice:08d}"
cr0_cmt = obj_comentario.cria(cr0_atrs)
verifica_comentario("cr0", cr0_cmt, cr0_id, cr0_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.cria} com pai:\n")
cr1_vid = cr0_vid
cr1_usr = obj_usuario.obtem_objeto("U-00000002")
cr1_pai = cr0_cmt
cr1_atrs = { 'video': cr1_vid, 'autor': cr1_usr, 'pai': cr1_pai, 'texto': "Não diga!" }
cr1_indice = cr0_indice + 1 # Índice esperado.
cr1_id = f"C-{cr1_indice:08d}"
cr1_cmt = obj_comentario.cria(cr1_atrs)
verifica_comentario("cr1", cr1_cmt, cr1_id, cr1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.busca_por_video()}:\n")

def testa_busca_simples(rot_teste, chave, val, idents_esp):
  """Testes de consistência das funções de busca que devolvem listas de identificadores, dados
  a chave de busca {chave}, o valor de busca {val}, e a lista de identificadores {idents_esp} esperados."""
  sys.stderr.write("  %s: testando {obj_comentario.busca_por_%s(\"%s\")}:\n" % (rot_teste, chave, val))

  ok = True
  if chave == 'video':
    sem_pai = False
    # !!! Devia testar também com {sem_pai=True} !!!
    idents_fun = obj_comentario.busca_por_video(val, sem_pai)
  elif chave == 'autor':
    idents_fun = obj_comentario.busca_por_autor(val)
  elif chave == 'data':
    data_ini = val[0];
    data_fin = val[1];
    idents_fun = obj_comentario.busca_por_data(data_ini, data_fin)
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
bv1_vid_id = "V-00000001"
bv1_vid_res_esp = (
    "C-00000001", "C-00000002", "C-00000005", "C-00000007", "C-00000008", "C-00000009",
    "C-00000010", "C-00000011", "C-00000012", "C-00000013", "C-00000014", "C-00000015",
    "C-00000016", 
  )  
testa_busca_simples("bv1", 'video', bv1_vid_id, bv1_vid_res_esp)

bv2_vid_id = "V-00000003"
bv2_vid_res_esp = ( "C-00000004", "C-00000006", cr0_id, cr1_id, )
testa_busca_simples("bv2", 'video', bv2_vid_id, bv2_vid_res_esp)

bv3_vid_id = "V-00000004"
bv3_vid_res_esp = ()
testa_busca_simples("bv3", 'video', bv3_vid_id, bv3_vid_res_esp)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.busca_por_autor()}:\n")

bu1_usr_id = "U-00000003"
bu1_usr_res_esp = ( "C-00000004", "C-00000005", )
testa_busca_simples("bu1", 'autor', bu1_usr_id, bu1_usr_res_esp)

bu2_usr_id = "U-00000005"
bu2_usr_res_esp =  ( 
    "C-00000012", "C-00000013", "C-00000014", "C-00000015", 
    "C-00000016", cr0_id,
  )
testa_busca_simples("bu2", 'autor', bu2_usr_id, bu2_usr_res_esp)

bu3_usr_id = "U-00000006"
bu3_usr_res_esp =  ( )
testa_busca_simples("bu3", 'autor', bu3_usr_id, bu3_usr_res_esp)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.busca_por_data()}:\n")

# Todos os comentários de teste na base:
coms_todos = ( \
    "C-00000001", "C-00000002", "C-00000003",
    "C-00000004", "C-00000005", "C-00000006",
    "C-00000007", "C-00000008", "C-00000009",
    "C-00000010", "C-00000011", "C-00000012",
    "C-00000013", "C-00000014", "C-00000015",
    "C-00000016", cr0_id,       cr1_id,
  )

bd1_data_ini = "2024-04-05 08:00:00 UTC"
bd1_data_fin = "2024-09-30 24:00:00 UTC"
# Interprete o resultado tendo em vista que busca por data é somente em função de intervalo de anos
testa_busca_simples("bd1", 'data', ( bd1_data_ini, bd1_data_fin), coms_todos)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.busca_por_campos()}:\n")

def testa_busca_por_campos(rot_teste, args_bus, idents_esp):
  """Testes de consistência da função {busca_por_campos} dado o dicionário {args_bus}
  com as chaves e valores dos campos de busca {chave}, o valor de busca {val},
  e a lista de identificadores {idents_esp} esperados."""
  sys.stderr.write(f"  {rot_teste}: testando obj_comentario.busca_por_campos({str(args_bus)}):\n")
  ok = True
  
  idents_fun = obj_comentario.busca_por_campos(args_bus)
  if idents_fun == None: idents_fun = ( )
  
  if sorted(idents_fun) != sorted(idents_esp):
    sys.stderr.write(f"  retornou {str(idents_fun)}, deveria ter retornado {str(idents_esp)}\n")
    ok = False

  if not ok:
    sys.stderr.write("  ** teste falhou\n")
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# Video existente:
bcs03_args_bus = { 'video': "V-00000003" }
bcs03_res_esp = ( "C-00000004", "C-00000006", cr0_id, cr1_id, )
testa_busca_por_campos("vid3", bcs03_args_bus, bcs03_res_esp)

# Video inexistente:
bcs05_args_bus = { 'video': "V-23000001" }
bcs05_res_esp = ( )
testa_busca_por_campos("vidN", bcs05_args_bus, bcs05_res_esp)

# Autor existente:
bcs06_args_bus = { 'autor': "U-00000001" }
bcs06_res_esp = (  "C-00000001", "C-00000009", )
testa_busca_por_campos("autE", bcs06_args_bus, bcs06_res_esp)

# Autor inexistente:
bcs07_args_bus = { 'autor': "U-23000001" }
bcs07_res_esp = ( )
testa_busca_por_campos("autN", bcs07_args_bus, bcs07_res_esp)

# Comentario pai existente:
bcs08_args_bus = { 'pai': "C-00000001" }
bcs08_res_esp = (  "C-00000002", )
testa_busca_por_campos("paiE", bcs08_args_bus, bcs08_res_esp)

# Comentario existente mas sem filhos:
bcs09_args_bus = { 'pai': "C-00000003" }
bcs09_res_esp = ( )
testa_busca_por_campos("paiS", bcs09_args_bus, bcs09_res_esp)

# Comentario pai inexistente:
bcs10_args_bus = { 'pai': "C-23000001" }
bcs10_res_esp = ( )
testa_busca_por_campos("paiX", bcs10_args_bus, bcs10_res_esp)

# Intervalo de datas com todos os comentários:
bcs11_data_ini = "2024-01-01 08:00:00 UTC"
bcs11_data_fin = "2024-09-30 08:00:00 UTC"
bcs11_args_bus = { 'data': (bcs11_data_ini, bcs11_data_fin) }
bcs11_res_esp = coms_todos
testa_busca_por_campos("datP", bcs11_args_bus, bcs11_res_esp)

# Intervalo de datas sem comentários
bcs12_data_ini = "2025-01-01 08:00:00 UTC"
bcs12_data_fin = "2025-09-30 08:00:00 UTC"
bcs12_args_bus = { 'data': (bcs12_data_ini, bcs12_data_fin) }
bcs12_res_esp = ( )
 
testa_busca_por_campos("datP", bcs12_args_bus, bcs12_res_esp)

# # Data parcial:
# bcs13_data_pat = "*05-17*"
# bcs13_args_bus = { 'data': bcs13_data_pat }
# bcs13_res_esp = coms_todos
# testa_busca_por_campos("mesP", bcs13_args_bus, bcs13_res_esp)

# Texto parcial que existe
bcs15_args_bus = { 'texto': "*sobe*" }
bcs15_res_esp = (  "C-00000004" , )
testa_busca_por_campos("texE", bcs15_args_bus, bcs15_res_esp)

# Texto parcial que não ocorre em nenhum comentário:
bcs16_args_bus = { 'texto': "*Superhomem*" }
bcs16_res_esp = ( )
testa_busca_por_campos("texN", bcs16_args_bus, bcs16_res_esp)

# Múltiplos parâmetros com resposta única (supõe lógica "E"):
bcs17_args_bus = { 'texto': "talvez", 'pai': "C-00000001", 'autor': "U-00000002" }
bcs17_res_esp = (  "C-00000002", )
testa_busca_por_campos("mulU", bcs17_args_bus, bcs17_res_esp)

# Múltiplos parâmetros com múltiplas respostas (supõe lógica "E"):
bcs18_args_bus = { 'autor': "U-00000002", 'video': "V-00000001" }
bcs18_res_esp = (  "C-00000002", "C-00000008", )
testa_busca_por_campos("mulM", bcs18_args_bus, bcs18_res_esp)

# Múltiplos parâmetros sem resposta (supõe lógica "E"):
bcs19_args_bus = { 'autor': "U-00000002", 'video': "V-00000004" }
bcs19_res_esp = ( )
testa_busca_por_campos("mulV", bcs19_args_bus, bcs19_res_esp) 

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.obtem_conversa()}:\n")

def testa_obtem_conversa(raizes, max_coms=10, max_nivel=10):
  """
  Faltando adicionar as verificações corretamente, atualmente só executa e printa
  """
  sys.stderr.write(f"Obtem de {str(raizes)} {max_coms} comentarios, no maximo em {max_nivel} niveis \n")
  conversa_video = obj_comentario.obtem_conversa(raizes, max_coms, max_nivel)
  sys.stderr.write(str(conversa_video) + "\n")

testa_obtem_conversa([com1.id, com3.id, com8.id], 5, 10)
testa_obtem_conversa([com1.id, com8.id], 2, 10)
testa_obtem_conversa([com1.id, com8.id], 3, 10)
testa_obtem_conversa([com1.id, com8.id], 4, 10)
testa_obtem_conversa([com1.id, com8.id], 10, 1)
testa_obtem_conversa([com1.id, com8.id], 10, 2)
testa_obtem_conversa([com1.id, com8.id], 7, 3)

# ----------------------------------------------------------------------
sys.stderr.write("%s\n" % ("=" * 70))
sys.stderr.write("  testando {obj_comentario.obtem_arvore()}:\n")

def testa_obtem_arvore(rot_teste, vid, com):
  """"Testa o metodo obtem arvores, que dado um comentario retorna a arvore de comentarios
  relacionados"""
  vid_id = obj_video.obtem_identificador(vid) if vid != None else None
  com_id = obj_comentario.obtem_identificador(com) if com != None else None
  sys.stderr.write("  %s: testando {obj_comentario.obtem_arvore}: {vid} = %s {com} = %s\n" % (rot_teste, vid_id, com_id))
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

# Chamadas comentadas pois o metodo obtem_arvore não é mais público em obj_comentario

# testa_obtem_arvore("CR0_V", cr0_vid, None)
# testa_obtem_arvore("CR0_VP", cr0_vid, cr0_cmt)

# testa_obtem_arvore("CR1_V", cr1_vid, None)
# testa_obtem_arvore("CR1_VP", cr1_vid, cr1_cmt)

# for vid in vid1, vid2, vid3:
#   vid_id = obj_video.obtem_identificador(vid)
#   rot_teste = f"CR_{vid_id}"
#   testa_obtem_arvore(rot_teste, vid, None)

# for com in com1, com2, com3, com4, com5, com6:
#   com_id = obj_comentario.obtem_identificador(com)
#   vid = obj_comentario.obtem_atributo(com, 'video')
#   vid_id = obj_video.obtem_identificador(vid)
#   rot_teste = f"CR_{vid_id}_{com_id}"
#   testa_obtem_arvore(vid, com)


# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
