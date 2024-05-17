import html_bloco_dados_de_sessao_IMP

def gera(ses):
  """
  Retorna um fragmento HTML que exibe dados da sessão {ses}
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Dono", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente.
  
  O parâmetro {ses_id} deve ser o identificador (um string no formato
  "S-{NNNNNNNN}") de uma sessão existente.
  
  Especificamente, no bloco gerado:
  
    * Haverá um campo "Sessão", que mostra {ses_id}, com chave 'sessao'.
  
    * Haverá um campo "Usuário" que mostra o identificador do usuário
    logado na sessão, com a chave 'dono'.
    
    * Haverá um campo "Data" com chave 'data'
    
    * Haverá um campo "Aberta" que mostra "Sim" ou "Não" conforme
    o atributo 'aberta'.
    
  Por enquanto, todos os campos serão readonly.
  """
  return html_bloco_dados_de_sessao_IMP.gera(ses)
