# Implementação do módulo {comando_cadastrar_usuario}.

import html_pag_login
import html_pag_cadastrar_usuario
import obj_usuario
import obj_sessao
from util_erros import ErroAtrib, erro_prog, mostra
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):
  # Tenta criar o usuário:
  try:
    obj_usuario.confere_e_elimina_conf_senha(cmd_args)
    usr = obj_usuario.cria(cmd_args)
    pag = html_pag_login.gera(ses, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_cadastrar_usuario.gera(ses, cmd_args, erros)
  return pag
