
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
    id_ses1 = cmd_args['id_ses']
    ses1 = obj_sessao.busca_por_identificador(id_ses1)
    if ses1 == None or obj_sessao.obtem_usuario(ses1) != usr_ses:
      erros.append('identificador de sessão inválido')
    else: 
      ht_conteudo = html_bloco_dados_de_sessao.gera(ses1)
      args_bt = {'id_ses': id_ses}
      ht_conteudo += html_elem_button_simples.gera("Fechar sessão", 'fechar_sessao', args_bt, '#FFA700')
      pag = html_pag_generica.gera(ses, ht_conteudo, None)
         
  return html_pag_ver_sessao.gera(ses, ses1, erros)
