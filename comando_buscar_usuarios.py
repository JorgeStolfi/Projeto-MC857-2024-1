import comando_buscar_usuarios_IMP

def processa(ses, args):
  """
  Esta função é chamada quando o usuário aperta o botão "Buscar" em uma
  formulário de busca de usuario (vide {html_form_buscar_usuarios.gera}).
  
  O parâmetro {ses} é uma sessão atualmente aberta.
  
  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_usuario} (vide {obj_usuario.py}). Por exemplo,
  {{'nome': "João", 'email': "joao@email.com"}}. Campos de {args} com
  valor {None} devem ser ignorados. O campo {args} deve conter pelos
  menos um dos atributos do {obj_usuario.Classe}, e/ou o campo 'id_usuario'
  com o identificador do usuário. A função deve procurar na base de
  dados os usuários que casam estes dados.

  O resultado deve ser uma página com a lista dos usuários encontrados, gerada
  por {html_pag_lista_de_usuarios.gera}.
  """
  return comando_buscar_usuarios_IMP.processa(ses, args)
