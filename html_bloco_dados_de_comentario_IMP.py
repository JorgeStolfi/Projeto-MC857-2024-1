import html_bloco_tabela_de_campos
import obj_video
import obj_usuario
import html_elem_button_simples

def gera(id_com, atrs, edita_texto):

  atrs_tab = atrs.copy() # Para não alterar o original.
  
  edita_tudo = (id_com == None)
  
  dados_linhas = [].copy()

  if id_com != None:
    # Ver ou alterar um comentário existente:
    atrs_tab.update( { 'comentario': id_com } )
    dados_linhas.append( ( "Identificador",  "text",  'comentario',   False, None, ) )
    dados_linhas.append( ( "Data",           "date",  'data',         False, None, ) )

  dados_linhas.append( ( "Vídeo",    "text",     'video',     False,   None,  ) )
  dados_linhas.append( ( "Autor",    "text",     'autor',     False,   None,  ) )
  dados_linhas.append( ( "Pai",      "text",     'pai',       False,   None,  ) )
  dados_linhas.append( ( "Texto",    "textarea", 'texto',     edita_texto,   None,  ) )

  ht_bloco = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tab)

  # Botão de conversa
  ht_bt_conversa = html_elem_button_simples.gera("Ver conversa", 'html_pag_ver_conversa', None, '#808080')

  return ht_bloco + ht_bt_conversa
