import html_bloco_lista_de_sessoes
import html_pag_generica
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, args):
  assert ses != None
  assert obj_sessao.aberta(ses)
  usr_ses = obj_sessao.obtem_usuario(ses)
  id_usr_ses = obj_usuario.obtem_identificador(usr_ses)
  assert usr_ses != None
  if 'id_usuario' in args:
    # Alguém quer ver sessões de usuário específico:
    id_usr = args['id_usuario']
    assert (id_usr == id_usr_ses) or obj_sessao.eh_administrador(ses) # Deveria ser o caso.
    bt_ver = True
    bt_fechar = True
  else:
    # Usuário da sessão {ses} uer ver as próprias sessões:
    usr = usr_ses
    id_usr = id_usr_ses
    bt_ver = True
    bt_fechar = True

  # Com o id do usuário, podemos buscar suas sessões no banco:
  ids_sessoes = obj_sessao.busca_por_campo('usr', id_usr)
  ht_conteudo = html_bloco_lista_de_sessoes.gera(ids_sessoes, bt_ver, bt_fechar)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag
