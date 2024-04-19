#! /usr/bin/python3

import sys
import comando_buscar_videos_de_usuario
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# Usuário a examinar: 

def testa_comando_buscar_videos_de_usuario(rot_teste, *cmd_args):
    """Testa {funcao(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_buscar_videos_de_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)


id_ses = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(id_ses)

# Sessão de usuário comum:
testa_comando_buscar_videos_de_usuario("teste1", ses1, {'usuario': '1'})  

sys.stderr.write("Testes terminados normalmente.\n")
 
