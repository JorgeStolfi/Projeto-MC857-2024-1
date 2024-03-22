import html_form_criar_alterar_usuario
import html_pag_generica
import html_elem_button_simples

def gera(ses, id_usr, atrs, admin, erros):
  # Constrói formulário com dados:
  ht_form = html_form_criar_alterar_usuario.gera(id_usr, atrs, admin, "Confirmar alterações", 'alterar_usuario')

  # Constroi botões de ações adicionais na página
  if admin and id_usr != None:
    ht_botao_sessoes = html_elem_button_simples.gera("Ver sessões", "ver_sessoes", {'id_usuario': id_usr}, '#eeee55')
  else:
    ht_botao_sessoes = ""
    
  # Gera conteudo
  ht_conteudo_pag = \
    ht_form + "<br />" + \
    ("   " + ht_botao_sessoes)

  # Monta a página:
  pagina = html_pag_generica.gera(ses, ht_conteudo_pag, erros)

  return pagina
