import html_bloco_dados_de_sessao_IMP
def gera(ses_id, para_admin, para_proprio):
  """
  Retorna um fragmento HTML que exibe dados da sessão {ses}
  cujo identificador é {ses_id}.
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Dono", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente.
  
  O parâmetro {ses_id} deve ser o identificador (um string no formato
  "S-{NNNNNNNN}") de uma sessão existente.

  Os parâmetros booleanos {para_admin} e {para_proprio} especificam quais
  campos do formulário serão visíveis, como detalhado abaixo. Se o
  parâmetro booleano {para_admin} for {True}, a função entende que o
  usuário que pediu o formulário é administrador. Se o parâmetro
  booleano {para_proprio} for {True}, entende que o formulário foi pedido
  pelo próprio dono da sessão {ses}.
  
  Especificamente, no bloco gerado:
  
    * Haverá um campo "Sessão", que mostra {ses_id}, com chave 'sessao'.
  
    * Haverá um campo "Usuário" que mostra o identificador do usuário
    logado na sessão, com a chave 'dono'.
    
    * Haverá campos "Data" com chave 'data'
    
    * Haverá um campo "Aberta" que mostra "Sim" ou "Não" conforme
    o atributo 'aberta'.
    
  Por enquanto, todos os campos serão readonly.
  """
  return html_bloco_dados_de_sessao_IMP.gera(ses_id, para_admin, para_proprio)
