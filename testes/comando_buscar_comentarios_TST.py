#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_comentarios
import obj_sessao
import obj_usuario
import obj_video
import obj_comentario
import util_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_processa(rot_teste, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_buscar_comentarios
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

assert False, "!!! comand_buscar_comentarios_TST.py ainda não escrito !!!"

sys.stderr.write("Testes terminados normalmente.")