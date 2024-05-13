import obj_usuario
import obj_video
import html_elem_paragraph
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_button_submit

def gera(vid_id, atrs, editavel, para_admin, para_proprio):

  # Validação de tipos (paranóia):
  assert vid_id == None or isinstance(vid_id, str), "{vid_id} inválido"
  assert atrs == None or isinstance(atrs, dict), "{atrs} inválido"
  assert type(editavel) is bool, "{editavel} inválido"
  assert type(para_admin) is bool, "{para_admin} inválido"
  assert type(para_proprio) is bool, "{para_proprio} inválido"

  # Obtem os atributos {atrs_tab} a mostrar:
  if vid_id == None:
    vid = None
    atrs_tab = atrs.copy()
  else:
    vid = obj_video.obtem_objeto(vid_id)
    assert vid != None, "Vídeo não existe"
    atrs_tab = obj_video.obtem_atributos(vid).copy()
    atrs_tab.update(atrs)

  # Linhas da tabela: 
  dados_linhas = []

  # Identificador existe só para vídeo existente, e é readonly:
  if vid_id != None:
    atrs_tab['video'] = vid_id
    dados_linhas.append( ( "Identificador",  "text", 'video', False, None, ) )

  # O autor existe mesmo na criação, e é sempre é imutável:
  dados_linhas.append( ( "Autor",  "text", 'autor',  False, None, ) )
  
  # Data só existe depois de criado, e é sempre imutável:
  if vid_id != None:
    dados_linhas.append( ( "Data",   "date", 'data',  False, None, ) )
  
  if vid_id == None:
    # Upload de arquivo só na criação:
    dados_linhas.append( ( "Arquivo", "file", 'conteudo', True,  None, ) )

  # Titulo sempre aparece, possivelmente editável:
  dados_linhas.append( ( "Título",  "textarea",  'titulo',       editavel,  None, ) )

  # Nota na criação começa com 2.0. Sempre aparece, mas é editável só para administrador:
  if vid_id == None: 
    atrs_tab.pop('nota', None)
  else:
    ed_nota = editavel and para_admin
    dados_linhas.append( ( "Nota",  "number", 'nota', ed_nota, "N.NN", ) )

  # Dimensãoe do vídeo só aparecem depois de criado, sempre readonly:
  if vid_id != None:
    dados_linhas.append( ( "Duracao (ms)",   "number",   'duracao',         False, None, ) )
    dados_linhas.append( ( "Altura",         "number",   'altura',          False, None, ) )
    dados_linhas.append( ( "Largura",        "number",   'largura',         False, None, ) )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tab)

  # Acrescenta botões para ver outras coisas do vídeo, se for o caso:
  ht_bt_alterar = None # A menos que tenha.
  ht_bt_conversa = None # A menos que tenha.
  ht_bt_comentar = None # A menos que tenha.
  if vid_id != None:
    cmd_args = {'video': vid_id}
    if not editavel:
      ht_bt_alterar = html_elem_button_simples.gera(f"Alterar", "solicitar_pag_alterar_video", cmd_args, '#eeee55')
    ht_bt_conversa = html_elem_button_simples.gera(f"Ver comentarios", "ver_conversa", cmd_args, '#eeee55')
    ht_bt_comentar = html_elem_button_submit.gera("Comentar", "solicitar_pag_postar_comentario", cmd_args, '#55ee55')

  ht_bloco = \
    ht_table + "<br/>" + \
    ( ht_bt_alterar + " " if ht_bt_alterar != None else "") + \
    ( ht_bt_conversa  + " " if ht_bt_conversa != None else "") + \
    ( ht_bt_comentar  + " " if ht_bt_comentar != None else "")
  
  return ht_bloco
