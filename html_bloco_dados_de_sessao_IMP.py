import obj_usuario
import obj_sessao
import html_elem_paragraph
import html_bloco_tabela_de_campos
import html_elem_button_simples

def gera(ses):

  # Validação de tipos (paranóia):
  assert ses != None and isinstance(ses, obj_sessao.Classe)
 
  # Obtem os atributos {atrs_tab} a mostrar:
  atrs_tab = obj_sessao.obtem_atributos(ses).copy()
  
  # Acrescenta o identificador da sessão:
  atrs_tab['sessao'] = obj_sessao.obtem_identificador(ses)
  
  # Converte o atributo 'aberta' para "Aberta"/"Fechada":
  atrs_tab['aberta'] = "Aberta" if atrs_tab['aberta'] else "Fechada"

  # Linhas da tabela: 
  dados_linhas = \
    (
      ( "ID da sessão",       "text", 'sessao',     False, None, ),
      #( "Criada em",          "text", 'data_login', False, None, ), # Original/Old
      ( "Criada em",          "text", 'criacao', False, None, ),# Alterado data_login para "criacao" conforme obj_sessao_IMP
      ( "Dono",               "text", 'dono',       False, None, ),
      ( "Cookie",             "text", 'cookie',     False, None, ),
      ( "Status",             "text", 'aberta',     False, None, ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tab)

  ht_bloco = ht_table
 
  return ht_bloco
