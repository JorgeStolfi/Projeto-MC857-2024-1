# Implementação do módulo {comando_solicitar_pag_buscar_usuarios}.

import html_pag_buscar_usuarios
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  assert len(cmd_args) ==0, f"Argumentos espúrios \"{cmd_args}\""
   
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_buscar_usuarios.gera(ses, {}, None)

  return pag
