import obj_usuario
import obj_sessao

import html_form_criar_alterar_usuario
import html_pag_generica
import html_elem_button_simples

def gera(ses, usr, erros):
  usr_sessao = obj_sessao.obtem_usuario(ses)
  usr_sessao_admin = obj_usuario.obtem_atributo(usr_sessao, "administrador") == 1

  assert usr != None and type(usr) is obj_usuario.Classe
  id_usr = obj_usuario.obtem_identificador(usr)
  atrs = obj_usuario.obtem_atributos(usr)
  
  ht_form = html_form_criar_alterar_usuario.gera(id_usr, atrs, usr_sessao_admin, "Confirmar", "alterar_usuario")

  ht_botao_sessoes = html_elem_button_simples.gera("Ver sessões", "ver_sessoes", {'id_usuario': id_usr}, '#eeee55')

  ht_conteudo_pag = "<span>O usuário tem " + \
             str(len(obj_usuario.sessoes_abertas(usr))) + \
             " sessões abertas</span><br />" + \
             ht_form

  return html_pag_generica.gera(ses, ht_conteudo_pag, erros)
