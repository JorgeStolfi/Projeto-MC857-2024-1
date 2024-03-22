# Implementação do módulo {comando_fazer_upload_video}.

# Interfaces do projeto usadas por esta implementação:
import obj_usuario
import obj_sessao
import html_pag_mensagem_de_erro
import html_pag_principal

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, dados):
  erros = [ "!!! {comando_fazer_upload_video} ainda não foi implementado !!!" ]
  pag = html_pag_mensagem_de_erro.gera(None, erros)

  return pag
