#! /usr/bin/python3

import db_base_sql
import db_tabelas
import comando_ver_comentarios
import obj_sessao
import util_testes
import obj_usuario

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

def testa_processa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_comentarios
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.busca_por_identificador(ses_adm_id)

# Teste passando um id do video
id_video = {'id_video': "V-00000002"}

testa_processa("id_video",        ses_adm, id_video)

sys.stderr.write("Testes terminados normalmente.")
