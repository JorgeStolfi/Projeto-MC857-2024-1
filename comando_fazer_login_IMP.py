# Implementação do módulo {comando_fazer_login}.

# Interfaces do projeto usadas por esta implementação:
import obj_usuario
import obj_sessao
import html_pag_mensagem_de_erro
import html_pag_principal

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, dados):
  ses_nova = ses # Caso o login falhe.

  if ses != None:
    # Não deveria acontecer, mas por via das dúvidas:
    pag = html_pag_mensagem_de_erro.gera(ses, "Favor sair da sessão corrente primeiro")
  else:
    erro_email = None # Email não especificado ou não cadastrado.
    erro_senha = None # Senha não especificada ou inválida.

    if 'senha' not in dados:
      erro_senha = "campo 'senha' é obrigatório"
      senha = None
    else:
      senha = dados['senha'] 

    if 'email' not in dados:
      erro_email = "campo 'email' é obrigatório"
      email = None
    else:
      email = dados['email']

    usr = None
    if email != None and senha != None:
      # Obtem o usuário pelo email:
      usr_id = obj_usuario.busca_por_email(email)
      if usr_id == None:
        erro_email = "Usuário " + email + " não está cadastrado"
      else:
        usr = obj_usuario.obtem_objeto(usr_id)
        assert usr != None
        atrs_usr = obj_usuario.obtem_atributos(usr)
        if atrs_usr["senha"] != senha:
          erro_senha = "Senha incorreta"
          usr = None

    if usr != None:
      cookie = secrets.token_urlsafe(32)
      # Data de criação definida como "agora":
      ses_nova = obj_sessao.cria(usr, cookie, criacao = None)
      pag = html_pag_principal.gera(ses_nova, None)
    else:
      erros = [ erro_email, erro_senha ]
      pag = html_pag_mensagem_de_erro.gera(None, erros)

  return pag, ses_nova
