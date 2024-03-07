import html_bloco_lista_de_sessoes
import html_pag_generica
import html_pag_mensagem_de_erro
import html_bloco_dados_de_sessao
import html_elem_button_simples
import html_bloco_erro
import obj_sessao

def processa(ses, args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  usr_ses = obj_sessao.obtem_usuario(ses)
  if 'id_sessao' in args:
    id_sessao = args['id_sessao']
    sesaux = obj_sessao.busca_por_identificador(id_sessao)
    if sesaux == None or obj_sessao.obtem_usuario(sesaux) != usr_ses:
      pag = html_bloco_erro.gera('id de sessão inválido')
    
    else: 
      ht_conteudo = html_bloco_dados_de_sessao.gera(sesaux)
      args_bt = {'id_sessao': id_sessao}
      ht_conteudo += html_elem_button_simples.gera("Fechar sessão", 'fechar_sessao', args_bt, '#FFA700')
      pag = html_pag_generica.gera(ses, ht_conteudo, None)
    
  else:
    pag = html_bloco_erro.gera('Chamada sem argumentos')

  return pag
