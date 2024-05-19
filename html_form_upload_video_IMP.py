import obj_video
import html_bloco_cabecalho_de_video
import html_bloco_tabela_de_campos
import html_elem_button_simples
import html_elem_button_submit
import html_elem_form
import util_dict

def gera(atrs_novo, ed_nota):

  # Validação de argumentos (paranóia):
  assert atrs_novo == None or type(atrs_novo) is dict
  assert type(ed_nota) is bool
  
  if atrs_novo == None: atrs_novo = { }

  # Converte objetos para identificadores, limpa {atrs_novo}:
  atrs_novo = util_dict.para_identificadores(atrs_novo)

  # Cabeçalho com atributos do vídeo
  ht_cabeca = html_bloco_cabecalho_de_video.gera \
    ( None, atrs_novo, largura = 600,
      mostra_id = False, mostra_data = False
    )

  # Linhas da tabela: 
  dados_linhas = []
   
  dados_linhas.append( ( "Arquivo", "file",    'conteudo', True,  None, ) )
  dados_linhas.append( ( "Título", "textarea", 'titulo', True,  None, ) )

  # Nota opcionalmente editável:
  if ed_nota:
    dados_linhas.append( ( "Nota",  "number",  'nota', True,  "0.00 a 5.00", ) )

  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_novo)

  ht_bt_submit = html_elem_button_submit.gera("Enviar", "fazer_upload_video", None, None)
  ht_bt_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, None)

  ht_conteudo = \
    ht_cabeca + "<br/>\n" + \
    ht_tabela + "<br/>\n" + \
    ht_bt_submit + "\n" + \
    ht_bt_cancel

  # O formulário deve ter {multipart = True} para subir o conteúdo do campo "file":
  ht_form = html_elem_form.gera(ht_conteudo, multipart = True)
  
  return ht_form
