import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import obj_usuario
import obj_sessao
import html_elem_form
import util_nota

def gera(usr_id, atrs, editavel, para_admin, para_proprio):

  # Validação de tipos (paranóia):
  assert usr_id == None or isinstance(usr_id, str), "{usr_id} inválido"
  assert atrs == None or isinstance(atrs, dict), "{atrs} inválido"
  assert type(editavel) is bool, "{editavel} inválido"
  assert type(para_admin) is bool, "{para_admin} inválido"
  assert type(para_proprio) is bool, "{para_proprio} inválido"
  
  nao_editavel = False

  if atrs == None: atrs = { }

  # Obtem os atributos {atrs_tab} a mostrar:
  if usr_id == None:
    assert editavel, "Criacao tem que ser editável"
    usr = None
    atrs_tab = atrs.copy()
  else:
    if editavel: assert para_admin or para_proprio, "Não devia ser editavel"
    usr = obj_usuario.obtem_objeto(usr_id)
    assert usr != None, "Usuário não existe"
    atrs_tab = obj_usuario.obtem_atributos(usr).copy()
    atrs_tab.update(atrs)
  
  # Apaga a senha e contra-senha, se houverem:
  atrs_tab.pop('senha', None)
  atrs_tab.pop('conf_senha', None)
  
  # Linhas da tabela: 
  dados_linhas = []
  
  if usr_id != None:
    # Mostra identificador do usuário como readonly:
    atrs_tab['usuario'] =  usr_id
    dados_linhas.append( ( "Identificador", "text",  'usuario',  editavel, None, ) )

  # Nome sempre aparece, possivelmente editável:
  dados_linhas.append( ( "Nome", "text", 'nome',  editavel, None, ) )

  # Email aparece, possivelmente editável, só na criação ou para admin ou próprio:
  if usr_id == None or para_admin or para_proprio:
    dados_linhas.append( ( "E-mail", "text", 'email', editavel,  "xxx@xxx.xxx.xx", ) )
    
  # Senha, conf-senha sempre aparecem se usuário é editável:
  # if editavel:
  #   dados_linhas.append( ( "Senha",            "password", 'senha',       True, None, ) )
  #   dados_linhas.append( ( "Confirme senha",   "password", 'conf-senha',  True, None, ) )
  # Atributo 'administrador' sempre aparece, mas é editável só para administrador:
  # edt_admin = (editavel and para_admin)
  
  dados_linhas.append( ( "Administrador", "checkbox", 'administrador', para_admin, None ) )
  
  # formata a nota para exibição com emoji:
  atrs_tab['vnota'] = util_nota.formata(atrs['vnota'])
  # Atributo 'vnota' sempre aparece, mas é editável só para administrador:
  dados_linhas.append( ( "Nota dos vídeos", "text", 'vnota',  None, None, ) )
  
  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tab)

  # Acrescenta botões para ver outras coisas do usuário, se for o caso:
  ht_bt_alterar = None # A menos que tenha.
  ht_bt_sessoes = None # A menos que tenha.
  ht_bt_videos = None # A menos que tenha.
  ht_bt_comentarios = None # A menos que tenha.
  if para_admin or para_proprio:
    cmd_args = {'usuario': usr_id}
    ht_bt_alterar = html_elem_button_simples.gera(f"Alterar", "solicitar_pag_alterar_usuario", cmd_args, None)
    ht_bt_recalcular = html_elem_button_simples.gera("Recalcular notas", "recalcular_notas_de_usuario", cmd_args, None)
    if not para_proprio:
      # Não tem estes botões no menu:
      # Somente administrador ou o próprio podem ver as sessões de {usr}:
      if para_admin:
        nab = len(obj_sessao.busca_por_dono(usr, True))
        if nab > 0 and not para_proprio:
          ht_bt_sessoes = html_elem_button_simples.gera(f"Ver sessões ({nab})", "buscar_sessoes_de_usuario", cmd_args, None)

    # Qualquer um pode ver os vídeos e comentários de {usr}
    ht_bt_videos = html_elem_button_simples.gera(f"Ver videos", "buscar_videos_de_usuario", {'usuario': usr_id}, None)
    ht_bt_comentarios = html_elem_button_simples.gera(f"Ver comentarios", "buscar_comentarios_de_usuario", cmd_args, None)

  ht_bloco = \
    ht_table + "<br/>" + \
    ( ht_bt_alterar + " " if ht_bt_alterar != None else "") + \
    ( ht_bt_sessoes + " " if ht_bt_sessoes != None else "") + \
    ( ht_bt_videos  + " " if ht_bt_videos != None else "") + \
    ( ht_bt_comentarios  + " " if ht_bt_comentarios != None else "") + \
    ( ht_bt_recalcular  + " " if ht_bt_comentarios != None else "")

  return ht_bloco
