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

ses_admin = obj_sessao.busca_por_identificador("S-00000001")
ses_comum = obj_sessao.busca_por_identificador("S-00000003")

def testa_processa(rot_teste, *cmd_args):
    """Testa {comando_solicitar_pag_alterar_comentario.processa(*cmd_args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    modulo = comando_solicitar_pag_alterar_comentario
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *cmd_args)

# Testa erro de sessão inválida
testa_processa("sessaoInvalida", None, {})

# Testa erro de comentário não especificado
testa_processa("comentarioNaoEspecificado", ses_admin, {})

# Testa erro de comentário não existente
id_comentario_nao_existente = 'C-01010101'
testa_processa("comentarioNaoExistente", ses_admin, { 'comentario': id_comentario_nao_existente })

# Testa erro de permissão para alterar comentário
id_comentario_outro_usuario = 'C-00000001'
testa_processa("usuarioSemPermissao", ses_comum, { 'comentario': id_comentario_outro_usuario })

# Teste de gerar página para alterar um comentário
id_comentario_existente = 'C-00000001'
testa_processa("exibePaginaAlterarComentario", ses_admin, { 'comentario': id_comentario_existente })

sys.stderr.write("Testes terminados normalmente.\n")