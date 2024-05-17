
import html_pag_buscar_sessoes
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  assert len(cmd_args) == 0, "Argumentos espúrios {cmd_args}"

  # Verifica permissão:
  para_admin = False
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação.")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação.")
  else:
    para_admin = ses != None and obj_sessao.de_administrador(ses)
    if not para_admin:
      erros.append("Você não tem permissão para usar este comando.")
   
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_buscar_sessoes.gera(ses, {}, None)

  return pag
