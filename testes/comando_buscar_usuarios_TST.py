#! /usr/bin/python3

import db_base_sql
import db_tabelas
import comando_buscar_usuarios
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

    modulo = comando_buscar_usuarios
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.busca_por_identificador(ses_adm_id)
assert obj_sessao.eh_administrador(ses_adm), f"sessão {ses_adm_id} não é de administrador" 

# Testa com busca por identificador_que existe:
args_id_usr = {'id_usuario': "U-00000002"}

# Testa com busca por email que existe:
args_email = {'email': "primeiro@gmail.com"}

# Testa com busca por nome que existe:
args_nome = {'nome': "João Segundo"}

# Testa com busca por email que não existe:
args_email_no = {'email': "naoexiste@email.com"}

testa_processa("id_usuario",        ses_adm, args_id_usr)
testa_processa("email_ok",      ses_adm, args_email)
testa_processa("email_no",      ses_adm, args_email_no)
testa_processa("nome",          ses_adm, args_nome)

sys.stderr.write("Testes terminados normalmente.")
