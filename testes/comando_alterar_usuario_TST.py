#! /usr/bin/python3

import sys #mudança de linha
sys.path.insert (0, "/home/cc2018-ceb/ra074126/Downloads/Projeto_2024_03_15/Projeto-MC857-2024-1") #linha acrescentada


import comando_alterar_usuario
import db_tabelas
import obj_usuario
import obj_sessao
import db_base_sql
import util_testes
from util_valida_campo import ErroAtrib

#import sys #linha original


# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessao de teste
ses = obj_sessao.busca_por_identificador("S-00000001")

def testa_comando_alterar_usuario(rotulo, *args):
    """Testa {funcao(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


def testa_atualiza_nome_com_sucesso():
    novo_nome = "John First"
    cmd_args = {
        'id_usr': "U-00000001",
        'nome': novo_nome,
    }
    testa_comando_alterar_usuario("Nom", ses, cmd_args)

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "nome") == novo_nome, "nome não atualizado"

def testa_atualiza_email_com_sucesso():
    email_novo = "banana@nanica.com"
    cmd_args = {
        'id_usr': "U-00000001",
        'email': email_novo,
    }
    testa_comando_alterar_usuario("Ema", ses, cmd_args)

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "email") == email_novo, "email não atualizado"

def testa_atualiza_email_repetido_falha():
    email_dup = "segundo@ic.unicamp.br"
    cmd_args = {
        'id_usr': "U-00000001",
        'email': email_dup,
    }
    try:
      testa_comando_alterar_usuario("Dup", ses, cmd_args)
    except ErroAtrib as ex:
      msg = ex.atrs[0]
      mostra(4, f"testa_comando_alterar_usuario: erro = \"{str(msg)}\"")
      sys.stderr.write("    (erro esperado)\n")

    updated_user = obj_usuario.busca_por_identificador("U-00000001")

    assert obj_usuario.obtem_atributo(updated_user, "email") != email_dup, "email duplicado aceito"

'''
#acrescentei o teste da função msg_campo_obrigatorio(nome_do_campo) *falta implementar
def testa_msg_campo_obrigatorio():
    modulo = comando_alterar_usuario
    funcao = modulo.msg_campo_obrigatorio
    nome_do_campo = "campo_teste"
    msg_campo_obrigatorio(nome_do_campo)
'''

# Executa os testes

#testa_msg_campo_obrigatorio() # acrescentei
testa_atualiza_nome_com_sucesso()
testa_atualiza_email_com_sucesso()
testa_atualiza_email_repetido_falha()

sys.stderr.write("Testes terminados normalmente.\n")
