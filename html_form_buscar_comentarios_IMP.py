import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form
import html_elem_paragraph

def gera(atrs, para_admin):
    dados_linhas = (
      ( "ID", "text",     'comentario',    True,  "C-nnnnnnnn" ),
      ( "Vídeo", "text",     'video',    True,  "V-nnnnnnnn" ),
      ( "Autor",  "text",     'autor',  True,  "U-nnnnnnnn" ),
      ( "Pai",  "text", 'pai',  True,  "C-nnnnnnnn" ),
      ( "Texto",  "text",     'texto',  True,  "" ),
      ( "Data",  "text",     'data',  True,  "ano-mes-dia hora:minuto:segundos UTC (formato ISO)" ),
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
