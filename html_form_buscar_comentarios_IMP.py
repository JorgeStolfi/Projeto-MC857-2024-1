import html_elem_input
import html_elem_button_submit
import html_elem_button_simples
import html_bloco_tabela_de_campos
import html_elem_form
import html_elem_paragraph

def gera(atrs, para_admin):
    # Aqui você pode implementar a lógica para gerar o formulário com base nos atributos fornecidos
    # Por enquanto, vou deixar apenas uma mensagem estática como conteúdo do formulário
    
    conteudo = "!!! html_form_buscar_comentarios.gera ainda não implementada !!!"
    ht_conteudo = html_elem_paragraph.gera(None, conteudo)
    ht_form = html_elem_form.gera(ht_conteudo, False)
    
    return ht_form
