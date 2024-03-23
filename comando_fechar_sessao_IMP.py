# Implementação do módulo {comando_fechar_sessao}.

import html_pag_ver_sessao
import html_pag_mensagem_de_erro
import html_pag_principal
import obj_sessao

def processa(ses, cmd_args):
  if ses == None or not obj_sessao.aberta(ses) or not obj_sessao.eh_administrador(ses):
    # Isto nunca deveria acontecer, mas em todo caso:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa entrar como administrador antes de fechar a sessão de outro usuário")
  else:
    # Busca sessão mandada nos argumentos da url e a fecha
    ses_a_fechar = obj_sessao.busca_por_identificador(cmd_args['id_ses'])
    obj_sessao.fecha(ses_a_fechar)
    
    if ses == ses_a_fechar:
      # se a sessao que está sendo fechada for a sessao corrente, fazer como em comando_fazer_logout (retorna pra homepage).
      pag = html_pag_principal.gera(None, None)
    else:
      # Redireciona para a mesma página, agora com dados atualizados
      pag = html_pag_ver_sessao.gera(ses, ses_a_fechar, None)
    
  return pag
