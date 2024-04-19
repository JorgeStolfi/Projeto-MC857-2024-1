#! /usr/bin/python3

import comando_solicitar_pag_alterar_comentario
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_processa(rot_teste, *cmd_args):
    """Testa {comando_solicitar_pag_alterar_comentario.processa(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_solicitar_pag_alterar_comentario
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

aviso_prog("!!! Programa de teste {comando_solicitar_pag_alterar_comentario_TST.py} ainda não escrito !!!")
