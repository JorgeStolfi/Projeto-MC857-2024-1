import obj_usuario
import obj_sessao
import obj_video
import html_pag_mensagem_de_erro
import html_pag_upload_video
import html_pag_ver_video

def processa(ses, cmd_args):
  
  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  cmd_args = cmd_args.copy() # Para não estragar o original.
  erros = []
  
  # Obtem o dono da sessão:
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação")
    ses_dono = None
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação")
    ses_dono = None
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
  
  # O autor do vídeo será sempre o dono da sessão:
  autor = ses_dono
  if autor != None:
    autor_id = obj_usuario.obtem_identificador(autor)

    # Verifica parâmetro redundante 'autor':
    for chave in 'usuario', 'autor':
      if chave in cmd_args:
        val = cmd_args[chave]
        if val != None and val != autor_id:
          erros.append(f"Argumento de busca inválido '{chave}' = {val} inválido, devia ser {autor_id}")
        del cmd_args[chave]

  if 'titulo' in cmd_args:
    titulo = cmd_args.pop('titulo')
    if titulo == None or len(titulo) == 0:
      erros.append("O título do vídeo não foi definido") 
      titulo = None
    
  # Pega o conteúdo (bytes) do arquivo:
  if 'arquivo' in cmd_args:
    conteudo = cmd_args.pop('arquivo')
  elif 'conteudo' in cmd_args:
    conteudo = cmd_args.pop('conteudo')
  else:
    erros.append("Os bytes do vídeo não foram enviados") 
    conteudo = None
  
  # A nota inicial é sempre 2.0:
  nota = 2.0 
  
  if len(cmd_args) != 0:
    lixo = ",".join(map(lambda x: f"'{x}'", cmd_args.keys()))
    erros.append(f"Atributos espúrios especifcados: {lixo}")

  if len(erros) == 0:
    atrs_cria = { 'autor': autor, 'titulo': titulo, }
    if conteudo != None: atrs_cria['conteudo'] = conteudo
    atrs_cria['nota'] = nota
    
    # Salva o arquivo, cria o objeto, e registra na tabela de vídeos:
    try:
      vid = obj_video.cria(atrs_cria)
    except ErroAtrib as ex:
      erros += ex.args[0]
      vid = None
  else:
    vid = None
    
  if vid != None:
    # Criou o novo vídeo com sucesso:
    pag = html_pag_ver_video.gera(ses, vid, erros)
  elif ses_dono != None:
    # Comando falhou; repita o formulário com campos essenciais:
    cmd_args_novo = { }
    if titulo != None: cmd_args_novo['titulo'] = titulo
    # Atributos 'autor', 'nota', etc não devem existir.
    pag = html_pag_upload_video.gera(ses, cmd_args_novo, erros)
  else:
    # Não vale a pena repetir o formulário
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
