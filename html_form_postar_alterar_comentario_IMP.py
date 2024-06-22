import html_bloco_cabecalho_de_comentario
import html_elem_textarea
import html_elem_form
import html_elem_label
import html_elem_input
import html_elem_button_simples
import html_elem_button_submit

def gera(com_id, atrs, ed_nota, ed_voto):

  # Validação de argumentos (paranóia):
  assert com_id == None or isinstance(com_id, str)
  assert atrs == None or isinstance(atrs, dict)
  
  if atrs == None: atrs = {}

  ht_cabeca = html_bloco_cabecalho_de_comentario.gera \
    ( com_id, atrs, 
      largura = 600, # Por enquanto.
      mostra_id = False,
      mostra_data = (com_id != None),
      mostra_video = True,
      mostra_pai = True
    )
  
  # Campos editáveis:
  texto_mod = atrs.get('texto', None)
  editavel = True
  obrigatorio = True
  ht_texto = html_elem_textarea.gera \
    ( None, 'texto', 'texto', texto_mod,
      editavel = True, dica = None, cmd = None, obrigatorio = True,
      altura = 5, largura = 60
    )

  # Nota opcionalmente editável:
  if ed_nota:
    com_nota = atrs.get('nota', 2.0)
    ht_nota = "<br/>" + \
      html_elem_label.gera("Nota:", " ") + \
      html_elem_input.gera("number", 'nota', 'nota', com_nota, 0.0, True, None, None, True, True )
  else:
    ht_nota = ""

  # Voto opcionalmente editável:
  if ed_voto:
    com_voto = atrs.get('voto', 0)
    ht_voto = "<br/>" + \
      html_elem_label.gera("Voto:", " ") + \
      html_elem_input.gera("number", 'voto', 'voto', com_voto, 0, True, None, None, False, False )
  else:
    ht_voto = ""
 
  # Botões 'Confirmar' e 'Cancelar':
  if com_id == None:
    ht_submit = html_elem_button_submit.gera("Postar comentário", "postar_comentario", None, None)
  else:
    cmd_args = { 'comentario': com_id }
    ht_submit = html_elem_button_submit.gera("Salvar alterações", "alterar_comentario", cmd_args, None)
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, None)
  
  ht_form_conteudo = \
    ht_cabeca + \
    ht_texto + \
    ht_nota + "<br/>" + \
    ht_voto + "<br/>" + \
    ht_submit + "\n" + \
    ht_cancel
      
  # Campos hidden para passar os atributos para o comando:
  video_id = atrs.get('video', None)
  if video_id != None:
    ht_video_id = html_elem_input.gera("hidden", 'video', None, video_id, None, False, None, None, True, None, True)
    ht_form_conteudo += "\n" + ht_video_id
  
  pai_id = atrs.get('pai', None)
  if pai_id != None:
    ht_pai_id = html_elem_input.gera("hidden", 'pai', None, pai_id, None, False, None, None, True, None, True)
    ht_form_conteudo += "\n" + ht_pai_id

  ht_form = html_elem_form.gera(ht_form_conteudo, False)

  return ht_form
