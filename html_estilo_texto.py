import html_estilo_texto_IMP

def gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens):
  """Retorna um fragmento de CSS para uso no atributo "style" 
  de um texto genperico, por exemplo mensagem de erro,
  título de vídeo, texto de comentário, etc.
  
  O parâmetro {tam_fonte} especifica a altura nominal do fonte, como 
  no atributo CSS "font-size:" por exemplo "24px".
  
  O parâmetro {peso_fonte} especifica o peso do fonte, 
  como no atributo CSS "font-weight:"; por exemplo "bold" ou
  "medium".
  
  Os parâmetros {cor_texto} e {cor_fundo} definem a cor do texto e do fundo,
  respectivamente.  Cada um deve ser uma especificação de 
  cor aceitável nos atributos CSS "color:" e "background:",
  por exemplo "#558800".  Se {cor_fundo} for {None}, deixa o fundo transparente.
  
  O parâmetro {margens} pode ser {None}, ou uma lista de 4 strings que especificam 
  margens adicionais (atributo CSS "padding:") a deixar em torno do texto, por 
  exemplo {("10px", "2em", "10px", "2em")}. Essas margens serão preenchidas com a [cor_fundo}.
  """
  return html_estilo_texto_IMP.gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens)
