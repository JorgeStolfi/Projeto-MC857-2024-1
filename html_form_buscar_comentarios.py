import html_form_buscar_comentarios_IMP


def gera(atrs, para_admin):
  """Gera um formulário "<form>...</form>" com campos editáveis para 
  especificar uma busca de comentários satsfazendo certas condições.
  Este formulário será o conteúdo pricipal de {html_pag_buscar_comentarios.gera}.
  
  Os campos do formulário serão inicializados com os valores que constam do
  dicionádio {atrs},  que pode ser incompleto ou vazio.

  O parâmetro booleano {para_admin} informa se o usuário que pediu o formulário 
  é administrador.
  """
  return html_form_buscar_comentarios_IMP.gera(atrs, para_admin)
