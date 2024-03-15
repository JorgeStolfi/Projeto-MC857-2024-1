import html_bloco_sessao
import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_sessao
import html_elem_form
import obj_sessao

def gera(ses, ses1, erros):
  ht_bloco_ses = html_bloco_dados_de_sessao.gera(ses1)

  # Somente gera botão caso o usuário da sessao atual seja administrador e a sessão selecionada esteja aberta
  if (obj_sessao.eh_administrador(ses) and obj_sessao.aberta(ses1)):
    cmd_args = {}
    cmd_args['id_ses'] = obj_sessao.obtem_identificador(ses1)

    # TODO: escolher cores melhores para os botões
    fecha_btn = html_elem_button_simples.gera('Fechar sessão', 'fechar_sessao', cmd_args, 'green')
    ht_bloco_ses += fecha_btn
    
  ht_form_ses = html_elem_form.gera(ht_bloco_ses)

  pag = html_pag_generica.gera(ses, ht_bloco_ses, erros)
  return pag
