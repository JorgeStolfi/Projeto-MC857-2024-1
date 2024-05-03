
def gera(arquivo, descr, alt_px):

  # Se receber valor {None}, converte string para vazia
  if arquivo is None: 
    arquivo = "imagens/cinza.png"
    if descr == None: descr = "** Imagem não especificada."
  else:
    if descr == None: descr = f"Imagem {arquivo}"

  # O atributo {alt} é para quando a imagem não pode ser mostrada; {title} é o que aparece no mouse hover.
  ht_img = ("<img src=\"%s\" alt=\"%s\" title=\"%s\" style=\"float:left;height:%dpx;\"/>" % (arquivo, descr, descr, alt_px))

  return ht_img
