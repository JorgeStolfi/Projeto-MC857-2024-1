import html_form_login
import html_pag_generica

def gera(erros):
  conteudo = html_form_login.gera()
  pagina = html_pag_generica.gera(None, conteudo, erros)
  return pagina
