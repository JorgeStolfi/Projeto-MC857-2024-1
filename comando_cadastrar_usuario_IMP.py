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
  
  # Estas condições devem valer para comandos emitidos por páginas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe), "sessão inválida"
  if ses != None: assert obj_sessao.aberta(ses), "sessão  já foi fechada"
  assert isinstance(cmd_args, dict), "argumentos inválidos para o comando"
  
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = []
  
  # Tenta criar o usuário:
  erros += obj_usuario.confere_e_elimina_conf_senha(cmd_args)
  
  if len(erros) == 0:
    try:
      usr = obj_usuario.cria(cmd_args)
      pag = html_pag_login.gera(None)
    except ErroAtrib as ex:
      erros += ex.args[0]
      sys.stderr.write(f"Erro na criação de usuário: {erros}\n")
      # Repete a página de cadastrar com os mesmos argumentos (menos senha) e mens de erro:
      cmd_args.pop('senha')
      pag = html_pag_cadastrar_usuario.gera(ses, cmd_args, erros)
  return pag
