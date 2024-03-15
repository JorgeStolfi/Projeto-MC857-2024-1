import html_bloco_lista_de_sessoes
import html_pag_generica
import html_pag_mensagem_de_erro
import html_bloco_dados_de_sessao
import html_elem_button_simples
import html_bloco_erro
import obj_sessao

def processa(ses, cmd_args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  usr_ses = obj_sessao.obtem_usuario(ses)
  if 'id_ses' in cmd_args:
    id_ses = cmd_args['id_ses']
    ses1 = obj_sessao.busca_por_identificador(id_ses)
    if ses1 == None or obj_sessao.obtem_usuario(ses1) != usr_ses:
      pag = html_bloco_erro.gera('identificador de sessão inválido')
    
    else: 
      ht_conteudo = html_bloco_dados_de_sessao.gera(ses1)
      args_bt = {'id_ses': id_ses}
      ht_conteudo += html_elem_button_simples.gera("Fechar sessão", 'fechar_sessao', args_bt, '#FFA700')
      pag = html_pag_generica.gera(ses, ht_conteudo, None)
    
  else:
    pag = html_bloco_erro.gera('Chamada sem argumentos')

  return pag
