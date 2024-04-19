#! /usr/bin/python3

import comando_solicitar_pag_alterar_usuario
import db_base_sql
import db_tabelas_do_sistema
import obj_usuario
import obj_sessao
import util_testes

import sys

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

# sessão usada no teste
sessao1 = obj_sessao.busca_por_identificador("S-00000001")
assert sessao1 != None

def testa_processa(rot_teste, *cmd_args):
    """Testa {comando_solicitar_pag_alterar_usuario.processa(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_solicitar_pag_alterar_usuario
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

cmd_args1 = {}
# Teste mostra os dados do dono da sessão
testa_processa("SucVazio", sessao1, cmd_args1)

cmd_args1['usuario'] = "U-00000002"
# Teste mostra os dados do dono do identificador passado
testa_processa("SucPreenchido", sessao1, cmd_args1)

sys.stderr.write("Testes terminados normalmente.\n")
