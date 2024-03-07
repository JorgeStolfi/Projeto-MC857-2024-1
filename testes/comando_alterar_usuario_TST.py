#! /usr/bin/python3

import comando_alterar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste


sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")


def testa_alteracao(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


def testa_atualiza_nome_com_sucesso():
    novo_nome = "John First"
    args = {
        'id_usuario': "U-00000001",
        'nome': novo_nome,
    }
    testa_alteracao("Nom", ses, args)

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "nome") == novo_nome, "nome não atualizado"

def testa_atualiza_email_com_sucesso():
    email_novo = "banana@nanica.com"
    args = {
        'id_usuario': "U-00000001",
        'email': email_novo,
    }
    testa_alteracao("Ema", ses, args)

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "email") == email_novo, "email não atualizado"

def testa_atualiza_email_repetido_falha():
    email_dup = "segundo@ic.unicamp.br"
    args = {
        'id_usuario': "U-00000001",
        'email': email_dup,
    }
    testa_alteracao("Dup", ses, args)

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "email") != email_dup, "email duplicado aceito"

# Executa os testes

testa_atualiza_nome_com_sucesso()
testa_atualiza_email_com_sucesso()
testa_atualiza_email_repetido_falha()
