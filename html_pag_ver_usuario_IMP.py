import obj_usuario
import obj_sessao

import html_pag_alterar_usuario
import html_bloco_dados_de_usuario
import html_pag_generica
import html_elem_button_simples
from util_erros import ErroAtrib, erro_prog

def gera(ses, usr, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert usr != None and isinstance(usr, obj_usuario.Classe), "Usuário inválido"
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  erros = [].copy()
  
  # Obtem o usuário da sessão:
  usr_ses = obj_sessao.obtem_usuario(ses) if ses != None else None

  try:
    # Determina privilégios do usuário da sessão:
    admin = obj_sessao.de_administrador(ses) if ses != None else False
    
    # Obtem o identificador e atributos do usuário:
    id_usr = obj_usuario.obtem_identificador(usr)
    atrs_usr = obj_usuario.obtem_atributos(usr)
    
    auto = (usr == usr_ses)
    ht_bloco = html_bloco_dados_de_usuario.gera(id_usr, atrs_usr, admin, auto)
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  except ErroAtrib as ex:
    erros += ex.args[0]
    pag = html_pag_mensagem_de_erro(ses, erros)

  return pag
