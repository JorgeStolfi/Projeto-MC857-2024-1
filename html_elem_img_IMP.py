
def gera(nome, alt, tam):
  """Constrói o HTML para a imagem com nome {nome} e texto alternativo {alt},
  com {tam} pixels de altura."""

  #Se receber valor {None}, converte string para vazia
  if nome is None:
      nome = ""

  #Se campo nome não for string {vazia} carrega imagem solicitada, senão carrega imagem cinza.png
  if nome and not nome.isspace():
      ht_img = ("<img src=\"imagens/" + nome + "\" alt=\"" + alt + "\" style=\"float:left;height:%dpx;\"/>" % tam)
  else:
      ht_img = ("<img src=\"imagens/cinza.png" + nome + "\" alt=\"" + alt + "\" style=\"float:left;height:%dpx;\"/>" % tam)

  return ht_img
