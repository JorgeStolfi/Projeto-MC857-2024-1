import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import obj_usuario
import obj_sessao
import html_elem_form

def gera(id_usr, atrs, ses_admin, auto):

  # For simplicity:
  atrs = {}.copy() if atrs == None else atrs.copy()
  atrs.update( { 'usuario': id_usr } )

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = [].copy()

  if id_usr == None or ses_admin or auto:
    dados_linhas.append( ( "Nome",             "text",     'nome',          True,      None,             ) )
    dados_linhas.append( ( "E-mail",           "email",    'email',         True,      "xxx@xxx.xxx.xx", ) )
    dados_linhas.append( ( "Senha",            "password", 'senha',         True,      None,             ) )
    dados_linhas.append( ( "Confirmar senha",  "password", 'conf_senha',    True,      None,             ) )
    dados_linhas.append( ( "Administrador",    "checkbox", 'administrador', ses_admin,     None              ) )
    if id_usr != None:                                                             
      dados_linhas.append( ( "Identificador",    "text",     'usuario',    False,     None,            ) )
  else:                                                                            
    dados_linhas.append( ( "Nome",             "text",     'nome',          False, None,            ) )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)

  # Acrescenta o botão "Ver sessões" se for o caso:
  ht_bt_sessoes = None # A menos que tenha.
  ht_bt_videos = None # A menos que tenha.
  if id_usr != None:
    # Somente admininstrador ou o próprio podem ver as sessões de {usr}:
    if ses_admin or auto:
      usr = obj_usuario.busca_por_identificador(id_usr)
      assert usr != None
      nab = len(obj_sessao.busca_por_usuario(usr, True))
      if nab > 0:
        ht_bt_sessoes = html_elem_button_simples.gera(f"Ver sessões ({nab})", "buscar_sessoes_de_usuario", {'usuario': id_usr}, '#eeee55')

    # Mas qualquer um pode ver os vídeos de {usr}
    ht_bt_videos = html_elem_button_simples.gera(f"Ver videos", "buscar_videos_de_usuario", {'usuario': id_usr}, '#eeee55')
  
    # !!! Acrescentar botão para ver comentários do usuário !!! 

  ht_bloco = \
    ht_table + "<br/>" + \
    ( ht_bt_sessoes + " " if ht_bt_sessoes != None else "") + \
    ( ht_bt_videos  + " " if ht_bt_videos != None else "")

  return ht_bloco
