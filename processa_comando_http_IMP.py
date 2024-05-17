# Implementação do módulo {processa_comando_http}.

# Interfaces do projeto usadas por este módulo:
import obj_sessao
import obj_usuario

import comando_ver_sessao
import comando_solicitar_pag_login
import comando_fazer_login
import comando_fazer_logout
import comando_fechar_sessao
import comando_solicitar_pag_buscar_sessoes
import comando_buscar_sessoes
import comando_buscar_sessoes_de_usuario

import comando_ver_usuario
import comando_solicitar_pag_cadastrar_usuario
import comando_cadastrar_usuario
import comando_solicitar_pag_alterar_usuario
import comando_alterar_usuario
import comando_solicitar_pag_buscar_usuarios
import comando_buscar_usuarios

import comando_ver_video
import comando_solicitar_pag_upload_video
import comando_fazer_upload_video
import comando_solicitar_pag_alterar_video
import comando_alterar_video
import comando_solicitar_pag_buscar_videos
import comando_buscar_videos
import comando_buscar_videos_de_usuario
import comando_ver_grade_de_videos

import comando_ver_comentario
import comando_solicitar_pag_postar_comentario
import comando_postar_comentario
import comando_solicitar_pag_alterar_comentario
import comando_alterar_comentario
import comando_solicitar_pag_buscar_comentarios
import comando_solicitar_pag_postar_comentario
import comando_buscar_comentarios
import comando_buscar_comentarios_de_video
import comando_buscar_comentarios_de_usuario
import comando_buscar_respostas_de_comentario
import comando_ver_conversa

import comando_ver_objeto

import html_estilo_texto
import html_elem_span
import html_elem_div
import html_pag_principal
import html_pag_mensagem_de_erro

import util_testes
from util_erros import erro_prog, mostra, aviso_prog

# Outras interfaces usadas por este módulo:
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, re, cgi
import urllib.parse

# Classe interna:

class Processador_de_pedido_HTTP(BaseHTTPRequestHandler):
  """Classe necessária para usar `HTTPServer`.  Os métodos
  {do_GET}, {do_POST}, e {do_HEAD} desta classe são chamados pelo
  servidor para processar um pedido HTTP do usuário.
  Eles devem devolver a resposta por meio de {devolve_pagina(hstr)}
  onde {hstr} é uma página em formato HTML (ou {None} em
  caso de erro), ou {devolve_imagem(arq)} onde {arq}
  é uma imagem, ou {devolve_video(arq)} onde {arq}
  é uma imagem."""

  # CAMPOS E MÉTODOS HERDADOS

  # Versao da classe, passada no dicionário {dados} aos métodos abaixo:
  server_version = "MC857"

  def do_GET(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'GET'."""
    return self.do_geral('GET')

  def do_POST(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'POST'."""
    return self.do_geral('POST')

  def do_HEAD(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'HEAD'."""
    return self.do_geral('HEAD')

  # CAMPOS E MÉTODOS INTERNOS

  def do_geral(self, tipo):
    # Processa um comando HHTP do {tipo} indicado ('GET','POST', ou 'HEAD').

    mostra(0, ("processando um comando HTTP %s ..." % tipo))

    # Extrai os dados do comando HTTP na forma de um dicionário:
    dados = self.extrai_dados(tipo)
    
    imagens_re = r"/(imagens|avatares|thumbs)/"
    if tipo == 'GET' and re.match(imagens_re, dados['real_path']):
      # Pedido de um arquivo:
      nome_imagem = dados['real_path'][1:]
      with open(nome_imagem, 'rb') as arq:
        imagem = arq.read()
      self.devolve_imagem(imagem)
    elif tipo == 'GET' and re.match(r"/videos/", dados['real_path']):
      # Pedido de um video stream:
      nome_video = dados['real_path'][1:]
      with open(nome_video, 'rb') as arq:
        video = arq.read()
      self.devolve_video(video)
    else:
      # Pedido de uma página HTML:

      # Determina a sessao à qual este comando se refere:
      ses = self.obtem_sessao(dados)
      
      # Verificação de comprimento, por segurança:
      cmd_len_max = 10000000 + 100000;  # Upload de arquivos até 10 MB:
      if 'content-length' in self.headers:
        cmd_len = int(self.headers['content-length'])
        # sys.stderr.write(f"@$@ do_geral({tipo}): cmd_len = {cmd_len}\n")
        if cmd_len > cmd_len_max:
          self.devolve_erro(ses, f"comando {tipo} muito longo ({cmd_len}, máximo {cmd_len_max})") 
          return

      # Processa o comando e constrói a página HTML de resposta:
      pag, ses_nova = processa_comando(tipo, ses, dados)
      pag_debug = str(pag)
      if len(pag_debug) > 207:
        pag_debug = pag_debug[0:100] + " [...] " + pag_debug[-100:]
      mostra(0, "pag = " + pag_debug + "")

      # Envia a página ao browser do usuário:
      self.devolve_pagina(ses_nova, pag)

  def extrai_dados(self, tipo):
    """Retorna todos os campos de um pedido do tipo {tipo} 
    ('GET','POST', ou 'HEAD') na forma de um dicionário Python {dados}.
    O valor do campo {dados['request_type']} é o {tipo} dado. Os demais
    campos são extraídos do {self} conforme especificado
    na classe {BaseHTTPRequestHandler}, com as seguintes adições:
     'headers': o valor é um sub-dicionário que é uma cópia
       de {self.headers}, contendo os itens do preâmbulo do pedido HTTP
       ('contents-type', etc.).
     'real_path': valor de {urlparse.urlparse(self.path).path}.
       No caso de 'GET', é a sub-cadeia do URL entre o último '/'
       e o '?'.  No caso de 'POST', é o atributo 'action' do <form>
       ou 'formaction' do botão tipo 'submit', com '/' na frente.
     'query':  o valor de {urlparse.urlparse(self.path).query}.
       no caso de 'GET', é a cadeia que segue o '?', possivelmente
       com códigos URL; por exemplo, 'foo=bar&bar=%28FOO%29&foo=qux'
     'query_data': o valor é um sub-dicionário com os argumentos de
       'query' destrinchados e com códigos URL convertidos
       para caracters Unicode.  Os valores são listas, para indicar
       repetição. Por exemplo, o 'query' acima viraria
       {'foo': ['bar','qux'], 'bar': ['(FOO)']}.  No caso de 'POST',
       é um dicionário vazio.
     'form_data': no caso de um comando 'POST',
       o valor é um sub-dicionário com os campos do formulário
       submetido. No caso de 'GET', é um dicionário vazio.
    """

    assert(self.command == tipo)

    dados = {} # Novo dicionário.

    # Campos originais do {BaseHTTPRequestHandler}
    dados['command'] = self.command
    dados['request_version'] = self.request_version
    dados['client_address'] = self.client_address
    dados['client_address_string'] = self.address_string()

    dados['date_time'] = self.log_date_time_string()
    dados['server_version'] = self.server_version
    dados['sys_version'] = self.sys_version
    dados['protocol_version'] = self.protocol_version

    dados['path'] = self.path # Por exemplo "/busca?

    # Campos adicionados por este módulo:
    parsed_path = urllib.parse.urlparse(self.path)
    dados['real_path'] = parsed_path.path
    dados['query'] =  parsed_path.query

    dados['headers'] = self.extrai_cabecalhos_http()

    dados['cookies'] = self.extrai_cookies(dados['headers'])

    dados['query_data'] = urllib.parse.parse_qs(dados['query'])

    dados['form_data'] = self.extrai_dados_de_formulario()

    return dados

  def extrai_cabecalhos_http(self):
    """Converte o campo {self.headers} em um dicionario Python, limpando
    brancos supérfluos."""
    hds = {} # Novo dicionario.
    for name, value in self.headers.items():
      hds[name] = value.rstrip()
    return hds

  def extrai_cookies(self, dados):
    """Analisa a cadeia {cook_str} que é o campo 'Cookie'
    do dicionário {dados}, que veio com os headers HTTP, convertendo-a
    em um dicionário Python.  Retorna esse dicionário.

    Supõe que {cook_str} é uma cadeia com formato '{chave1}={valor1};
    {chave2}={valor2}; {...}'. Os campos de valor não podem conter ';'
    ou '='. Se algum valor estiver envolvido em aspas, remove as aspas.
    Os campos de {cook_str} cujo valor é a cadeia 'None' ou vazia são omitidos."""
    cookies = {}
    if 'Cookie' in dados:
      cook_str = dados['Cookie']
      cook_els = re.split(r'[ ;]+', cook_str)
      for cook_el in cook_els:
        # A cadeia {cook_el} deve ser '{chave}={valor}'
        cook_pair = re.split(r'[=]', cook_el)
        assert len(cook_pair) == 2
        cook_key = cook_pair[0]
        assert cook_key != ""
        cook_val = (cook_pair[1]).strip("\"'")
        if cook_val != "" and cook_val != "None":
          cookies[cook_key] = cook_val
    return cookies

  def extrai_dados_de_formulario(self):
    """Se o comando é 'POST', extrai os dados do formulário, dos
    campos {self.rfile} e {self, headers}, na forma de um dicionário Python."""
    ffs = {} # Novo dicionário.
    if self.command == 'POST':
      # sys.stderr.write(f"@#@ extrai_dados_de_formulario: self.command = {str(self.command)}\n")
      formulario = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']}
      )
      # sys.stderr.write(f"@#@ extrai_dados_de_formulario: formulario = {str(formulario)[:2000]}\n")
      # Enumera os nomes dos campos presentes no formulário:
      for chave in formulario.keys():
        # sys.stderr.write(f"@#@ extrai_dados_de_formulario: chave = '{chave}'\n")
        # Pega a lista de todos os campos com nome {chave}:
        item_list = formulario.getlist(chave)
        # Enumera os campos com esse nome:
        for val in item_list:
          # sys.stderr.write(f"@#@ extrai_dados_de_formulario:   val = {str(val)[:64]}\n")
          # Armazena no dicionário:
          if chave in ffs:
            erro_prog("o formulário tem mais de um campo com nome '" + chave + "'")
          ffs[chave] = val
    return ffs

  def obtem_sessao(self, dados):
    """Determina a sessão à qual o comando HTTP se refere, ou {None}
    se o usuário não está logado, a partir do dicionário de cookies
    contidos em {dados}."""
    if not 'cookies' in dados:
      # Não temos cookies?
      return None
    cookies = dados['cookies']
    if 'sessao' in cookies:
      ses_id = cookies['sessao']
      ses = obj_sessao.obtem_objeto(ses_id)
    else:
      ses = None
    return ses

  def devolve_erro(self, msg):
    """Manda para o usuário uma página HTML 5.0. simples dizendo que houve erro
    no comando, com a mensagem {msg}."""
    pag = \
      "<!doctype html>\n" + \
      "<html>\n" + \
      "<head>\n" + \
      "<title>ERRO Comando Inválido</title>\n" + \
      "</head>\n" + \
      "<body bgcolor='#ffaa77'>" + \
      "<h2>O servidor MC857 recebeu um comando inválido<h2>\n" + \
      f"<h3>{msg}<h3>\n" + \
      "</body>\n" + \
      "</html>\n"
    self.devolve_pagina(ses, pag)
    return
  
  def devolve_pagina(self, ses, pag):
    """Manda para o usuário a {pag} dada, que deve ser um string
    com o conteúdo da página em HTML 5.0, com os preâmulos adequados
    segundo o protocolo HTTP.
    Se {pag} é {None}, sinaliza no preâmbulo o código 404 com conteúdo 'text/plain',
    mensagem 'Não encontrado'. Caso contrário, devolve a página com código 200 e
    'content-type' 'text/html'.

    Se {ses} não é {None}, deve ser um objeto da classe {ObjSession}.
    Nesse caso, a função inclui no preâmbulo cookies que identificam a
    sessão e o o usuário."""

    if pag == None:
      aviso_prog("Página a devolver é {None}", True)
      codigo = 404  # Error - Not found.
      msg = "Pagina nao encontrada - Page not found"
      tipo = 'text/plain'
      pag = html_pag_mensagem_de_erro.gera(ses, msg)
      if pag == None:
        aviso_prog("Função {html_pag_mensagem_de_erro.gera} devolveu {None}", True)
        #  Na marra:
        pag = "<!doctype html>\n<html>\n<body>\n" + msg + "\n</body>\n</head>"
    else:
      codigo = 200  # No error.
      tipo = 'text/html'

    self.send_response(codigo)
    self.send_header('Content-type', tipo)

    # Manda cookies que identificam usuário e sessão:
    if ses != None:
      ses_id = obj_sessao.obtem_identificador(ses)
      cookie = obj_sessao.obtem_cookie(ses)
      ses_dono = obj_sessao.obtem_dono(ses)
      ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
    else:
      ses_id = ""
      cookie = ""
      ses_dono = None
      ses_dono_id = ""
    self.send_header('Set-Cookie', 'usuario=' + ses_dono_id)
    self.send_header('Set-Cookie', 'sessao=' + ses_id)
    self.send_header('Set-Cookie', 'cookie_sessao=' + cookie)

    self.end_headers()
    self.wfile.write(pag.encode('utf-8'))

  def devolve_imagem(self, imagem):
    """Manda para o usuário a {imagem} dada, que deve ser um string
    com o conteúdo de uma imagem PNG."""

    codigo = 200  # No error.
    tipo = 'image/PNG'

    self.send_response(codigo)
    self.send_header('Content-type', tipo)
    self.end_headers()
    self.wfile.write(imagem)

  def devolve_video(self, video):
    """Manda para o usuário o {video} dado, que deve ser um string
    com o conteúdo de um video MP4."""

    codigo = 200  # No error.
    tipo = 'video/mp4'

    self.send_response(codigo)
    self.send_header('Content-type', tipo)
    self.end_headers()
    self.wfile.write(video)

def cria_objeto_servidor(host, porta):
  endereco = (host, porta)
  serv = HTTPServer(endereco, Processador_de_pedido_HTTP)
  return serv

# FUNÇÕES INTERNAS

def processa_comando(tipo, ses, dados):
  """Esta função processa um comando HTTP 'GET', 'POST', ou 'HEAD' recebido pelo
  servidor, com as informações convertidas em um dicionario {dados}.

  A sessão {ses} deve ser a sessão deduzida a partir dos cookies que
  viram com o comando HTTP.

  Esta função devolve a página {pag} a ser enviada ao usuário.  Devolve também
  a sessão {ses_nova} corrente.  Esta sessão pode ser diferente de {ses}, se o
  comando for login ou logout."""

  mostra_dados(dados)

  mostra_cmd = True # Deve mostrar os dados do comando no final da página?

  cmd = dados['real_path']; del dados['real_path']

  # Define página a retornar {pag} e a sessão {ses_nova} para futuros comandos:
  ses_nova = ses  # Geralmente a sessão não muda
  if tipo == 'GET' or tipo == 'POST':
    # Obtem os argumentos do comando:
    if tipo == 'GET':
      # Comando causado por acesso inicial ou botão simples:
      cmd_args = dados['query_data']; del dados['query_data'] # Argumentos do comando "GET", no próprio URL "cmd?n1=v1&n2=v2...".
    elif tipo == 'POST':
      # Comando causado por botão do tipo "submit" dentro de um <form>...</form>:
      cmd_args = dados['form_data']; del dados['form_data'] # Campos do formulário.
    else:
      assert False

    # Remove parenteses e colchetes supérfluos em {cmd_args}:
    cmd_args = descasca_argumentos(cmd_args)

    # Despacha o comando:
    # !!! Completar a lista abaixo com todos os módulos {comando_*.py} que existem. !!!

    ses_id = obj_sessao.obtem_identificador(ses) if ses != None else "None"
    sys.stderr.write("  !! {processa_comando_hhtp.processa_comando}: " + f"ses = {ses_id} cmd = {str(cmd)}\n")

    # --- comandos gerais ------------------------------------------------

    if cmd == '' or cmd == '/' or cmd == '/pag_principal':
      # Acesso sem comando, ou usuário apertou "Principal" no menu geral.
      pag =  html_pag_principal.gera(ses, [])

    elif cmd == '/ver_objeto':
      # Quer ver os atributos de um objeto:
      pag = comando_ver_objeto.processa(ses, cmd_args)

    # --- comandos referentes a {obj_usuario.Classe} ------------------------

    elif cmd == '/ver_usuario':
      # Quer ver dados de algum usuário:
      pag = comando_ver_usuario.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_cadastrar_usuario':
      # Quer formumlário para cadastrar novo usuário:
      pag = comando_solicitar_pag_cadastrar_usuario.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_alterar_usuario':
      # Quer formumlário para alterar novo usuário:
      pag = comando_solicitar_pag_alterar_usuario.processa(ses, cmd_args)

    elif cmd == '/cadastrar_usuario':
      # Preencheu atributos de novo usuário e quer executar a criação:
      pag = comando_cadastrar_usuario.processa(ses, cmd_args)

    elif cmd == '/alterar_usuario':
      # Alterou atributos de usuário no formulário e quer executar as mudanças:
      pag = comando_alterar_usuario.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_buscar_usuarios':
      # Quer formumlário para buscar usuários por campos variados:
      pag = comando_solicitar_pag_buscar_usuarios.processa(ses, cmd_args)

    elif cmd == '/buscar_usuarios':
      # Quer formumlário para cadastrar novo usuário:
      pag = comando_buscar_usuarios.processa(ses, cmd_args)

    # --- comandos referentes a {obj_sessao.Classe} -----------------------

    elif cmd == '/ver_sessao':
      pag = comando_ver_sessao.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_login':
      # Qer formulário para fazer "login":
      # ATENÇÃO: Este comando só mostra o formulário de login, não muda a sessão ainda.
      pag = comando_solicitar_pag_login.processa(ses, cmd_args)

    elif cmd == '/fazer_login':
      # Preencheu o formulário de login e quer entrar (criar nova sessão):
      # ATENÇÃO: devolve também a nova sessão (que pode ser {None} se o login não deu certo).
      pag, ses_nova = comando_fazer_login.processa(ses, cmd_args)

    elif cmd == '/fazer_logout':
      # Quer fazer "logout" (fechar a sessão corrente):
      # ATENÇÃO: devolve também a nova sessão (que geralmente vai ser {None}).
      pag, ses_nova = comando_fazer_logout.processa(ses, cmd_args)

    elif cmd == '/fechar_sessao':
      # Quer encerrar uma sessão dada:
      pag = comando_fechar_sessao.processa(ses, cmd_args)

    elif cmd == '/buscar_sessoes_de_usuario':
      # Lista as sessões de determinado usuário:
      pag = comando_buscar_sessoes_de_usuario.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_buscar_sessoes':
      # Quer formumlário para buscar sessões por campos variados:
      pag = comando_solicitar_pag_buscar_sessoes.processa(ses, cmd_args)

    elif cmd == '/buscar_sessoes':
      # Efetua a busca de sessões por atributos variados:
      pag = comando_buscar_sessoes.processa(ses, cmd_args)

    # --- comandos referentes a {obj_video.Classe} -----------------------
      
    elif cmd == '/ver_video':
      # Página que mostra um detetrminado vídeo:
      pag = comando_ver_video.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_upload_video':
      # Quer formulário para fazer upload de um video:
      pag = comando_solicitar_pag_upload_video.processa(ses, cmd_args)

    elif cmd == '/fazer_upload_video':
      # Preencheu o formulário de upload de video e quer fazer o upload:
      pag = comando_fazer_upload_video.processa(ses, cmd_args)

    elif cmd == '/solicitar_pag_alterar_video':
      # Quer formulário para alterar atributos de um video:
      pag = comando_solicitar_pag_alterar_video(ses, cmd_args)

    elif cmd == '/alterar_video':
      # Preencheu formulário e quer efetuar as alterações:
      pag = comando_alterar_video.processa(ses, cmd_args)
      
    elif cmd == '/solicitar_pag_buscar_videos':
      # Quer formumlário para buscar vídeos por campos variados:
      pag = comando_solicitar_pag_buscar_videos.processa(ses, cmd_args)
    
    elif cmd == '/buscar_videos':
      # Preencheu parâmetros e quer executar a busca:
      pag = comando_buscar_videos.processa(ses, cmd_args)
      
    elif cmd == '/buscar_videos_de_usuario':
      # Quer lista dos vídeos de algum usuário:
      pag = comando_buscar_videos_de_usuario.processa(ses, cmd_args)
      
    elif cmd == '/ver_grade_de_videos':
      # Quer lista dos vídeos de algum usuário:
      pag = comando_ver_grade_de_videos.processa(ses, cmd_args)

    # --- comandos referentes a {obj_comentario.Classe} -----------------------
      
    elif cmd == '/ver_comentario':
      # Página que mostra um determinado comentário:
      pag = comando_ver_comentario.processa(ses, cmd_args)
      
    elif cmd == '/solicitar_pag_postar_comentario':
      # Quer formumlário para postar um comentário a um vídeo ou resposta:
      pag = comando_solicitar_pag_postar_comentario.processa(ses, cmd_args)
      
    elif cmd == '/postar_comentario':
      # Acrescenta o comentário com o texto preenchido:
      pag = comando_postar_comentario.processa(ses, cmd_args)
      
    elif cmd == '/solicitar_pag_alterar_comentario':
      # Quer forumlário para editar um comentário existente:
      pag = comando_solicitar_pag_alterar_comentario.processa(ses, cmd_args)
      
    elif cmd == '/alterar_comentario':
      # Efetua alterações especificadas num comentário:
      pag = comando_alterar_comentario.processa(ses, cmd_args)
      
    elif cmd == '/solicitar_pag_buscar_comentarios':
      # Quer formumlário para buscar comentarios por campos variados:
      pag = comando_solicitar_pag_buscar_comentarios.processa(ses, cmd_args)
      
    elif cmd == '/buscar_comentarios':
      # Busca de comentáriso com certos atributos:
      pag = comando_buscar_comentarios.processa(ses, cmd_args)
      
    elif cmd == '/buscar_comentarios_de_usuario':
      # Quer lista de comentários de algum usuário:
      pag = comando_buscar_comentarios_de_usuario.processa(ses, cmd_args)
      
    elif cmd == '/buscar_comentarios_de_video':
      # Quer lista de comentários de algum video:
      pag = comando_buscar_comentarios_de_video.processa(ses, cmd_args)
      
    elif cmd == '/buscar_respostas_de_comentario':
      # Quer lista de comentários que são respostas de algum comentário:
      pag = comando_buscar_respostas_de_comentario.processa(ses, cmd_args)
      
    elif cmd == '/ver_conversa':
      # Quer lista de comentários que são respostas de algum comentário:
      pag = comando_ver_conversa.processa(ses, cmd_args)

    # --- outros comandos -----------------------

    else:
      # Comando não identificado
      pag =  html_pag_mensagem_de_erro.gera(ses, ("** comando POST \"%s\" inválido" % cmd))

  elif tipo == 'HEAD':
    # Comando emitido por proxy server:
    # !!! (MAIS TARDE) Tratar este caso !!!
    cmd_args = {}
    pag =  html_pag_mensagem_de_erro.gera(ses, ("** comando HEAD \"%s\" não implementado" % cmd))
  else:
    # Tipo de comando inválido:
    cmd_args = {}
    pag =  html_pag_mensagem_de_erro.gera(ses, ("** comando \"%s\" não implementado" % tipo))

  if pag == None:
    pag = html_pag_mensagem_de_erro.gera(ses, [ "Resultado do comando foi {None}" ])
  elif re.match(r"^ *[!*][!*]", pag) != None:
    # Parece mais mensagem de erro que página
    pag = html_pag_mensagem_de_erro.gera(ses, [ "Resultado do comando foi:", pag ])
  
  sys.stderr.write("    pag resultado =\n%s\n" % pag)

  if mostra_cmd:
    # Acrescenta os dados do comando para depuração:
    ht_cmd = formata_dados_http(cmd,cmd_args,dados,True)
    sys.stderr.write(f"{'~'*70}\n{ht_cmd}\n{'~'*70}\n")
    ebdix = pag.find('</body>')
    pag = pag[:ebdix] + "<br/>" + ht_cmd + "<br/><br/></body>" 

  return pag, ses_nova

def formata_dados_http(cmd, cmd_args, resto, html):
  """
  Esta função de depuração devolve um string que mostra a função {cmd}
  que foi executada, o dicionário {cmd_args} com os argumentos da mesma,
  e o dicionário {resto} com os demais parâmetros do comando HTTP
  recebido. 
  
  Se o booleano {html} é {False}, o resultado é prórpio para imprimir
  em {stderr}. Se {html} é {True}, o resultado é um trecho de HTML5 a
  ser inserido no final de uma página. Nos dois casos, os dados são
  formatados de maneira mais ou menos legível, e campos muito longos são
  truncados.
  """
  resto_d = resto.copy()
  tipo = resto_d['command']; del resto_d['command'] # 'GET', 'POST', ou 'HEAD'
  # Dados principais:
  max_len = 2000
  ht_cmd_args = util_testes.formata_valor(cmd_args, html, max_len)
  ht_resto = util_testes.formata_valor(resto_d, html, max_len)

  # Monta um bloco HTML com os dados de depuração:
  ht_tit = (f"Resposta a comando HTTP \"{tipo}\" recebido com dados principais:")
  if html:
    ht_cmd =      f"<br/>cmd = \"{cmd}\"<br/>"
    ht_cmd_args = "cmd_args =<br/>" + ht_cmd_args 
    ht_resto =    "<br/><hr/>Outros dados:<br/>" + ht_resto
  else:
    ht_cmd =      f"\ncmd = \"{cmd}\"\n"
    ht_cmd_args = "cmd_args =\n" + ht_cmd_args 
    ht_resto =    "\n" + ("-"*70) + "Outros dados:\n" + ht_resto
  
  ht_conteudo = ht_tit + ht_cmd + ht_cmd_args + ht_resto

  if html:
    cor_texto = "#000000"
    cor_fundo = None
    margens = None
    estilo = html_estilo_texto.gera("18px", "medium", cor_texto, cor_fundo, margens)
    ht_conteudo = html_elem_span.gera(estilo, ht_conteudo)
    ht_conteudo = "<hr/>\n" + html_elem_div.gera("background-color:#bbbbbb;", ht_conteudo) + "<hr/>\n"
  return ht_conteudo

def mostra_dados(dado):
  """Esta função de depuração imprime o valor simples ou estruturado {dado} em {stderr}, 
  formatado e com os campos longs devidamente truncados."""
  
  html = False
  max_len = 2000
  dado = util_testes.formata_valor(dado, html, max_len)
  sys.stderr.write(("-"*70)+"\n")
  sys.stderr.write("dado =\n")
  sys.stderr.write(dado)
  sys.stderr.write(("-"*70)+"\n")

def descasca_argumentos(cmd_args):
  """Dado um dicionário de argumentos extraídos de um comando GET ou POST,
  devolve uma cópia do mesmo onde cada valor que é uma tupla (ou lista) de 
  comprimento 1 é substituído por seu único elemento."""
  args_new = {}
  for ch, val in cmd_args.items():
    if val != None and (type(val) is list or type(val) is tuple):
      if len(val) == 1:
        val = val[0]
    args_new[ch] = val
  return args_new


# !!! Comandos que tratam dados vindos de formularios devem liminar brancos e newlines inciais e finais de valores de campos antes de validar e usar. !!!
