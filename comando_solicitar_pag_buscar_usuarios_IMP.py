# Implementação do módulo {comando_solicitar_pag_buscar_usuarios}.

import html_pag_buscar_usuarios
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, args):
  if ses == None:
    return html_pag_mensagem_de_erro.gera(ses, "Precisa estar logado para usar este comando.")
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    admin = obj_usuario.obtem_atributo(usr_ses, 'administrador')
    if not admin:
       return html_pag_mensagem_de_erro.gera(ses, "Precisa ser administrador para usar este comando.")
  pag = html_pag_buscar_usuarios.gera(ses, {}, admin, None)
  return pag
