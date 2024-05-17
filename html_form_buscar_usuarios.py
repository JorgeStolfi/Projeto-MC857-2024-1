import html_form_buscar_usuarios_IMP

def gera(atrs, para_admin):
  """Gera um formulário "<form>...</form>" com campos editáveis para 
  especificar uma busca de usuarios satsfazendo certas condições.
  Este formulário será o conteúdo pricipal de {html_pag_buscar_usuarios.gera}.
  
  Os campos do formulário serão inicializados com os valores que constam do
  dicionádio {atrs},  que pode ser incompleto ou vazio."""
  return html_form_buscar_usuarios_IMP.gera(atrs, para_admin)
