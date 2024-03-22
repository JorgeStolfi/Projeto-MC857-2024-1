import obj_sessao
import obj_usuario
import html_form_criar_alterar_usuario
import html_pag_generica

def gera(ses, atrs, erros):
  # Quem está cadastrando é administrador?
  if ses != None:
    usr_ses = obj_sessao.obtem_usuario(ses)
    atrs_ses = obj_usuario.obtem_atributos(usr_ses)
    admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)
  else:
    admin = False
  # Constrói formulário com dados:
  ht_form = html_form_criar_alterar_usuario.gera(None, atrs, admin, "Cadastrar", "cadastrar_usuario")

  ht_conteudo_pag = \
    ht_form

  # Monta a página:
  pagina = html_pag_generica.gera(ses, ht_conteudo_pag, erros)
  return pagina
