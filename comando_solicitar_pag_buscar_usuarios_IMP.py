# Implementação do módulo {comando_solicitar_pag_buscar_usuarios}.

import html_pag_buscar_usuarios
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):
  # Estas condições deveriam valer para comandos gerados
  # pelas páginas do site:
  assert ses == None or obj_sessao.aberta(ses), "Sessao inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  assert cmd_args == {}, "Argumentos espúrios"
  
  pag = html_pag_buscar_usuarios.gera(ses, {}, None)
  return pag
