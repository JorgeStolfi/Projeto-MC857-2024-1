#! /usr/bin/python3
import sys
import comando_ver_sessoes
import db_base_sql
import db_tabelas
import obj_usuario
import obj_sessao
import util_testes

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessão de usuário comum:

# Sessão de usuário administrador
ses4 = obj_sessao.busca_por_identificador("S-00000003")

# Usuário a examinar: 

def testa_comando_ver_sessoes(rotulo, *cmd_args):
    """Testa {funcao(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_sessoes
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *cmd_args)

# Sessão de usuário comum:
ses1 = obj_sessao.busca_por_identificador("S-00000004")
assert not obj_sessao.eh_administrador(ses1)
usr1 = obj_sessao.obtem_usuario(ses1)
usr1_id = obj_usuario.obtem_identificador(usr1)
testa_comando_ver_sessoes("teste1-N", ses1, {} )  
testa_comando_ver_sessoes("teste1-U", ses1, {'id_usuario': usr1_id } )  

# Administrador olhando suas sessões:
ses2 = obj_sessao.busca_por_identificador("S-00000002")
assert obj_sessao.eh_administrador(ses2)
usr2_id = "U-00000002"
testa_comando_ver_sessoes("teste2-N", ses2, {} )  
testa_comando_ver_sessoes("teste2-U", ses2, {'id_usuario': usr2_id } )  

sys.stderr.write("Testes terminados normalmente.\n")
