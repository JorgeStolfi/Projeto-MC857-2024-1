import html_bloco_cabecalho_de_comentario
import html_elem_textarea
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit

def gera(com_id, atrs):

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
  
  texto_mod = atrs.get('texto', None)
  editavel = True
  obrigatorio = True
  ht_texto = html_elem_textarea.gera \
    ( None, 'texto', 'texto', texto_mod,
      editavel = True, dica = None, cmd = None, obrigatorio = True,
      altura = 5, largura = 60
    )

  # Botões 'Confirmar' e 'Cancelar':
  if com_id == None:
    ht_submit = html_elem_button_submit.gera("Postar comentário", "postar_comentario", None, '#55ee55')
  else:
    cmd_args = { 'comentario': com_id }
    ht_submit = html_elem_button_submit.gera("Salvar alterações", "alterar_comentario", cmd_args, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  
  ht_form_conteudo = \
    ht_cabeca + \
    ht_texto + "<br/>" + \
    ht_submit + \
    ht_cancel

  ht_form = html_elem_form.gera(ht_form_conteudo, False)
  
  return ht_form
