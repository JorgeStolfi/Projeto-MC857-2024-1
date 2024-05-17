import obj_video
import html_bloco_cabecalho_de_video
import html_bloco_rodape_de_video
import html_bloco_tabela_de_campos
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit
import html_elem_video
import util_dict

def gera(vid_id, atrs_mod, ed_nota):

  # Validação de argumentos (paranóia):
  assert vid_id != None and type(vid_id) is str
  assert atrs_mod == None or type(atrs_mod) is dict
  assert type(ed_nota) is bool
  
  if atrs_mod == None: atrs_mod = { }

  vid = obj_video.obtem_objeto(vid_id)
  assert vid != None, f"Vídeo {vid_id} não existe"

  # Converte objetos para identificadores, limpa {atrs_mod}:
  vid_atrs = util_dict.para_identificadores(obj_video.obtem_atributos(vid))
  atrs_mod = util_dict.para_identificadores(atrs_mod)
  util_dict.elimina_alteracoes_nulas(atrs_mod, vid_atrs)
  
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
  dados_linhas.append( ( "Título",  "textarea",  'titulo',  True,  None, ) )

  # Nota opcionalmente editável:
  if ed_nota:
    dados_linhas.append( ( "Nota",  "number",  'nota', True,  "0.00 a 5.00", ) )
 
  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_mod)

  ht_rodape = html_bloco_rodape_de_video.gera \
    ( vid_id, vid_atrs, largura = 600,
      mostra_nota = (not ed_nota), mostra_dims = True
    )

  # Botões do formulário:
  ht_bt_submit = html_elem_button_submit.gera("Confirmar alterações", 'alterar_video', None, '#55ee55')
  ht_bt_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, "#ee5555")

  ht_conteudo = \
    ht_cabeca + "\n" + \
    ht_video + "\n" + \
    ht_tabela + "\n" + \
    ht_rodape + "\n" + \
    ht_bt_submit + " " + \
    ht_bt_cancel
 
  ht_form = html_elem_form.gera(ht_conteudo, multipart = False)
  
  return ht_form
