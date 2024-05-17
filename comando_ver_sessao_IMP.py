import html_pag_ver_sessao
import obj_sessao

def processa(ses, cmd_args):
  erros = []
  ses_a_ver = None
  if ses == None or not obj_sessao.aberta(ses):
    erros.append("Precisa estar logado para executar este comando")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    admin = obj_sessao.de_administrador(ses)
    if 'sessao' not in cmd_args:
      # Identificador da sessão não foi especificado, supõe que é a corrente:
      ses_a_ver = ses
      ses_a_ver_id = obj_sessao.obtem_identificador(ses_a_ver)
    else: 
      # Quer ver uma sessão diferente da corrente:
      ses_a_ver_id = cmd_args['sessao']
      ses_a_ver = obj_sessao.obtem_objeto(ses_a_ver_id)
      if ses_a_ver == None:
        erros.append("A sessão \"{ses_a_ver_id}\" não existe")

    if ses_a_ver != None:
      if obj_sessao.obtem_dono(ses_a_ver) != ses_dono and not admin:
        erros.append('Você não tem permissão para examinar essa sessão')
        ses_a_ver = None

    if ses_a_ver != None:
      pag = html_pag_ver_sessao.gera(ses, ses_a_ver, erros)
    else:
      pag = html_pag_principal(ses, erros)
  return pag
