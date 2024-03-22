import html_form_login
import html_pag_generica

def gera(ses, erros):
  conteudo = html_form_login.gera()
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
