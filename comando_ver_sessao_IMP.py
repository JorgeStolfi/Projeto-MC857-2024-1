import html_pag_ver_sessao
import html_bloco_dados_de_sessao
import obj_sessao

def processa(ses, cmd_args):
  erros = [].copy()
  ses_a_ver = None
  if ses == None or not obj_sessao.aberta(ses):
    erros.append("precisa estar logado para executar este comando")
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    admin = obj_sessao.de_administrador(ses);
    if 'sessao' not in cmd_args:
      # Identificador da sessão não foi especificado, supõe que é a corrente:
      ses_a_ver = ses
      id_ses_a_ver = obj_sessao.obtem_identificador(ses_a_ver)
    else: 
      # Quer ver uma sessão diferente da corrente:
      id_ses_a_ver = cmd_args['sessao']
      ses_a_ver = obj_sessao.busca_por_identificador(id_ses_a_ver)
      if ses_a_ver == None:
        erros.append("sessão inexistente")
    if ses_a_ver != None:
      if obj_sessao.obtem_usuario(ses_a_ver) != usr_ses and not admin:
        erros.append('sessão não é sua - permissão negada')
        ses_a_ver = None

    if ses_a_ver != None:
      pag = html_pag_ver_sessao.gera(ses, ses_a_ver, erros)
    else:
      pag = html_pag_principal(ses, erros)
  return pag
