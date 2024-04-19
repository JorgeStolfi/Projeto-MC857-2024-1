#! /usr/bin/python3
# Teste do módulo {tabelas}

import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import obj_video

import sys

# ----------------------------------------------------------------------

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

sys.stderr.write("  Abrindo as tabelas...\n")
db_tabelas_do_sistema.inicializa_todas(False)
db_tabelas_do_sistema.cria_todos_os_testes(True)

# ----------------------------------------------------------------------
sys.stderr.write("  Verificando tabela \"usuarios\" usr = %s\n" % "usr1") 

usr1_id = "U-00000001"
usr1 = obj_usuario.busca_por_identificador(usr1_id)
assert usr1 != None
usr1_atrs = obj_usuario.obtem_atributos(usr1)
obj_usuario.verifica_criacao(usr1, usr1_id, usr1_atrs)

assert usr1 == db_tabelas_do_sistema.identificador_para_objeto(usr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("  Verificando tabela \"sessoes\", ses = %s\n" % "ses1") 

ses1_id = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(ses1_id)
assert ses1 != None
ses1_atrs = obj_sessao.obtem_atributos(ses1)
obj_sessao.verifica_criacao(ses1, ses1_id, ses1_atrs)

assert ses1 == db_tabelas_do_sistema.identificador_para_objeto(ses1_id)

# ----------------------------------------------------------------------
sys.stderr.write("  Verificando tabela \"videos\", ses = %s\n" % "ses1") 

vid1_id = "V-00000001"
vid1 = obj_video.busca_por_identificador(vid1_id)
assert vid1 != None
vid1_atrs = obj_video.obtem_atributos(vid1)
obj_video.verifica_criacao(vid1, vid1_id, vid1_atrs)

assert vid1 == db_tabelas_do_sistema.identificador_para_objeto(vid1_id)

sys.stderr.write("\n")

sys.stderr.write("Testes terminadosnormalmente.\n")
