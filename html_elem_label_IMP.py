
def gera(texto, sep):
  if texto == None or texto == "":
    return ""
  else:
    return "<label>" + texto + (sep if sep != None else "") + "</label>"
