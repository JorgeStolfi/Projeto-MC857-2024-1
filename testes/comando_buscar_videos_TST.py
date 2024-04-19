#! /usr/bin/python3

import db_base_sql
import db_tabelas_do_sistema
import comando_buscar_videos
import obj_sessao
import util_testes
import obj_video

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

    modulo = comando_buscar_videos
    funcao = modulo.processa
    frag = False # Resultado é só um fragmento de página?
    pretty = False # Deve formatar o HTML para facilitar view source?
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# Sessão em que o usuário dela é o administrador.
ses_adm_id = "S-00000001"
ses_adm = obj_sessao.busca_por_identificador(ses_adm_id)
assert obj_sessao.de_administrador(ses_adm), f"sessão {ses_adm_id} não é de administrador" 

# Testa com busca por identificador_que existe:
#args_id_vd = {'video': "V-00000002"}

# Testa com busca por autor que existe:
#args_autor = {'autor': "Quentin Tarantino"}

# Testa com busca por título que existe:
#args_titulo = {'titulo': "Django"}

# Testa com busca por arquivo que não existe:
args_arq = {'arq': "virus.gif"}

# Testa com busca por autor que não existe:
args_autor_no = {'autor_no': "naoexiste"}

#testa_processa("video",        ses_adm, args_id_vd)
#testa_processa("email_ok",      ses_adm, args_autor)
testa_processa("arq",          ses_adm, args_arq)
testa_processa("autor_no",      ses_adm, args_autor_no)
#testa_processa("autor",          ses_adm, args_titulo)

sys.stderr.write("Testes terminados normalmente.")
