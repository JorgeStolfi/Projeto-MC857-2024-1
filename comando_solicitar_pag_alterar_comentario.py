import comando_solicitar_pag_alterar_comentario_IMP

def processa(ses, cmd_args):
  """
  Esta função trata o comando HTTP "solicitar_pag_alterar_comentario"
  recebido pelo servidor do site. Esse comando tipicamente é emitido
  pelo browser quando o usuário aperta um botão "Alterar" ou equivalente
  para alterar os dados de um comentário {com} qualquer. A função retorna uma
  página que permite alterar atributos desse comentário.
  
  O argumento {ses} é a sessão de login que emitiu o comando. Não pode
  ser {None} e deve ser um objeto de tipo {obj_sessao.Classe}
  representando uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário contendo os argumentos do comando.
  Deve conter um único campo 'comentario' com o identificador do comentário a alterar.
  
  O dono da sessão {ses} deve ser um administrador ou o autor do comentário {com}.
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados do comentário {com}. Veja {html_pag_alterar_comentario.gera}.
  Alguns atributos do comentário (como o autor e data) serão exibidos
  mas não poderão ser ser alterados, nem mesmo pelo administrador. A
  página terá um botão de submissão "Salvar", "Confirmar" ou equivalente
  que emite um comando HTTP "alterar_comentario".
  """
  return comando_solicitar_pag_alterar_comentario_IMP.processa(ses, cmd_args)

