import html_form_buscar_videos_IMP

def gera(atrs, para_admin):
  """Gera um formulário "<form>...</form>" com campos editáveis para 
  especificar uma busca de videos satsfazendo certas condições.
  Este formulário será o conteúdo pricipal de {html_pag_buscar_videos.gera}.
  
  Os campos do formulário serão inicializados com os valores que constam do
  dicionádio {atrs},  que pode ser incompleto ou vazio.
  
  O parâmetro booleano {para_admin} diz se quem pediu este formulário é
  um administrador.  Alguns campos, como 'bloqueado', só podem ser usados em buscas por
  administradores."""
  return html_form_buscar_videos_IMP.gera(atrs, para_admin)
