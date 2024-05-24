import html_elem_button_simples_IMP

def gera(texto, URL, cmd_args, cor_fundo):
  """
  Devolve um fragmento HTML5 que implementa um botão genérico de 
  tipo "<button>", com o {texto} e {cor_fundo} especificados. 
  
  Quando clicado, esse botão emite um comando HTTP 'GET' para o {URL} dado.
  O URL geralmente é o nome de um comando do site sem o prefixo "comando_",
  por exemplo "buscar_videos".  Mas pode ser um arquivo como "imagens/mapa.png",
  o comando especial "pag_principal", ou um URL externo "https://...".
  
  Se {cmd_args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas ao {URL} no formato
  "?{chave1}={valor1}&{chave2}={valor2}...". Por enquanto, cada chave
  pode usar apenas os caracteres [_A-Za-z0-9], e cada valor pode usar
  apenas os caracteres [-+.,_A-Za-z0-9].
  
  O botão terá letras e moldura pretas com fundo da {cor_fundo}
  especificada.  Se {cor_fundo} for {None}, escolhe uma cor
  com base no {texto}.  Vide {html_estilo_button.escolhe_cor_fundo}.
  """
  return html_elem_button_simples_IMP.gera(texto, URL, cmd_args, cor_fundo)
