import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import obj_usuario
import obj_sessao
import html_elem_form

def gera(id_usr, atrs, ses_admin, ses_proprio):

  # Para simplificar
  atrs = {}.copy() if atrs == None else atrs.copy()
  
  # Acrescenta identificador do usuário:
  atrs.update( { 'usuario': id_usr } )
  
  # Apaga a senha e contra-senha, se houverem:
  if 'senha' in atrs: atrs.pop('senha')
  if 'conf-senha' in atrs: atrs.pop('conf-senha')

  edit = ses_admin or ses_proprio  # Atributos comuns devem ser editáveis.
  edcri = id_usr == None or edit   # Mostre senha e email, editáveis
  
  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = [].copy()
  
  if id_usr != None:
    # Mostra identificador do usuário como readonly:
    dados_linhas.append( ( "Identificador", "text",  'usuario',  False, None, ) )

  # Mostra sempre o nome:
  dados_linhas.append( ( "Nome", "text", 'nome',  edcri, None, ) )

  if edcri:
    # Mostra senha, conf-senha, e email, editáveis
    dados_linhas.append( ( "E-mail",           "email",    'email',         True,      "xxx@xxx.xxx.xx", ) )
    dados_linhas.append( ( "Senha",            "password", 'senha',         True,      None,             ) )
    dados_linhas.append( ( "Confirmar senha",  "password", 'conf_senha',    True,      None,             ) )
    
  if ses_admin:
    # Mostra atributo 'admnistrador', editável:
    dados_linhas.append( ( "Administrador",    "checkbox", 'administrador', ses_admin, None ) )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)

  # Acrescenta o botão "Ver sessões" se for o caso:
  ht_bt_sessoes = None # A menos que tenha.
  ht_bt_videos = None # A menos que tenha.
  ht_bt_comentarios = None # A menos que tenha.
  if id_usr != None:
    # Somente admininstrador ou o próprio podem ver as sessões de {usr}:
    if ses_admin or ses_proprio:
      usr = obj_usuario.obtem_objeto(id_usr)
      assert usr != None
      nab = len(obj_sessao.busca_por_usuario(usr, True))
      if nab > 0 and not ses_proprio:
        ht_bt_sessoes = html_elem_button_simples.gera(f"Ver sessões ({nab})", "buscar_sessoes_de_usuario", {'usuario': id_usr}, '#eeee55')

    if not ses_proprio:
      # Mas qualquer um pode ver os vídeos de {usr}
      ht_bt_videos = html_elem_button_simples.gera(f"Ver videos", "buscar_videos_de_usuario", {'usuario': id_usr}, '#eeee55')
  
      # Assim como qualquer um pode ver seus comentários
      ht_bt_comentarios = html_elem_button_simples.gera(f"Ver comentarios", "buscar_comentarios_de_usuario", {'usuario': id_usr}, '#eeee55')

  ht_bloco = \
    ht_table + "<br/>" + \
    ( ht_bt_sessoes + " " if ht_bt_sessoes != None else "") + \
    ( ht_bt_videos  + " " if ht_bt_videos != None else "") + \
    ( ht_bt_comentarios  + " " if ht_bt_comentarios != None else "")

  return ht_bloco
