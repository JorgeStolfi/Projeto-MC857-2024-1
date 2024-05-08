#! /usr/bin/python3

import sys

import comando_buscar_comentarios
import db_base_sql
import db_tabelas_do_sistema
import obj_comentario
import obj_sessao
from util_erros import aviso_prog
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
    ok = util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)
    ok_global = ok_global and ok
    return ok

# Sessão para teste:
ses_id = "S-00000001"
ses = obj_sessao.obtem_objeto(ses_id)

# Teste passando um id de comentario existente:
cmd_args_01 = {"comentario": "C-00000001"}
testa_processa("comE", str, ses, cmd_args_01)

# Teste passando um id de comentario inexistente:
cmd_args_02 = {"comentario": "C-23000001"}
testa_processa("comN", str, ses, cmd_args_02)

# Teste sem estar logado:
cmd_args_03 = {"video": "V-00000003"}
testa_processa("logF-vidE", str, None, cmd_args_03)

# Teste passando um id de video existente:
cmd_args_04 = {"video": "V-00000003"}
testa_processa("vidE", str, ses, cmd_args_04)

# Teste passando um id de video inexistente:
cmd_args_05 = {"video": "V-23000001"}
testa_processa("vidN", str, ses, cmd_args_05)

# Teste passando um id de autor existente:
cmd_args_06 = {"autor": "U-00000001"}
testa_processa("autE", str, ses, cmd_args_06)

# Teste passando um id de autor inexistente:
cmd_args_07 = {"autor": "U-23000001"}
testa_processa("autN", str, ses, cmd_args_07)

# Teste passando um id de comentario pai existente:
cmd_args_08 = {"pai": "C-00000001"}
testa_processa("paiE", str, ses, cmd_args_08)

# Teste passando um id de comentario existente mas sem filhos:
cmd_args_09 = {"pai": "C-00000003"}
testa_processa("paiS", str, ses, cmd_args_09)

# Teste passando um id de comentario pai inexistente:
cmd_args_10 = {"pai": "C-23000001"}
testa_processa("paiN", str, ses, cmd_args_10)

# Teste passando uma data exata que existe:
com3 = obj_comentario.obtem_objeto("C-00000003")
dat3 = obj_comentario.obtem_atributo(com3, 'data')
cmd_args_11 = {"data": dat3}
testa_processa("datP", str, ses, cmd_args_11)

# Teste passando uma data exata que não existe:
cmd_args_12 = {"data": "2024-01-01 08:00:00 UTC"}
testa_processa("datP", str, ses, cmd_args_12)

# Teste passando data corrente ano+mes:
mes3 = dat3[0:7] # Ano e mes.
cmd_args_13 = {"data": mes3}
testa_processa("mesP", str, ses, cmd_args_13)

# Teste passando o ano corrente:
cmd_args_14 = {"data": "2024"}
testa_processa("anoP", str, ses, cmd_args_14)

# Teste passando um texto parcial que existe
cmd_args_15 = {"texto": "sobe"}
testa_processa("texE", str, ses, cmd_args_15)

# Teste passando um texto que não aparece em nenhum comentário:
cmd_args_16 = {"texto": "Superhomem"}
testa_processa("texN", str, ses, cmd_args_16)

# Teste passando vários parâmetros com resposta única (supõe lógica "E"):
cmd_args_17 = {"texto": "talvez", "pai": "C-00000001", "autor": "U-00000002"}
testa_processa("mulU", str, ses, cmd_args_17)

# Teste passando vários parâmetros com múltiplas respostas (supõe lógica "E"):
cmd_args_18 = {"autor": "U-00000002", "video": "V-00000001"}
testa_processa("mulM", str, ses, cmd_args_18)

# Teste passando vários parâmetros sem resposta (supõe lógica "E"):
cmd_args_19 = {"autor": "U-00000002", "video": "V-00000004"}
testa_processa("mulV", str, ses, cmd_args_19)

if ok_global:
    sys.stderr.write("Testes terminados normalmente.")
else:
    aviso_prog("Alguns testes falharam", True)
