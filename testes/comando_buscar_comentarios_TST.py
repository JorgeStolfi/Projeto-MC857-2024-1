#! /usr/bin/python3

import sys

import comando_buscar_comentarios
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video
import util_testes

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

ok_global = True  # Vira {False} se algum teste falha.


def testa_processa(rot_teste, res_esp, *args):
    """Testa {funcao(*args)}, verifica se o resultado é {res_esp}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rot_teste}.html"."""

    global ok_global
    modulo = comando_buscar_comentarios
    funcao = modulo.processa
    frag = False  # Resultado é só um fragmento de página?
    pretty = False  # Deve formatar o HTML para facilitar view source?
    ok = util_testes.testa_funcao_que_gera_html(
        modulo, funcao, rot_teste, res_esp, frag, pretty, *args
    )
    ok_global = ok_global and ok
    return ok


# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.busca_por_identificador(ses_adm_id)

# Teste onde não há sessão aberta, retorna comentarios
testa_processa("Teste sem sessão aberta", str, None, {"video": "V-00000001"})

# Teste passando um id de video existente, retorna comentarios
testa_processa("Teste video existente", str, ses_adm, {"video": "V-00000001"})

# Teste passando um id de video inexistente, nao retorna comentarios
testa_processa("Teste video existente", str, ses_adm, {"video": "V-23000001"})

# Teste passando um id de autor existente, retorna comentarios
testa_processa("Testa autor existente", str, ses_adm, {"autor": "U-00000001"})

# Teste passando um id de autor inexistente, nao retorna comentarios
testa_processa("Testa autor inexistente", str, ses_adm, {"autor": "U-23000001"})

# Teste passando um id de comentario existente, retorna comentarios
testa_processa("Teste comentario existente", str, ses_adm, {"comentario": "C-00000001"})

# Teste passando um id de comentario inexistente, nao retorna comentarios
testa_processa(
    "Teste comentario inexistente", str, ses_adm, {"comentario": "C-23000001"}
)

# Teste passando um id de comentario pai existente, retorna comentarios
testa_processa("Teste comentario pai existente", str, ses_adm, {"pai": "C-00000001"})

# Teste passando um id de comentario pai inexistente, nao retorna comentarios
testa_processa("Teste comentario pai inexistente", str, ses_adm, {"pai": "C-23000001"})

# Teste passando um id de comentario existente mas que não é pai, nao retorna comentarios
testa_processa(
    "Teste comentario existente mas que não é pai", str, ses_adm, {"pai": "C-00000003"}
)

# Teste passando uma data proxima ANO, retorna comentarios
testa_processa(
    "Teste data de comentario existente no momento ANO", str, ses_adm, {"data": "2024"}
)

# Teste passando uma data proxima ANO-MES, retorna comentarios
testa_processa(
    "Teste data de comentario existente no momento ANO-MES",
    str,
    ses_adm,
    {"data": "2024-04"},
)

# Teste passando uma data proxima DATA, retorna comentarios
testa_processa(
    "Teste data de comentario existente no momento DATA",
    str,
    ses_adm,
    {"data": "2024-04-05 08:00:00 UTC"},
)

# Teste passando uma data proxima ANO, retorna comentarios
testa_processa(
    "Teste data de comentario existente no momento ANO", str, ses_adm, {"data": "2024"}
)

# Teste passando uma data não próxima, nao retorna comentarios
testa_processa(
    "Teste data de comentario não existente no momento ANO",
    str,
    ses_adm,
    {"data": "2014"},
)

# Teste passando um texto que está parecido em um comentário, retorna comentarios
testa_processa(
    "Teste texto que está parecido em um comentário", str, ses_adm, {"texto": "soberbo"}
)

# Teste passando um texto que não está parecido em um comentário, nao retorna comentarios
testa_processa(
    "Teste texto que não está parecido em um comentário",
    str,
    ses_adm,
    {"texto": "Super homem"},
)

# Teste passando uma junção de parametros de um comentario existente, retorna comentarios
testa_processa(
    "Teste passando uma junção de parametros de um comentario existente",
    str,
    ses_adm,
    {"texto": "talvez", "pai": "C-00000001", "autor": "U-00000002"},
)

# Teste passando uma junção de parametros existentes mas de comentarios diferentes, nao retorna comentarios
testa_processa(
    "Teste passando uma junção de parametros existentes mas de comentarios diferentes",
    str,
    ses_adm,
    {"texto": "soberbo", "pai": "C-00000002", "autor": "U-00000001"},
)

# Teste passando uma junção de todos os parametros de um comentario existente, retorna comentarios
testa_processa(
    "Teste passando uma junção de todos os parametros de um comentario existente",
    str,
    ses_adm,
    {
        "comentario": "C-00000002",
        "texto": "talvez",
        "pai": "C-00000001",
        "autor": "U-00000002",
        "video": "V-00000001",
        "data": "2024-04-05 08:10:00 UTC",
    },
)

if ok_global:
    sys.stderr.write("Testes terminados normalmente.")
else:
    aviso_erro("Alguns testes falharam", True)
