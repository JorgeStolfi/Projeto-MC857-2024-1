
import html_pag_ver_sessao
import obj_sessao

def processa(ses, cmd_args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  usr_ses = obj_sessao.obtem_usuario(ses)
  erros = list()
  ses1 = None
  if 'id_ses' not in cmd_args:
    erros.append('Chamada sem argumentos')
  else:
    id_ses = cmd_args['id_ses']
    ses1 = obj_sessao.busca_por_identificador(id_ses)
    if ses1 == None or obj_sessao.obtem_usuario(ses1) != usr_ses:
      erros.append('identificador de sessão inválido')
         
  return html_pag_ver_sessao.gera(ses, ses1, erros)
