import obj_usuario
import html_elem_item_de_resumo
import html_elem_button_simples
import html_elem_link_text

def gera(admin, usr):
  
  atrs = obj_usuario.obtem_atributos(usr) if usr != None else None

  ht_campos = []
  
  colunas = [ 'usuario', 'admin', 'email', 'nome' , 'vnota']

  for chave in colunas:
    if chave == 'usuario':
      mostra = True
      texto = html_elem_link_text.gera(obj_usuario.obtem_identificador(usr), "ver_usuario", { 'usuario': obj_usuario.obtem_identificador(usr) }) if usr != None else "Usuário"
    elif chave == 'admin':
      mostra = True
      texto = ("Sim" if atrs['administrador'] else "") if usr != None else chave.capitalize()
    elif chave == 'email':
      mostra = True
      if admin:
        texto = str(atrs[chave]) if usr != None else chave.capitalize()
      else:
        mostra = False
    elif chave == 'vnota':
      mostra = True
      texto = str(atrs['vnota']) if usr != None else "Nota"
    else:
      mostra = True
      texto = str(atrs[chave]) if usr != None else chave.capitalize()
      
    if mostra:
      cab = (usr == None)
      cor_fundo = None
      cor_texto = None
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha, cor_texto)
      ht_campos.append(ht_item)

  if usr != None:
    bt_arg = { 'usuario': obj_usuario.obtem_identificador(usr) }
    bt_ver = html_elem_button_simples.gera("Ver", "ver_usuario", bt_arg, None)
    ht_campos.append("<td>" + bt_ver + "</td>")

  return ht_campos
