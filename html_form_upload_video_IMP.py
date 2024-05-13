import html_elem_form
import html_elem_button_simples
import html_elem_button_submit
import html_bloco_dados_de_video

def gera(atrs, para_admin):

  # Validação de argumentos (paranóia):
  assert atrs == None or isinstance(atrs, dict), "{atrs} inválido"
  assert isinstance(para_admin, bool), "{para_admin} inválido"

  atrs_tab = atrs.copy() if atrs != None else {}

  # Verifica se atributos essenciais estão definidos (paranóia):
  assert 'autor' in atrs_tab, "Campo 'autor' não especificado"
  
  # Elimina atributos não editáveis de {atrs_tab}:
  atrs_tab.pop('data',    None)
  atrs_tab.pop('duracao', None)
  atrs_tab.pop('altura',  None)
  atrs_tab.pop('largura', None)
  atrs_tab.pop('nota',    None)

  # Constrói tabela com dados:
  vid_id = None
  editavel = True
  para_proprio = True # Porque vai ser criado
  ht_tabela = html_bloco_dados_de_video.gera(vid_id, atrs_tab, editavel, para_admin, para_proprio)
 
  ht_bt_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, '#55ee55')
  ht_bt_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')

  ht_conteudo = \
    ht_tabela + "<br/>\n" + \
    ht_bt_submit + "\n" + \
    ht_bt_cancel

  multipart = True
  ht_form = html_elem_form.gera(ht_conteudo, multipart)
  
  return ht_form
