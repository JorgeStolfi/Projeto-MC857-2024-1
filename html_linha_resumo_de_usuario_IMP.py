import obj_usuario
import html_elem_item_de_resumo
import html_elem_button_simples

def gera(usr):
  
  atrs = obj_usuario.obtem_atributos(usr) if usr != None else None

  ht_campos = []
  
  colunas = [ 'usuario', 'admin', 'email', 'nome' ]

  for chave in colunas:
    if chave == 'usuario':
      mostra = True
      texto = obj_usuario.obtem_identificador(usr) if usr != None else "Usuário"
    elif chave == 'admin':
      mostra = True
      texto = ("ADMIN" if atrs['administrador'] else "") if usr != None else ""
    else:
      mostra = True
      texto = str(atrs[chave]) if usr != None else chave.capitalize()
      
    if mostra:
      cab = (usr == None)
      cor_fundo = None
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha)
      ht_campos.append(ht_item)

  if usr != None:
    bt_arg = { 'usuario': obj_usuario.obtem_identificador(usr) }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_usuario", bt_arg, '#eeee55')
    ht_campos.append("<td>" + bt_ver + "</td>")

  return ht_campos
