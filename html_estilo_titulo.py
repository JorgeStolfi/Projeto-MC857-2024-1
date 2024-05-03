import html_estilo_titulo_IMP

def gera(cor_texto):
  """Retorna um fragmento de CSS para uso no atributo "style" 
  de um título de página ou seção, por exemplo 
  produzido por {html_bloco_titulo.gera}.
  
  O parâmetro {cor_texto} define a cor do texto. Deve ser uma especificação de 
  cor aceitável no atributo CSS "color:", por exemplo "#558800". """
  return html_estilo_titulo_IMP.gera(cor_texto)
