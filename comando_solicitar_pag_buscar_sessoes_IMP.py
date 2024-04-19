
import html_pag_buscar_sessoes
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):
  # Estas condições deveriam valer para comandos gerados
  # pelas páginas do site:
  assert ses == None or obj_sessao.aberta(ses), "Sessao inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  assert cmd_args == {}, "Argumentos espúrios"

  admin = obj_sessao.de_administrador(ses) if ses != None else False
  if not admin:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa ser administrador para usar este comando.")
  else:
    pag = html_pag_buscar_sessoes.gera(ses, {}, None)
  return pag
