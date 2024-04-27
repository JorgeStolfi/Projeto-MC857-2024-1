import obj_sessao
import obj_usuario

import html_bloco_cabecalho
import html_bloco_menu_geral
import html_bloco_erro
import html_elem_span
import html_bloco_rodape

import re
import sys

pgn_debug = False

def gera(ses, ht_conteudo, erros):
  # Cabeçalho das páginas:
  ht_cabe = html_bloco_cabecalho.gera("Oito-Cinco-Sete", True)

  logado = (ses != None)
  if logado:
    usr = obj_sessao.obtem_usuario(ses)

    nome_usuario = obj_usuario.obtem_atributos(usr)['nome']
    admin = obj_usuario.obtem_atributos(usr)['administrador']
    id_usr = obj_usuario.obtem_identificador(usr)
    num_ses = len(obj_sessao.busca_por_usuario(usr, True));
    if pgn_debug: sys.stderr.write("  > usuario %s num_ses = %d\n" % (id_usr, num_ses))
  else:
    nome_usuario = None
    admin = False
    num_ses = 0

  # Menu geral no alto da página:
  ht_menu = html_bloco_menu_geral.gera(logado, nome_usuario, admin)

  # Mensagem de multiplas sessoes:
  if num_ses > 1:
    estilo_multi_ses = None; # cor_texto = "#FF0000" cor_fundo = "#eeeeee"
    if num_ses == 2:
      ht_multi_ses = html_elem_span.gera(estilo_multi_ses, "Você tem outra sessao aberta.")
    else:
      ht_multi_ses = html_elem_span.gera(estilo_multi_ses, "Você tem outras %d sessoes abertas." % (num_ses-1))
  else:
    ht_multi_ses = None

  if logado:
    ht_nome_usuario = gera_nome_e_avatar_usuario(id_usr, nome_usuario, admin)
  else:
    ht_nome_usuario = None

  # Mensagens de erro - quebra e limpa:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Split lines, create a list:
    erros = re.split('[\n]', erros)
  assert type(erros) is list or type(erros) is tuple
  erros = [ er for er in erros if er != None ]
  erros = [ er.strip() for er in erros ]
  erros = [ er for er in erros if len(er) > 0 ]
  if len(erros) != 0:
    erros = "<br/>\n" + "<br/>\n".join(erros)
    ht_erros = html_bloco_erro.gera(erros) + "\n"
  else:
    ht_erros = ""

  # Rodapé da página:
  ht_roda = html_bloco_rodape.gera()

  # Monta a página:
  pagina = \
    ht_cabe + "<br/>\n" + \
    ht_menu + "<br/>\n" + \
    ( ht_multi_ses + "<br/>\n" if ht_multi_ses != None else "" ) + \
    ( ht_nome_usuario + "<br/>\n" if ht_nome_usuario != None else "" ) + \
    ht_erros + "<br/>\n" + \
    ht_conteudo + "<br/>\n" + \
    ht_roda
  return pagina

def gera_nome_e_avatar_usuario(id_usr, nome_usuario, admin):
  """Gera o avatar e o texto "Oi {nome}" para uma página genérica.  O parâmetro {admin} diz se é administrador."""
  avatar = ("<img src=\"avatares/avatar_" + id_usr + ".png\" style=\"float:left;height:20px;\"/>")
  nome = html_elem_span.gera(None, "Oi,  " + nome_usuario)
  
  return avatar + "&nbsp;" + nome
