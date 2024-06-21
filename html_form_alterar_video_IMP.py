import obj_video
import html_bloco_cabecalho_de_video
import html_bloco_rodape_de_video
import html_bloco_tabela_de_campos
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit
import html_elem_video
import util_dict
import html_elem_input

def gera(vid_id, atrs_mod, eh_adm):

  # Validação de argumentos (paranóia):
  assert vid_id != None and type(vid_id) is str
  assert atrs_mod == None or type(atrs_mod) is dict
  assert type(eh_adm) is bool
  
  if atrs_mod == None: atrs_mod = { }

  vid = obj_video.obtem_objeto(vid_id)
  assert vid != None, f"Vídeo {vid_id} não existe"

  # Converte objetos para identificadores, limpa {atrs_mod}:
  vid_atrs = util_dict.para_identificadores(obj_video.obtem_atributos(vid))
  atrs_mod = util_dict.para_identificadores(atrs_mod)
  # Cabeçalho com atributos do vídeo
  ht_cabeca = html_bloco_cabecalho_de_video.gera \
    ( vid_id, vid_atrs, largura = 600,
      mostra_id = False, mostra_data = True
    )
    
  # Janela do vídeo:
  ht_video = html_elem_video.gera(vid_id, altura = 300)
 
  # Linhas da tabela: 
  dados_linhas = []

  # Titulo sempre aparece, possivelmente editável:
  dados_linhas.append( ( "Título",  "textarea",  'titulo',  True,  None, False, ) )

  if eh_adm:
    dados_linhas.append( ( "Bloqueado",  "checkbox",  'bloqueado', True,  None, False, ) )
 
  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_mod)

  ht_rodape = html_bloco_rodape_de_video.gera \
    ( vid_id, vid_atrs, largura = 600,
      mostra_nota = (not eh_adm), mostra_dims = True
    )

  cmd_args = { 'video': vid_id }

  # Botões do formulário:
  ht_bt_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_video', cmd_args, None)
  ht_bt_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)
  ht_bt_calcnota = html_elem_button_simples.gera("Recalcular nota", "recalcular_nota", cmd_args, '#ff5555')

  ht_conteudo = \
    ht_cabeca + "\n" + \
    ht_video + "\n" + \
    ht_tabela + "\n" + \
    ht_rodape + "\n" + \
    ht_bt_calcnota + " " + \
    ht_bt_submit + " " + \
    ht_bt_cancel
  
  # Campos hidden para passar os atributos para o comando:
  ht_video_id = html_elem_input.gera("hidden", 'video', None, vid_id, None, False, None, None, True, None)
  ht_conteudo += "\n" + ht_video_id
  ht_form = html_elem_form.gera(ht_conteudo, multipart = False)
  
  return ht_form
