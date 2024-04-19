#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
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
db_tabelas_do_sistema.cria_todos_os_testes(True)

def testa_processa(rot_teste, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_buscar_usuarios
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.busca_por_identificador(ses_adm_id)
assert obj_sessao.de_administrador(ses_adm), f"sessão {ses_adm_id} não é de administrador" 

# Testa com busca por identificador_que existe:
args_id_usr = {'usuario': "U-00000002"}

# Testa com busca por email que existe:
args_email = {'email': "primeiro@gmail.com"}

# Testa com busca por nome que existe:
args_nome = {'nome': "João Segundo"}

# Testa com busca por email que não existe:
args_email_no = {'email': "naoexiste@email.com"}

# Testa com busca por primeiro nome:
args_primeiro_nome = {'nome': "João"}

# Testa com busca por sobrenome:
args_sobrenome = {'nome': "Segundo"}

# Testa com nome aproximado:
args_nome_aproximado = {'nome': "joão segundo"}

# Testa com nome parcial:
args_nome_parcial = {'nome': "jo"}

testa_processa("usuario",        ses_adm, args_id_usr)
testa_processa("email_ok",      ses_adm, args_email)
testa_processa("email_no",      ses_adm, args_email_no)

# Testes abaixo devem retornar somente "João Segundo"
testa_processa("nome",          ses_adm, args_nome)
testa_processa("primeiro_nome", ses_adm, args_primeiro_nome)
testa_processa("sobrenome", ses_adm, args_sobrenome)
testa_processa("nome_aproximado", ses_adm, args_nome_aproximado)

# Teste abaixo deve retornar todos usuários que começam com "Jo"
# (José Primeiro, João Segundo, Josenildo Quinto, Joaquim Oitavo e Jonas Nono)
testa_processa("nome_parcial", ses_adm, args_nome_parcial)

sys.stderr.write("Testes terminados normalmente.")
