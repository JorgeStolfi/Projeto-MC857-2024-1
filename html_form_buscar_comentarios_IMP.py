import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form

def gera(atrs, admin):

  obj_bloqueado = ("Bloqueado", "text", 'bloqueado', True, "True")
  if not admin:
    obj_bloqueado = ("", "hidden", 'bloqueado', False, None)

  dados_linhas = (
      ( "Comentário",           "text",     'comentario',    True,  "C-nnnnnnnn" ),
      ( "Autor",                "text",     'autor',         True,  "U-nnnnnnnn" ),
      ( "Video",                "text",     'video',         True,  "V-nnnnnnnn" ),
      ( "Em resposta a",        "text",     'pai',           True,  "C-nnnnnnnn" ),
      ( "Data",                 "text",     'data',          True,  "2024-01-01 08:33:25 UTC" ),
      ( "Texto",                "text",     'texto',         True,  "Blá bla bla" ),
      ( "Bloqueado",            "text",     'bloqueado',     True,  "True" ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)
  ht_submit = html_elem_button_submit.gera("Buscar", "buscar_comentarios", None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", "pag_principal", None, '#ee5555')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  ht_form = html_elem_form.gera(ht_conteudo, False)
  
  return ht_form
