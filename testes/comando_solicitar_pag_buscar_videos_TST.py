# from util_testes import erro_prog
# erro_prog('!!! programa de teste do modulo comando_solicitar_pag_buscar_videos ainda nao foi escrito !!!')

import comando_solicitar_pag_buscar_videos
import db_tabelas
import obj_sessao
import obj_video
import db_base_sql
import util_testes
import obj_usuario
import sys

def testa_processa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_buscar_videos
    funcao = modulo.processa
    frag = False  
    pretty = True 
    util_testes.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas.cria_todos_os_testes(True)

# Sessões de teste
ses_comum = obj_sessao.busca_por_identificador("S-00000001")

#Sessão Admin
admin = obj_usuario.busca_por_identificador("U-00000001")
assert obj_usuario.obtem_atributo(admin, 'administrador')
ses_admin = obj_sessao.cria(admin, "NOPQRSTUVWX")

#Sessao usuário Comum
comum = obj_usuario.busca_por_identificador("U-00000002")
assert  not obj_usuario.obtem_atributo(comum, 'administrador')
ses_comum1 = obj_sessao.cria(comum, "NOPQRSTUVWX")



testa_processa("NL-e0", None, None)#Sem sessão
testa_processa("NA-e2", ses_comum, ["banana", "abacate"])#Sessão não aberta
testa_processa("OK-e0", ses_admin, None)#Sessão admin aberta
testa_processa("OK-e2", ses_admin, ["Roubar", "Mentir"])#Sessão admin aberta
testa_processa('OK-e3',ses_comum1,None)#Sessao usuário Comum aberta
testa_processa("OK-e4", ses_comum1, ["Roubar", "Mentir"])#Sessao usuário Comum aberta